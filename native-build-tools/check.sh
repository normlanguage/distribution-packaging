#!/usr/bin/bash

set -euo pipefail

source_root=$1
build_root=$2
openjson_jar=$3
test_classpath=$4

source_root=$(realpath "$source_root")
build_root=$(realpath "$build_root")

test_root="$build_root/test"
rm -rf "$test_root"
mkdir -p "$test_root/classes"

find \
  "$source_root/common/utils/src/test/java" \
  "$source_root/common/graalvm-reachability-metadata/src/test/java" \
  -name '*.java' -print | sort > "$test_root/sources"

classpath="$build_root/utils.jar:$build_root/graalvm-reachability-metadata.jar:$openjson_jar:$test_classpath"
javac \
  --release 17 \
  --add-modules jdk.httpserver \
  -cp "$classpath" \
  -d "$test_root/classes" \
  @"$test_root/sources"

cp -a "$source_root/common/utils/src/test/resources/." "$test_root/classes/"
cp -a "$source_root/common/graalvm-reachability-metadata/src/test/resources/." "$test_root/classes/"

(
  cd "$source_root/common/utils"
  java \
    --add-modules jdk.httpserver \
    -cp "$test_root/classes:$classpath" \
    org.junit.platform.console.ConsoleLauncher execute \
    --scan-class-path "$test_root/classes" \
    --exclude-engine junit-vintage \
    --fail-if-no-tests
)

java --module-path "$build_root/utils.jar:$build_root/graalvm-reachability-metadata.jar:$openjson_jar" --validate-modules
