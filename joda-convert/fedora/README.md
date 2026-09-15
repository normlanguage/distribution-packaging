# Joda-Convert for Fedora

Use the [spec](joda-convert.spec) and archive recorded in [source.json](../source.json). Build ThreeTen Backport first; [its recipe](../../threetenbp/fedora/) supplies the optional integration dependency used by the upstream build and tests.

The package preserves the upstream Java module and both optional integrations. Maven runs three upstream test configurations: default (198 tests), without Guava (180), and without ThreeTen (196). These overlap and are not 574 distinct tests. Fedora 44 and a Rawhide mock chain build passed all three configurations with zero failures, errors or skips.

The upstream `no-threetenbp` configuration specifies the wrong Maven group ID. The spec corrects it to the actual `org.threeten:threetenbp` coordinate. Publishing, website, style and coverage plugins are removed; Fedora's standard Maven Javadoc generation supplies the documentation package.

The [installed-package check](../tests/JodaConvertRoundTrip.java) verifies standard and annotation-based conversion while explicitly checking that both optional libraries are absent from the runtime classpath.

Fedora 44 rpmlint applied to the Rawhide artifacts reports the JDK-generated Javadoc legal file's old FSF address, large documentation size and no separate `%check` section. Upstream tests run during Maven `%build`.
