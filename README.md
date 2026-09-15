# Norm distribution packaging

Distribution-native packaging for dependencies required by [Norm](https://github.com/normlanguage/Norm). These recipes are maintained for review and integration into Debian and Fedora; this repository is not an official distribution repository.

| Component | Packaging | Upstream provenance |
| --- | --- | --- |
| Kryo 5 | [Debian](kryo/debian/), [Fedora](kryo/fedora/) | [Source](kryo/source.json), [repacked archive](kryo/repack.json) |
| ReflectASM | [Fedora](reflectasm/fedora/reflectasm.spec) | [Source](reflectasm/source.json), [patch notes](reflectasm/fedora/README.md) |
| MinLog | [Fedora](minlog/fedora/minlog.spec) | [Source](minlog/source.json) |

Debian source and binary artifacts are published as prerelease assets for review. The `.dsc` and its referenced archives are sufficient to extract the source with `dpkg-source -x`; use `sbuild` for an isolated build. Installed-package tests are defined in [debian/tests](kryo/debian/tests/).

For Fedora, fetch the archive recorded in the provenance file, place it and [MinlogCheck.java](minlog/fedora/MinlogCheck.java) in the RPM SOURCES directory, and build the [spec](minlog/fedora/minlog.spec). Validate the resulting SRPM with `mock`.

Norm's own compiler and release definitions remain in the [upstream repository](https://github.com/normlanguage/Norm). These recipes do not introduce a separate Norm compiler build.
