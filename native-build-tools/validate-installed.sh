#!/usr/bin/bash

set -euo pipefail

test_source=${1:-/tmp/InstalledCheck.java}
test_classes=$(mktemp -d)
trap 'rm -rf "$test_classes"' EXIT

rpm -V graalvm-native-build-tools

classpath=$(
  {
    rpm -ql graalvm-native-build-tools
    rpm -ql openjson
  } | grep -E '\.jar$' | sort -u | paste -sd: -
)

javac --release 17 -cp "$classpath" -d "$test_classes" "$test_source"
java -cp "$test_classes:$classpath" InstalledCheck
java --module-path "$classpath" --validate-modules
