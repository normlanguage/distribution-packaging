# Kryo Fedora packaging

[kryo5.spec](kryo5.spec) builds the unshaded upstream Maven module against distribution MinLog, ReflectASM and Objenesis. The optional Kotlin test profile is disabled; the Java test suite remains enabled. XMvn Javadoc uses the upstream Java 8 source mode.

Fedora 44 validation: SRPM, library RPM and Javadoc RPM built; 304 Java tests passed with no failures, errors or skips. The installed-package round trip uses [the shared test](../debian/tests/KryoRoundTrip.java) with the installed Kryo and dependency jars.

Rawhide mock validation is pending. Rpmlint reports a generated JDK documentation license address finding, a documentation size warning, and a missing check section warning; Maven runs tests during the build section. These findings have not been filtered or treated as resolved.
