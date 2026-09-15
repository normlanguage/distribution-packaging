%global commit 57cf9fde68ae40efc3943557caccd3628bccc3cf

Name: commonmark-java
Version: 0.29.0
Release: 1%{?dist}
Summary: CommonMark parsing and rendering for Java
License: BSD-2-Clause
URL: https://github.com/commonmark/commonmark-java
Source0: https://github.com/commonmark/commonmark-java/archive/%{commit}/commonmark-%{version}.tar.gz
BuildArch: noarch
BuildRequires: maven-local-openjdk25
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires: mvn(org.junit.jupiter:junit-jupiter)
BuildRequires: mvn(org.assertj:assertj-core)
BuildRequires: mvn(org.nibor.autolink:autolink)

%description
A Java library for parsing CommonMark text into an abstract syntax tree,
rendering HTML and extending the supported syntax.

%package javadoc
Summary: API documentation for CommonMark Java

%description javadoc
API documentation for CommonMark Java.

%prep
%autosetup -n commonmark-java-%{commit}
%pom_remove_plugin :central-publishing-maven-plugin
%pom_remove_plugin :maven-release-plugin
%pom_remove_dep org.openjdk.jmh: commonmark
%pom_remove_dep org.openjdk.jmh: commonmark-integration-test
%pom_remove_dep org.pegdown:pegdown commonmark-integration-test
rm commonmark/src/test/java/org/commonmark/test/SpecBenchmark.java
rm commonmark-integration-test/src/test/java/org/commonmark/integration/PegDownBenchmark.java
%mvn_package :commonmark-test-util __noinstall
%mvn_package :commonmark-integration-test __noinstall

%build
%mvn_build -j
find commonmark commonmark-ext-* -path "*/src/main/java/*.java" ! -name module-info.java | sort > javadoc-sources
classpath=$(find commonmark commonmark-ext-* -type d -path "*/target/classes" -printf "%%p:")$(build-classpath autolink-java/autolink)
javadoc -quiet -Xdoclint:none -encoding UTF-8 -d target/site/apidocs -classpath "$classpath" @javadoc-sources

%install
%mvn_install

%files -f .mfiles
%license LICENSE.txt
%doc README.md

%files javadoc -f .mfiles-javadoc
%license LICENSE.txt

%changelog
* Tue Sep 15 2026 w0fv1 <wofbi1@outlook.com> - 0.29.0-1
- Initial package
