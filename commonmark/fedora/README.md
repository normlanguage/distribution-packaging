# CommonMark Fedora packaging

[The spec](commonmark-java.spec) builds the upstream core, extension and integration-test modules with distribution Maven dependencies. Only the two JMH performance benchmark sources are excluded. Test utilities and integration-test artifacts are not installed.

The system Javadoc tool generates API documentation for the published modules. Library module descriptors remain intact. [The installed-package test](../tests/CommonmarkRoundTrip.java) exercises Markdown parsing and HTML output.

Fedora 44 builds and installed-package validation passed. Maven reported 4,531 tests with zero failures, zero errors and one upstream-disabled usage example. Rawhide x86_64 (fc46) mock validation passed with the same test totals. Rpmlint reports the generated JDK license address, documentation size and missing separate check-section findings; tests run during Maven's build lifecycle.
