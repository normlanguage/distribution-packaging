set -euo pipefail

graal_root=$1
test_sources=$(cd -- "$(dirname -- "$0")" && pwd)
test_output=$(mktemp -d)
trap 'rm -rf -- "$test_output"' EXIT
mkdir -p "$test_output/home"
modules=()
for name in collections word nativeimage jniutils nativebridge polyglot; do
    modules+=("$graal_root/sdk/mxbuild/dists/$name.jar")
done
for name in truffle-api truffle-compiler truffle-runtime; do
    modules+=("$graal_root/truffle/mxbuild/dists/$name.jar")
done
for name in asm asm-tree asm-commons; do
    modules+=("/usr/share/java/objectweb-asm/$name.jar")
done
module_path=$(IFS=:; printf '%s' "${modules[*]}")
processor_path="$graal_root/truffle/mxbuild/dists/truffle-dsl-processor.jar:/usr/share/java/antlr4/antlr4-runtime.jar"
java --module-path "$module_path" --validate-modules
javac --module-path "$module_path" --add-modules ALL-MODULE-PATH     -processorpath "$processor_path" -d "$test_output/classes" -s "$test_output/generated"     "$test_sources/AddOneNode.java" "$test_sources/TruffleCheck.java"
java --module-path "$module_path" --add-modules ALL-MODULE-PATH     -Duser.home="$test_output/home" -Dpolyglotimpl.AttachLibraryFailureAction=throw --enable-native-access=org.graalvm.truffle --sun-misc-unsafe-memory-access=allow     -cp "$test_output/classes" check.TruffleCheck
