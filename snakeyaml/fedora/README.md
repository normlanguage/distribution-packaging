# SnakeYAML for Fedora

The [spec](snakeyaml.spec) uses the upstream archive recorded in [source.json](../source.json). Bootstrap artifacts are only intermediate build dependencies; the final package uses normal mode with Jackson YAML available.

## Test fixtures

The [fixture patch](plain-java-test-fixtures.patch) expands the two upstream Lombok-annotated test files into ordinary Java using the original Lombok 1.18.30 version. [Generator provenance](fixture-generator.json) records the preparation tool; this tool is not an RPM build input or shipped payload. Upstream license headers, test methods and assertions are retained. Generated builder return-value documentation is omitted.

Using OpenJDK 21, original annotation-processed fixtures and expanded fixtures have matching method disassembly after ignoring constant-pool numbering and declaration order. This comparison covers seven compiled classes, including both unchanged regression tests. Both versions pass EnvLombokTest and YamlExecuteProcessContextTest. These fixtures compile without Lombok in the Fedora build.

## Build modes

`rpmbuild --with bootstrap` temporarily omits only issue1100/JacksonTest.java and its Jackson YAML dependency to break the build cycle. Normal builds retain both. The upstream JMH performance benchmarks are not packaged; upstream functional tests remain selected. StressTest and ParallelTest remain excluded as specified by the upstream POM.

Only issue318/classpath.properties receives Maven property filtering. All other test resources are copied byte-for-byte, preserving deliberately malformed encoding samples used by the fuzzer regressions.

Fedora 44 and isolated Rawhide bootstrap builds of 2.5 each report 1,173 tests with zero failures/errors and four skips. The isolated Rawhide normal build reports 1,174 tests with zero failures/errors and four skips, including the restored Jackson regression against Jackson YAML 2.21.5. The skips are upstream: the Java 6-only stack overflow test, two Java Optional reflection tests and the ignored map-comments test. All 237 runtime class entries, including the module descriptor, are byte-identical between the Rawhide bootstrap and normal RPMs. Normal-mode Fedora 44 execution has not been tested.

Fedora 44 rpmlint applied to the Rawhide artifacts reports two spelling findings for the upstream term representers, an old FSF address in JDK-generated Javadoc, and warnings for documentation size and the absence of a separate `%check` section. Tests run during Maven `%build`.

The combined installed-package validation and module-path limitation are documented with [Jackson YAML](../../jackson-dataformats-text/fedora/).
