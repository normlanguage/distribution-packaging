# JSpecify Fedora packaging

[The spec](jspecify.spec) adapts upstream's annotation artifact build to system JDK, Bnd and Fedora Java packaging tools. The build contracts are [the upstream root build](https://github.com/jspecify/jspecify/blob/b2a10e14bb81c1b7cb6e488c112fe55cb2218d7d/build.gradle), [multi-release layout](https://github.com/jspecify/jspecify/blob/b2a10e14bb81c1b7cb6e488c112fe55cb2218d7d/gradle/mrjar.gradle) and Bnd metadata. The complete upstream Gradle workflow, Error Prone checks and website build are not claimed.

Base classes target Java 8; the module descriptor targets Java 9 and occupies the multi-release location. Tests execute against the built JAR through the distribution JUnit Platform Launcher API. The [launcher](JSpecifyIntegrationRunner.java) explicitly selects upstream's static nested test classes and fails when no test succeeds or any test/container fails.

Fedora 44 RPM build and installed JPMS loading passed. On JDK 25, the Java 9+ test passed and the Java 8 test was aborted by its upstream assumption; Java 8 runtime behavior remains unverified. A no-tests invocation correctly failed. Rawhide x86_64 (fc46) mock validation passed with the same test outcomes.

Rpmlint retains the generated JDK documentation license address finding and documentation size warning.
