#!/usr/bin/bash
set -euo pipefail

test_source=${1:-/tmp/ArchUnitCheck.java}
test_classes=$(mktemp -d)
trap 'rm -rf "$test_classes"' EXIT

rpm -V archunit
classpath=/usr/share/java/archunit/archunit.jar
classpath+=:/usr/share/java/objectweb-asm/asm.jar
classpath+=:/usr/share/java/guava/guava.jar
classpath+=:/usr/share/java/guava/failureaccess.jar
classpath+=:/usr/share/java/slf4j/slf4j-api.jar
classpath+=:/usr/share/java/slf4j/slf4j-nop.jar
javac --release 17 -cp "$classpath" -d "$test_classes" "$test_source"
java -cp "$test_classes:$classpath" ArchUnitCheck
jar --describe-module --file /usr/share/java/archunit/archunit.jar | grep '^com.tngtech.archunit automatic$'
