import hashlib
import json
import re
import struct
import subprocess
import sys
import zipfile
from pathlib import Path

artifact = Path(sys.argv[1])
with zipfile.ZipFile(artifact) as archive:
    names = archive.namelist()
    assert not any("ch/randelshofer/fastdoubleparser/" in name or "/internal/shaded/fdp/" in name for name in names)
    assert not any(name.endswith(".jar") for name in names)
    base_classes = [name for name in names if name.endswith(".class") and not name.startswith("META-INF/")]
    assert base_classes
    versions = {struct.unpack(">H", archive.read(name)[6:8])[0] for name in base_classes}
    assert versions == {52}, versions
    assert "META-INF/versions/9/module-info.class" in names
    manifest = re.sub(r"\r?\n ", "", archive.read("META-INF/MANIFEST.MF").decode("utf-8"))
    imports = re.search(r"(?m)^Import-Package: (.*)", manifest).group(1)
    assert "ch.randelshofer.fastdoubleparser" in imports
    assert archive.read("META-INF/services/com.fasterxml.jackson.core.JsonFactory").decode("utf-8").strip() == "com.fasterxml.jackson.core.JsonFactory"
module = subprocess.check_output(["jar", "--describe-module", "--file", str(artifact), "--release", "9"], text=True)
assert "requires ch.randelshofer.fastdoubleparser" in module
assert "provides com.fasterxml.jackson.core.JsonFactory with com.fasterxml.jackson.core.JsonFactory" in module
print(json.dumps({"artifact": artifact.name, "sha256": hashlib.sha256(artifact.read_bytes()).hexdigest(), "base_class_count": len(base_classes), "base_class_major_version": 52, "bundled_fastdoubleparser": False, "jpms_external_dependency": True, "osgi_external_import": True, "service_provider": True}, indent=2))
