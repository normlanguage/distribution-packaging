# FastDoubleParser for Fedora

Build the [spec](fastdoubleparser.spec) with the archive recorded in [source.json](../source.json), the two patches and the regression test in this directory. Upstream Maven builds the Java 8 base and Java 11, 17, 21 and 23 variants into one multi-release JAR. Intermediate implementation artifacts are not installed.

The [UTF-8 patch](utf8-leading-format-characters.patch) routes byte slices containing non-ASCII data through the existing UTF-8 decoder and character parser. This preserves configured Unicode format handling at the beginning of a number and before an exponent sign. [Regression tests](LeadingFormatCharactersTest.java) cover both positions, slices, configured numeric values and malformed input. ASCII byte input to `ConfigurableDoubleParser` gains a validation scan before its existing optimized parser; performance has not been benchmarked.

The [numbering-system patch](explicit-arabic-numbering.patch) makes two Arabic-digit test fixtures select the Arabic numbering system explicitly. Their hardcoded Arabic digit assertions remain unchanged. The separate dynamic locale tests continue to exercise the JDK's default Arabic locale.

Demo modules, JMH benchmarks and publishing plugins are omitted. The unpublished development module, which targets an experimental Vector API, is not built as a separate artifact; its shared source and test files remain the inputs to all five release variants. The upstream functional test selection is retained, including its disabled long-running cases. Test JVMs use one fork with a 2 GB heap. The spec generates one API documentation set from the assembled public sources.

The [installed-package check](../tests/FastDoubleParserCheck.java) covers numeric boundaries, large integers and decimals, UTF-8 format characters, all double input forms and invalid input.

Fedora 44 and isolated Fedora Rawhide builds each pass all five release variant suites. Each suite reports 6,454 tests, zero failures/errors and 16 upstream skips; these are overlapping executions of shared tests, not 32,270 distinct tests. The installed Fedora 44 RPM passes the check under JDK 25 with the multi-release JAR selection capped at 8, 11, 17, 21 and 23. Execution on older JVMs has not been verified.

Fedora 44 rpmlint applied to both builds reports two errors: the redundant unversioned JPMS capability generated from `Automatic-Module-Name`, and an old FSF address in JDK-generated Javadoc. The automatic module name preserves the Java 9/10 module identity before the first explicit descriptor at Java 11. Two warnings cover documentation size and the absence of a separate `%check` section; functional tests run in Maven `%build`. No custom rpmlint filters suppress these results.

This package has not been submitted to Fedora review.
