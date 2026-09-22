#!/usr/bin/bash

set -euo pipefail

test_source=${1:-/tmp/Lsp4jRoundTrip.java}
test_classes=$(mktemp -d)
trap 'rm -rf "$test_classes"' EXIT

rpm -V lsp4j

classpath=$(
  {
    rpm -ql lsp4j
    rpm -ql google-gson
  } | grep -E '\.jar$' | sort -u | paste -sd: -
)

javac --release 11 -cp "$classpath" -d "$test_classes" "$test_source"
java -cp "$test_classes:$classpath" Lsp4jRoundTrip
java --module-path "$classpath" --validate-modules
