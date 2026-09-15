# Fedora Jackson module descriptors

These patches target the official Fedora source RPMs recorded in [sources.json](sources.json). They are proposed packaging corrections, not accepted Fedora updates or a parallel implementation of Jackson. Apply each patch to its corresponding spec after extracting the verified source RPM, then generate an SRPM with `rpmbuild -bs` and build it with Rawhide `mock`.

The official Core, Databind and Annotations specs remove the Moditect plugin. Consequently their JARs lack the upstream JPMS descriptors. An application requiring `com.fasterxml.jackson.core`, or YAML requiring the Jackson modules transitively, cannot resolve the official artifacts by those names.

Each patch adds the Moditect build dependency and retains the upstream plugin. It also increments the RPM release. No runtime sources, descriptors, Maven coordinates or module names are rewritten. Existing Fedora source patches and build policies remain intact.

## Validation

All three modified source RPMs build in isolated Rawhide. Annotations runs 62 tests with zero failures/errors/skips. The official Core and Databind specs skip their upstream test suites; these patches do not change that policy, and their builds must not be described as full upstream test passes.

Compared with the original official binary RPMs, all 1,059 existing runtime class entries are byte-identical. Each corrected JAR adds only its upstream module descriptor among class entries. [Observed class comparison](evidence/runtime-class-comparison.json) records the exact paths and counts. Other archive metadata is not covered by this class comparison.

The shared [YAML installed check](../jackson-dataformats-text/tests/JacksonYamlCheck.java) passes on both the class path and [module path](../jackson-dataformats-text/tests/module-info.java) with these three corrected RPMs, Jackson YAML 2.21.5 and final normal-mode SnakeYAML 2.5. It previously failed against the official RPMs; restoring only Core and Databind still fails because Annotations also lacks its descriptor. This proves this dependency chain's module integration, not the full Norm compiler or every Jackson consumer.

Fedora 44 rpmlint on the final Rawhide artifacts reports one error for an old FSF address in JDK-generated Javadoc, plus eight warnings covering existing spec metadata, documentation size and missing separate `%check` sections. No custom lint filters are used.

The corrections require Fedora maintainer review before official repository users can rely on them.
