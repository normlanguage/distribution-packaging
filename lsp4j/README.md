# LSP4J Fedora packaging

The [RPM candidate](lsp4j.spec) builds LSP4J 1.0.0 and its JSON-RPC module from the official Maven Central source release using system Java and Gson. The source release retains the original Xtend inputs and contains the generated Java sources published for consumers. No compiled upstream classes enter the build.

The [build entry point](build-source-release.sh) compiles 507 Java sources for Java 11 and assigns the stable upstream module names. [Lsp4jRoundTrip.java](Lsp4jRoundTrip.java) exercises two connected launchers with a Unicode request and response. [validate-installed.sh](validate-installed.sh) verifies the installed RPM without using the build tree.

The candidate passes a clean Fedora Rawhide mock build, RPM verification, Java module validation and the installed-package Unicode JSON-RPC round trip. The corresponding logs are stored in [evidence](evidence).

[source.json](source.json) identifies the Git source and inspected build definitions. [archive.json](archive.json) records the corresponding complete Git archive. The Git build requires Gradle, Xtext, Xtend and Bnd plugins that are unavailable in Fedora; the source-release path avoids that build-tool bootstrap while preserving the generated and generator source inputs.
