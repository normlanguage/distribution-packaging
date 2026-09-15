%global commit 2e1235766719b2db4f24c5c28920012850333833

Name: fastdoubleparser
Version: 2.0.1
Release: 1%{?dist}
Summary: Floating point number parsing for Java
License: MIT
URL: https://github.com/wrandelshofer/FastDoubleParser
Source0: https://api.github.com/repos/wrandelshofer/FastDoubleParser/tarball/%{commit}#/fastdoubleparser-%{version}.tar.gz
Source1: LeadingFormatCharactersTest.java
Patch0: utf8-leading-format-characters.patch
Patch1: explicit-arabic-numbering.patch
BuildArch: noarch
BuildRequires: maven-local-openjdk25
BuildRequires: mvn(org.apache.maven.plugins:maven-enforcer-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-assembly-plugin)
BuildRequires: mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires: mvn(org.junit.jupiter:junit-jupiter)
BuildRequires: mvn(org.junit.platform:junit-platform-suite-commons)

%description
FastDoubleParser converts decimal and hexadecimal text to floating point
numbers. It provides implementations optimized for different Java versions
in a single library.

%package javadoc
Summary: API documentation for FastDoubleParser

%description javadoc
API documentation for FastDoubleParser.

%prep
%autosetup -p1 -n wrandelshofer-FastDoubleParser-2e12357
cp %{SOURCE1} fastdoubleparser-dev/src/test/java/ch.randelshofer.fastdoubleparser/ch/randelshofer/fastdoubleparser/
for module in fastdoubleparserdemo*; do
    %pom_disable_module "$module"
done
%pom_disable_module fastdoubleparser-dev
%pom_remove_dep org.openjdk.jmh:jmh-core
%pom_remove_dep org.openjdk.jmh:jmh-generator-annprocess
find fastdoubleparser-dev/src/test -name 'Jmh*.java' -delete
%pom_remove_plugin :git-commit-id-maven-plugin
%pom_remove_plugin :maven-source-plugin
%pom_remove_plugin :maven-javadoc-plugin
%pom_remove_plugin :flatten-maven-plugin
%pom_remove_plugin :maven-gpg-plugin
%pom_remove_plugin :maven-javadoc-plugin fastdoubleparser
%pom_remove_plugin :maven-site-plugin fastdoubleparser
%pom_xpath_set pom:version %{version}
for module in fastdoubleparser fastdoubleparser-java*; do
    %pom_xpath_set pom:parent/pom:version %{version} "$module"
done
%pom_xpath_replace "pom:build/pom:plugins/pom:plugin[pom:artifactId='maven-surefire-plugin']/pom:configuration/pom:argLine" '<argLine>-Xmx2g</argLine>'
%pom_xpath_set "pom:build/pom:plugins/pom:plugin[pom:artifactId='maven-surefire-plugin']/pom:configuration/pom:forkCount" 1
%mvn_package :fastdoubleparser-java* __noinstall

%build
%mvn_build -j -- -Dgit.commit.id.full=%{commit} -Dgit.commit.time=2024-11-10T15:51:23Z
find fastdoubleparser/target/generated-sources/java -name '*.java' ! -name module-info.java | sort > javadoc-sources
javadoc -quiet -Xdoclint:none -encoding UTF-8 -classpath fastdoubleparser/target/fastdoubleparser-%{version}.jar -d target/site/apidocs @javadoc-sources

%install
%mvn_install

%files -f .mfiles
%license LICENSE NOTICE
%doc README.md

%files javadoc -f .mfiles-javadoc
%license LICENSE NOTICE

%changelog
* Tue Sep 15 2026 w0fv1 <wofbi1@outlook.com> - 2.0.1-1
- Initial package
