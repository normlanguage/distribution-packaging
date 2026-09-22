# GraalVM Native Build Tools Fedora packaging

The [RPM candidate](graalvm-native-build-tools.spec) builds the `utils` and `graalvm-reachability-metadata` modules from the pinned Native Build Tools 1.1.12 source. These are the modules used directly by Norm's compiler build.

The [build entry point](build.sh) compiles the two Java 17 modules against Fedora's OpenJSON package and generates the upstream build-time `VersionInfo` class. The [test entry point](check.sh) runs the two modules' complete upstream unit-test set and validates the resulting Java modules. [InstalledCheck.java](InstalledCheck.java) and [validate-installed.sh](validate-installed.sh) exercise the installed reachability metadata API independently of the build tree.

[source.json](source.json) records the release tag, immutable commit, archive digest and upstream repository. The remaining Gradle and Maven plugins are outside Norm's runtime dependency graph and are not included in this package.

[relax-backoff-timing-test.patch](relax-backoff-timing-test.patch) retains the upstream timing assertion while allowing for shared-builder scheduling latency. The one-second limit remains below the approximately 3.75-second default retry duration that the test distinguishes from the configured 31-millisecond duration.

The candidate passes a clean Fedora Rawhide mock build with all 90 upstream tests, RPM verification, Java module validation and an installed-package metadata copy. `rpmlint` reports zero errors and one missing-documentation warning. The corresponding logs are stored in [evidence](evidence).
