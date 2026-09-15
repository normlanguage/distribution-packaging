%global commit b2a10e14bb81c1b7cb6e488c112fe55cb2218d7d

Name: jspecify
Version: 1.0.0
Release: 1%{?dist}
Summary: Annotations for Java null analysis
License: Apache-2.0
URL: https://github.com/jspecify/jspecify
Source0: https://github.com/jspecify/jspecify/archive/%{commit}/jspecify-%{version}.tar.gz
Source1: JSpecifyIntegrationRunner.java
BuildArch: noarch
BuildRequires: maven-local-openjdk25
BuildRequires: aqute-bnd
BuildRequires: junit5
BuildRequires: opentest4j

%description
JSpecify supplies annotations for static analysis of null references and
interoperability between JVM languages.

%package javadoc
Summary: API documentation for JSpecify

%description javadoc
API documentation for JSpecify.

%prep
%autosetup -n jspecify-%{commit}
find . -type f -name '*.jar' -delete
printf '\nImplementation-Version: %{version}\nMulti-Release: true\n' >> bnd.bnd

%build
mkdir -p target/classes target/java9 target/test-classes
find src/main/java -name '*.java' | sort > target/main-sources
javac -encoding UTF-8 -source 8 -target 8 -d target/classes @target/main-sources
javac -encoding UTF-8 --release 9 -d target/java9 @target/main-sources src/java9/java/module-info.java
jar --create --file target/unbundled.jar -C target/classes .
bnd wrap --properties bnd.bnd --version %{version} --output target/jspecify.jar target/unbundled.jar
jar --update --file target/jspecify.jar --release 9 -C target/java9 module-info.class
javadoc -quiet -Xdoclint:none -encoding UTF-8 -d target/site/apidocs @target/main-sources
%mvn_artifact org.jspecify:jspecify:%{version} target/jspecify.jar

%install
%mvn_install

%check
test_classpath=target/jspecify.jar:$(build-classpath junit5 opentest4j junit hamcrest)
javac --release 8 -cp "$test_classpath" -d target/test-classes src/integrationTest/java/org/jspecify/annotations/NullMarkedTest.java %{SOURCE1}
java -cp "$test_classpath:target/test-classes" JSpecifyIntegrationRunner 'org.jspecify.annotations.NullMarkedTest$WithJava9OrLater' 'org.jspecify.annotations.NullMarkedTest$WithJava8'
java --module-path target/jspecify.jar --describe-module org.jspecify

%files -f .mfiles
%license LICENSE
%doc README.md AUTHORS

%files javadoc -f .mfiles-javadoc
%license LICENSE

%changelog
* Tue Sep 15 2026 w0fv1 <wofbi1@outlook.com> - 1.0.0-1
- Initial package
