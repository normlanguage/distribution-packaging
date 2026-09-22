#!/usr/bin/bash

set -euo pipefail

source_root=$1
build_root=$2
openjson_jar=$3
version=$4
metadata_version=$5

source_root=$(realpath "$source_root")
mkdir -p "$build_root"
build_root=$(realpath "$build_root")

utils_root="$source_root/common/utils"
reachability_root="$source_root/common/graalvm-reachability-metadata"

rm -rf "$build_root"
mkdir -p \
  "$build_root/generated/org/graalvm/buildtools" \
  "$build_root/utils-classes" \
  "$build_root/reachability-classes"

cat > "$build_root/generated/org/graalvm/buildtools/VersionInfo.java" <<EOF
package org.graalvm.buildtools;

public final class VersionInfo {
  public static final String JUNIT_PLATFORM_NATIVE_VERSION = "$version";
  public static final String METADATA_REPO_VERSION = "$metadata_version";
  public static final String NBT_VERSION = "$version";

  private VersionInfo() {}
}
EOF

find "$utils_root/src/main/java" -name '*.java' -print | sort > "$build_root/utils-sources"
javac \
  --release 17 \
  -cp "$openjson_jar" \
  -d "$build_root/utils-classes" \
  @"$build_root/utils-sources" \
  "$build_root/generated/org/graalvm/buildtools/VersionInfo.java"
cp -a "$utils_root/src/main/resources/." "$build_root/utils-classes/"

cat > "$build_root/utils.mf" <<'EOF'
Manifest-Version: 1.0
Automatic-Module-Name: org.graalvm.buildtools.utils
EOF
jar --create --file "$build_root/utils.jar" --manifest "$build_root/utils.mf" -C "$build_root/utils-classes" .

find "$reachability_root/src/main/java" -name '*.java' -print | sort > "$build_root/reachability-sources"
javac \
  --release 17 \
  -cp "$openjson_jar:$build_root/utils.jar" \
  -d "$build_root/reachability-classes" \
  @"$build_root/reachability-sources"

cat > "$build_root/reachability.mf" <<'EOF'
Manifest-Version: 1.0
Automatic-Module-Name: org.graalvm.reachability
EOF
jar --create --file "$build_root/graalvm-reachability-metadata.jar" --manifest "$build_root/reachability.mf" -C "$build_root/reachability-classes" .
