# Jackson YAML for Fedora

The [spec](jackson-dataformat-yaml.spec) builds the YAML module and text-format parent POM from the upstream archive in [source.json](../source.json). It uses Rawhide's official Jackson 2.21.5 Core/Databind and 2.21 Annotations packages, together with [SnakeYAML 2.5](../../snakeyaml/fedora/). CSV, properties and TOML are separate upstream modules and are not selected. CycloneDX and Gradle publication metadata generation are omitted; Maven's version generation, module descriptor, functional tests and Javadoc are retained.

## Build cycle

Build SnakeYAML with `--with bootstrap`, then this package, then SnakeYAML again without bootstrap. The final SnakeYAML build retains its Jackson integration test. The bootstrap package is not a final distribution artifact.

## Validation

The isolated Rawhide build reports 167 tests, zero failures/errors and zero skips. Installed RPMs pass the [classpath check](../tests/JacksonYamlCheck.java) with the final normal-mode SnakeYAML RPM and official Jackson dependencies under JDK 25. It covers Unicode record serialization, strict duplicate detection, malformed input, anchor/alias and explicit-tag metadata, document boundaries, service discovery and generated version metadata. This is dependency-level validation; Norm's full compiler has not been validated against these system packages.

The [module-path check](../tests/module-info.java) currently fails: official Rawhide Core and Databind JARs expose filename-derived automatic names `jackson.core` and `jackson.databind`, whereas YAML's retained upstream descriptor requires `com.fasterxml.jackson.core` and `com.fasterxml.jackson.databind`. Changing the test's direct requirements alone would not fix YAML's descriptor. No aliases, rewritten upstream names or removed descriptors conceal this mismatch. Distribution module integration remains required before claiming Norm's module-path build works.

Fedora 44 rpmlint applied to the Rawhide artifacts reports an old FSF address in JDK-generated Javadoc and warnings for documentation size and the absence of a separate `%check` section. Tests execute during Maven `%build`.
