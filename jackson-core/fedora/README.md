# Jackson Core for Fedora

This is a Fedora 44 backport recipe for Norm's pinned Jackson Core version. The verified Rawhide environment already provides Jackson Core 2.21.5; that official package is the first candidate for Norm's distribution build. This recipe is not a proposed Rawhide downgrade.

Build the [spec](jackson-core.spec) with the archive recorded in [source.json](../source.json), the [module patch](system-fastdoubleparser-module.patch), [Jackson build parents](../../jackson-bom/fedora/) and [FastDoubleParser](../../fastdoubleparser/fedora/). Upstream Maven generates the version class, runs tests and builds the module descriptor with Fedora's Replacer and Moditect plugins.

FastDoubleParser remains an external Maven dependency. The patch adds its JPMS requirement; the spec retains its OSGi import and omits shading. Coverage, SBOM, Gradle publication metadata, website generation and Android signature checks are omitted. The Java functional tests are retained.

Fedora 44 and isolated Rawhide builds each report 1,475 tests, zero failures/errors and two upstream skips: the exhaustive integer-division check and the near-2-GB string test. Rawhide resolves its official OSS Parent 75, Jackson Parent 2.21 and BOM 2.21.5 together with the locally built FastDoubleParser 2.0.1.

The installed Fedora 44 RPM passes [round-trip and service-discovery checks](../tests/JacksonCoreCheck.java) on both the class path and the [module path](../tests/module-info.java) under JDK 25. The [artifact inspection](../tests/inspect-jar.py) verifies Java 8 base bytecode, the Java 9 descriptor, external dependency declarations, service metadata and the absence of bundled FastDoubleParser classes or nested JARs. Older JVM execution and OSGi runtime integration have not been tested.

Fedora 44 rpmlint applied to the Rawhide artifacts reports an old FSF address in JDK-generated Javadoc and warnings for documentation size and the lack of a separate `%check` section. Tests execute during Maven `%build`.
