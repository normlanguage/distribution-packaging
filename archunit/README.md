# ArchUnit Fedora packaging

The [RPM candidate](archunit.spec) builds ArchUnit 1.5.0 core from the pinned upstream source using Fedora's ASM, Guava and SLF4J packages. It preserves the upstream automatic module name while keeping those libraries independently updatable.

[build.sh](build.sh) compiles the Java 8 core and Java 9 runtime additions. [ArchUnitCheck.java](ArchUnitCheck.java) imports a compiled class and evaluates an architecture rule. [validate-installed.sh](validate-installed.sh) repeats that check against installed RPM contents.

[source.json](source.json) records the immutable release source and digest. The JUnit integration modules are outside Norm's dependency graph and are not included.

The candidate passes a clean Fedora Rawhide mock build, `rpmlint` with zero errors, RPM verification, automatic-module validation and the installed-package architecture rule. Adding it to the local dependency repository completes all 27 direct Norm coordinates in the Fedora closure check. The corresponding logs are in [evidence](evidence).
