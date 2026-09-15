# FasterXML OSS Parent for Fedora

This is a Fedora 44 backport recipe. The verified Rawhide environment already provides version 75; use that official package when building there.

Build the [spec](fasterxml-oss-parent.spec) with the archive recorded in [source.json](../source.json). The installed POM retains compiler, bundle, generated-source and test configuration. Website, source-control publication, coverage and Central publishing plugins/extensions are omitted.

Fedora 44 and isolated Fedora Rawhide builds succeed using system Maven in offline mode. These projects contain Maven configuration rather than Java implementation code and have no Java test suite. Fedora 44 rpmlint applied to the Rawhide artifacts reports zero errors and one warning for the absence of a separate `%check` section. This backport has not been submitted to Fedora; Rawhide does not need a downgrade to this version.
