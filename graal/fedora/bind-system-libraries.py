import argparse
import ast
import hashlib
import json
import pprint
import subprocess
from pathlib import Path

parser = argparse.ArgumentParser()
parser.add_argument("suite", type=Path)
parser.add_argument("bindings", type=Path)
parser.add_argument("profile")
args = parser.parse_args()
source = args.suite.read_text(encoding="utf-8")
lines = source.splitlines(keepends=True)
offsets = [0]
for line in lines:
    offsets.append(offsets[-1] + len(line))
suite = next(node.value for node in ast.parse(source).body if isinstance(node, ast.Assign)
             and any(isinstance(target, ast.Name) and target.id == "suite" for target in node.targets))
libraries = next(value for key, value in zip(suite.keys, suite.values) if ast.literal_eval(key) == "libraries")
nodes = {ast.literal_eval(key): value for key, value in zip(libraries.keys, libraries.values)}
edits = []
manifest = json.loads(args.bindings.read_text(encoding="utf-8"))
for name in manifest["profiles"][args.profile]:
    binding = manifest["libraries"][name]
    node = nodes[name]
    library = ast.literal_eval(node)
    jar = Path(binding["path"]).resolve(strict=True)
    library["moduleName"] = subprocess.run(
        ["java", str(Path(__file__).with_name("DescribeModules.java")), str(jar)],
        check=True, text=True, stdout=subprocess.PIPE).stdout.strip()
    library["urls"] = [jar.as_uri()]
    library["digest"] = "sha512:" + hashlib.sha512(jar.read_bytes()).hexdigest()
    library["maven"]["version"] = binding["version"]
    for attribute in ("path", "sourcePath", "sourceUrls", "sourceDigest"):
        library.pop(attribute, None)
    edits.append((offsets[node.lineno - 1] + node.col_offset,
                  offsets[node.end_lineno - 1] + node.end_col_offset,
                  pprint.pformat(library, sort_dicts=False, width=1000000)))
for start, end, replacement in sorted(edits, reverse=True):
    source = source[:start] + replacement + source[end:]
args.suite.write_text(source, encoding="utf-8", newline="\n")
