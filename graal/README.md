# GraalVM SDK and Truffle source builds

The GraalVM 25.1.3 and mx 7.83.0 source inputs are pinned in [source.json](source.json). This is source-build preparation; no GraalVM SDK or Truffle RPM/SRPM has been produced.

## SDK

Fedora 44 builds `COLLECTIONS`, `WORD`, `NATIVEIMAGE`, `JNIUTILS` and `POLYGLOT` through the upstream mx SDK suite using system OpenJDK 25 and its separate JMOD package. The build runs in a network namespace without network access, uses a separate mx dependency cache, and selects javac with `--force-javac --no-daemon --serial`. mx generates the module descriptors and version resource from upstream definitions; no second handwritten compilation pipeline is used.

The five resulting JARs pass `java --validate-modules` together, and the Polyglot version resource is 25.1.3. [Build evidence](evidence/sdk-build.json) records arguments, toolchain, scope and artifact hashes. Upstream unit tests, RPM installation and full Norm integration have not been run for these artifacts.

## Truffle

The network-isolated build of `TRUFFLE_DSL_PROCESSOR`, `TRUFFLE_API`, `TRUFFLE_COMPILER` and `TRUFFLE_RUNTIME` succeeds from freshly extracted source with system ANTLR and ASM. The [source patch](fedora/unbundle-truffle-libraries.patch) removes embedded dependency classes. [System bindings](fedora/system-libraries.json) are applied to both mx and Truffle by [bind-system-libraries.py](fedora/bind-system-libraries.py), which obtains module names from the JDK and computes digests from installed JARs.

The [functional check](tests/run-check.sh) verifies DSL annotation processing, a Truffle call target and an ASM-generated host adapter. It requires native attachment failures to throw. [Artifact inspection](evidence/truffle-artifacts.json) records hashes, module descriptors and native resources; none of the ten inspected JARs contains ANTLR or ASM classes. `truffle-api.jar` includes the source-built Linux amd64 attachment library and needs architecture-aware packaging.

Evidence: [fresh build](evidence/graal-truffle-candidate-build.log), [functional check](evidence/graal-candidate-functional-check.log), [explicit JVMCI/compiler diagnostic](evidence/graal-candidate-jvmci-check.log). The default JVM uses interpreter fallback. Explicitly enabling JVMCI and resolving the system `jdk.graal.compiler` module fails because that module lacks the Truffle compiler package. Optimizing compilation remains unverified; these checks do not establish upstream unit-test coverage or full Norm compatibility.

mx packaging, upstream tests, a compatible optimizing compiler and distribution-native package generation remain required.

## Optimizing compiler

The upstream compiler suite's `GRAAL` target builds its processor and options module with the same offline mx command, then fails because system OpenJDK 25 does not provide `jdk.vm.ci.meta.annotation`. [Compiler build evidence](evidence/graal-compiler-source-build.log) records the failure. The pinned compiler source uses this package in its annotation support, snippet metadata and replay proxies; its `JVMCIVersionCheck.java` specifies Labs JDK 25.0.3+9, release 25.1, JVMCI build 19 as the minimum for JDK 25. Removing a suite export would not supply the missing API. A distribution-supported JVMCI implementation compatible with this compiler remains unresolved.
