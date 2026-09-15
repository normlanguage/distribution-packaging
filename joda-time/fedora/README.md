# Joda-Time for Fedora

Build the [spec](joda-time.spec) with the archive recorded in [source.json](../source.json). The [Joda-Convert package](../../joda-convert/fedora/) supplies the annotation dependency. Upstream Maven compiles the accompanying Global-TZ text data into the installed time zone database.

Fedora 44 and isolated Fedora Rawhide builds each report 4,235 tests with zero failures, errors or skips. The upstream suite contains 17 legacy SecurityManager cases that return early on modern JDKs; these do not validate SecurityManager behavior on JDK 25. The package retains the upstream test selection and assertions.

The [installed-package check](../tests/JodaTimeRoundTrip.java) validates a daylight-saving transition, date round trip, leap-year arithmetic and invalid-date rejection using the installed JAR.

Publishing plugins, historical API comparison and the duplicate artifact without time zone data are omitted. Fedora's standard Maven tooling generates the Javadoc package. Historical serialized test fixtures remain available to the upstream compatibility tests and are not installed as library payload.

Fedora 44 rpmlint applied to Rawhide artifacts reports an old FSF address in the JDK-generated Javadoc legal file, large documentation size and no separate `%check` section. Functional tests run during Maven `%build`.
