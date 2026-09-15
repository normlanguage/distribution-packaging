# Gradle source-build prerequisites

This is a prerequisite investigation, not a completed Gradle RPM or Debian source package. The source archive is pinned in [source.json](source.json).

The upstream [wrapper](https://github.com/gradle/gradle/blob/92f0512e7f06d84621afba191f75e265363890cf/gradle/wrapper/gradle-wrapper.properties) requests Gradle 9.7.0 to build 9.7.1. The [distribution catalog](https://github.com/gradle/gradle/blob/92f0512e7f06d84621afba191f75e265363890cf/gradle/dependency-management/distribution.versions.toml) declares Kotlin 2.4.0. The [settings build](https://github.com/gradle/gradle/blob/92f0512e7f06d84621afba191f75e265363890cf/build-logic-settings/settings.gradle.kts) resolves plugins from external Maven repositories.

A Fedora 44 diagnostic used the already downloaded upstream Gradle 9.7.1 binary, system JDK 25, a separate empty Gradle user home, `help --offline --no-daemon --max-workers=2`, and disabled JDK auto-download. Configuration failed at the Kotlin DSL 6.7.3 plugin marker before compilation. The [log](evidence/offline-configuration.log) records the failure. This probe is not a source-built bootstrap, does not use a distribution Maven repository adapter, and does not demonstrate that every later dependency is unavailable.

Targeted [Rawhide capability queries](evidence/rawhide-providers.json) independently found no Gradle, Kotlin, Kotlin compiler/Gradle plugin, or Kotlin DSL marker/implementation provider in the checked repository. These are capability checks, not an audit of every possible alternative packaging project.

A distribution build needs a reproducible Gradle/Kotlin bootstrap and its build-plugin closure. Norm's existing Gradle build remains the single compiler build definition; a second handwritten compiler build would not resolve this prerequisite correctly. Other independent runtime dependency work can proceed while the build-tool supply is unresolved.
