# ReflectASM packaging

The spec removes ASM shading and depends on the distribution ASM library. The generated Java module remains `com.esotericsoftware.reflectasm`.

The bytecode-version and Java 17 test patches come from Debian’s 1.11.9+dfsg-4 source package and identify their upstream commits in their headers. The Java 17 patch returns early from three protected/package-private constructor test methods on modern JDKs, matching upstream’s documented access limitations; a reported zero-skips count must not be interpreted as coverage of those cases.

The classloader-test patch retains garbage-collection verification using weak references to the two classloaders owned by the test. It avoids relying on a global classloader count that includes objects from unrelated tests.
