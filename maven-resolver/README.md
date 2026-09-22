# Maven Resolver Fedora packaging

The [RPM candidate](maven-resolver.spec) updates Fedora's Maven Resolver package to 2.0.21 and retains the distribution package's XMvn, Maven-coordinate alias and OSGi manifest structure. The selected reactor contains the core API and implementation, basic connector, file and Apache transports, named locks, utilities and Maven 3 supplier used by Norm.

[source.json](source.json) pins the upstream release tag and immutable Git archive. Modules for alternate transports, Maven 4, demos and tools are outside Norm's dependency graph and are excluded from the candidate.

The candidate builds successfully in a clean Fedora Rawhide mock. The build runs the selected modules' upstream test suites. A fresh mock installation passes RPM verification, resolves the Maven 3 supplier through XMvn, validates all nine automatic module names used by Norm and resolves a fixture artifact from a local file repository through `RepositorySystemSupplier` and `SessionBuilderSupplier`. A second clean Rawhide mock installs the candidate alongside Fedora's `maven-lib` and repeats the installed-package resolution check, covering the Maven provider combination used by Norm. The corresponding logs are in [evidence](evidence).
