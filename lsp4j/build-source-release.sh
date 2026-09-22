set -euo pipefail

output=$(realpath "$1")
lsp_sources=$(realpath "$2")
jsonrpc_sources=$(realpath "$3")
gson=$(realpath "$4")
rm -rf "$output"
mkdir -p "$output/jsonrpc-src" "$output/jsonrpc-classes" "$output/lsp-src" "$output/lsp-classes"
(cd "$output/jsonrpc-src" && jar xf "$jsonrpc_sources")
find "$output/jsonrpc-src" -name '*.java' | LC_ALL=C sort > "$output/jsonrpc-sources"
javac --release 11 -proc:none -encoding UTF-8 -cp "$gson" -d "$output/jsonrpc-classes" @"$output/jsonrpc-sources"
cp "$output/jsonrpc-src/about.html" "$output/jsonrpc-classes/"
printf 'Manifest-Version: 1.0\nAutomatic-Module-Name: org.eclipse.lsp4j.jsonrpc\n\n' > "$output/jsonrpc.mf"
jar --create --file "$output/org.eclipse.lsp4j.jsonrpc.jar" --manifest "$output/jsonrpc.mf" -C "$output/jsonrpc-classes" .
(cd "$output/lsp-src" && jar xf "$lsp_sources")
find "$output/lsp-src" -name '*.java' | LC_ALL=C sort > "$output/lsp-sources"
javac --release 11 -proc:none -encoding UTF-8 -cp "$output/org.eclipse.lsp4j.jsonrpc.jar:$gson" -d "$output/lsp-classes" @"$output/lsp-sources"
cp "$output/lsp-src/about.html" "$output/lsp-classes/"
printf 'Manifest-Version: 1.0\nAutomatic-Module-Name: org.eclipse.lsp4j\n\n' > "$output/lsp.mf"
jar --create --file "$output/org.eclipse.lsp4j.jar" --manifest "$output/lsp.mf" -C "$output/lsp-classes" .
