# Norm distribution packaging

Distribution-native packaging for dependencies required by [Norm](https://github.com/normlanguage/Norm). These recipes are maintained for review and integration into Debian and Fedora; this repository is not an official distribution repository.

| Component | Packaging | Upstream provenance |
| --- | --- | --- |
| SnakeYAML | [Fedora](snakeyaml/fedora/) | [Source](snakeyaml/source.json) |
| Jackson YAML | [Fedora](jackson-dataformats-text/fedora/) | [Source](jackson-dataformats-text/source.json) |
| Jackson Core | [Fedora 44 backport](jackson-core/fedora/) | [Source](jackson-core/source.json) |
| FasterXML OSS Parent | [Fedora](fasterxml-oss-parent/fedora/) | [Source](fasterxml-oss-parent/source.json) |
| Jackson Parent | [Fedora](jackson-parent/fedora/) | [Source](jackson-parent/source.json) |
| Jackson BOM and Base | [Fedora](jackson-bom/fedora/) | [Source](jackson-bom/source.json) |
| FastDoubleParser | [Fedora](fastdoubleparser/fedora/) | [Source](fastdoubleparser/source.json) |
| Joda-Time | [Fedora](joda-time/fedora/) | [Source](joda-time/source.json) |
| Joda-Convert | [Fedora](joda-convert/fedora/) | [Source](joda-convert/source.json) |
| ThreeTen Backport | [Fedora](threetenbp/fedora/) | [Source](threetenbp/source.json) |
| JSpecify | [Fedora](jspecify/fedora/) | [Source](jspecify/source.json) |
| OpenJSON | [Fedora](openjson/fedora/) | [Source](openjson/source.json) |
| CommonMark | [Fedora](commonmark/fedora/) | [Source](commonmark/source.json) |
| Kryo 5 | [Debian](kryo/debian/), [Fedora](kryo/fedora/) | [Source](kryo/source.json), [repacked archive](kryo/repack.json) |
| ReflectASM | [Fedora](reflectasm/fedora/reflectasm.spec) | [Source](reflectasm/source.json), [patch notes](reflectasm/fedora/README.md) |
| MinLog | [Fedora](minlog/fedora/minlog.spec) | [Source](minlog/source.json) |
| LSP4J | [Fedora](lsp4j/) | [Source](lsp4j/source.json) |
| GraalVM Native Build Tools | [Fedora](native-build-tools/) | [Source](native-build-tools/source.json) |
| Maven Resolver 2 | [Fedora](maven-resolver/) | [Source](maven-resolver/source.json) |

Debian source and binary artifacts are published as prerelease assets for review. The `.dsc` and its referenced archives are sufficient to extract the source with `dpkg-source -x`; use `sbuild` for an isolated build. Installed-package tests are defined in [debian/tests](kryo/debian/tests/).

[Corrections to official Fedora Jackson module metadata](fedora-jackson-modules/) are maintained as patches against identified source RPMs.

For Fedora, each component directory identifies its spec, source provenance, additional source inputs and validation scope. Build the spec with RPM tooling and validate the resulting SRPM with `mock`.

Norm's own compiler and release definitions remain in the [upstream repository](https://github.com/normlanguage/Norm). These recipes do not introduce a separate Norm compiler build.

Build-tool prerequisites are tracked separately in the [Gradle source-build investigation](gradle/).

The [GraalVM SDK/Truffle candidate](graal/) records the source build, installed-package checks and runtime toolchain validation.

[Plexus Testing](plexus-testing/) maintains a source update for the Maven plugin test framework.
