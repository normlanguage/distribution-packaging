# Jackson BOM and Base for Fedora

Build the [spec](jackson-bom.spec) with the archive recorded in [source.json](../source.json) and [Jackson Parent](../../jackson-parent/fedora/). This package installs both `jackson-bom` and `jackson-base`. The imported JUnit BOM is declared as a build and installed-POM dependency so that offline Maven can resolve the complete model. Central publishing is omitted; dependency management and build configuration are retained.

Fedora 44 and isolated Fedora Rawhide builds succeed using system Maven in offline mode. These projects contain Maven configuration rather than Java implementation code and have no Java test suite. Fedora 44 rpmlint applied to the Rawhide artifacts reports zero errors and one warning for the absence of a separate `%check` section. The packages have not been submitted for Fedora review.
