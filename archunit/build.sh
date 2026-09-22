#!/usr/bin/bash
set -euo pipefail

source_root=$(realpath "$1")
output=$(realpath -m "$2")
classpath=$3

rm -rf "$output"
mkdir -p "$output/classes"

find "$source_root/archunit/src/main/java" -name '*.java' -print | LC_ALL=C sort > "$output/main-sources"
javac --release 8 -proc:none -encoding UTF-8 -cp "$classpath" -d "$output/classes" @"$output/main-sources"

find "$source_root/archunit/src/jdk9main/java" -name '*.java' -print | LC_ALL=C sort > "$output/jdk9-sources"
javac --release 9 -proc:none -encoding UTF-8 -cp "$output/classes:$classpath" -d "$output/classes" @"$output/jdk9-sources"

if [[ -d "$source_root/archunit/src/main/resources" ]]; then
  cp -a "$source_root/archunit/src/main/resources/." "$output/classes/"
fi

printf 'Manifest-Version: 1.0\nAutomatic-Module-Name: com.tngtech.archunit\n\n' > "$output/manifest.mf"
jar --create --file "$output/archunit.jar" --manifest "$output/manifest.mf" -C "$output/classes" .
