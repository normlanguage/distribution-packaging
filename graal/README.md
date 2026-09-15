# GraalVM SDK and Truffle source builds

The GraalVM 25.1.3 and mx 7.83.0 source inputs are pinned in [source.json](source.json). This is source-build preparation; no GraalVM SDK or Truffle RPM/SRPM has been produced.

## SDK

Fedora 44 builds `COLLECTIONS`, `WORD`, `NATIVEIMAGE`, `JNIUTILS` and `POLYGLOT` through the upstream mx SDK suite using system OpenJDK 25 and its separate JMOD package. The build runs in a network namespace without network access, uses a separate mx dependency cache, and selects javac with `--force-javac --no-daemon --serial`. mx generates the module descriptors and version resource from upstream definitions; no second handwritten compilation pipeline is used.

The five resulting JARs pass `java --validate-modules` together, and the Polyglot version resource is 25.1.3. [Build evidence](evidence/sdk-build.json) records arguments, toolchain, scope and artifact hashes. Upstream unit tests, RPM installation and full Norm integration have not been run for these artifacts.

## Truffle

The same network-isolated build of `TRUFFLE_DSL_PROCESSOR`, `TRUFFLE_API`, `TRUFFLE_COMPILER` and `TRUFFLE_RUNTIME` stops at the requested ANTLR 4.13.2 runtime download. Fedora 44 provides `antlr4-runtime-4.13.2-18.fc44`; its installed JAR exposes the expected automatic module name `org.antlr.antlr4.runtime`.

The next integration step is to use the system ANTLR artifact through the upstream mx dependency model, preserve its actual content identity, and ensure the processor package does not bundle ANTLR classes. Later dependencies are not yet validated. mx packaging, SDK unit tests and distribution-native package generation also remain required.
