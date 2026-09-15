# Plexus Testing

[Upstream provenance](source.json) pins version 2.2.0. The [Fedora update](fedora/update-plexus-testing.patch) applies to the existing 1.3.0 source RPM identified in [source-rpm.json](fedora/source-rpm.json). The generated spec is not maintained separately.

Rawhide mock builds the source and binary RPMs and passes all four upstream tests with no skips. [Build evidence](evidence/build.log) and [installed packages](evidence/installed_pkgs.log) record the environment. The spec retains Fedora's explicit Plexus Utils/XML dependencies required by its Sisu runtime. No test sources are removed.

`rpmlint` reports no errors and two warnings: the inherited obsolete Javadoc package declaration and the absence of a separate `%check` section; Maven executes tests during `%build`. Integration with Maven Plugin Testing Harness remains a separate gate. This is a locally validated update, not an accepted Fedora package update.
