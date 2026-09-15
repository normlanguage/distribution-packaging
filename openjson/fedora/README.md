# OpenJSON Fedora packaging

[The spec](openjson.spec) uses system Maven, JUnit and the bundle plugin. Source and target settings are replaced with Java release 8 for the distribution JDK. Coverage and publishing plugins are omitted; all upstream unit tests remain enabled.

Fedora 44 builds passed all 226 tests without failures, errors or skips. [The installed-library check](../tests/OpenjsonRoundTrip.java) passed on both the Fedora RPM and Debian's existing libopenjson-java 1.0.13-1 package. Rawhide x86_64 (fc46) mock validation passed with the same 226 successful tests.

Rpmlint reports the generated JDK documentation license address, documentation size and missing separate check-section findings. Maven executes tests during the build lifecycle.
