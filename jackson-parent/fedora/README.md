# Jackson Parent for Fedora

Build the [spec](jackson-parent.spec) with the archive recorded in [source.json](../source.json) and [FasterXML OSS Parent](../../fasterxml-oss-parent/fedora/). The package preserves the upstream Jackson build configuration and requires OSS Parent 70 or newer. Upstream declares Apache-2.0 in the POM but does not include a separate license file in this source archive.

Fedora 44 and isolated Fedora Rawhide builds succeed using system Maven in offline mode. These projects contain Maven configuration rather than Java implementation code and have no Java test suite. Fedora 44 rpmlint applied to the Rawhide artifacts reports zero errors and one warning for the absence of a separate `%check` section. The packages have not been submitted for Fedora review.
