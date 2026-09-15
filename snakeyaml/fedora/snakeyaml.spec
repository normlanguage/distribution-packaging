%bcond bootstrap 0

Name: snakeyaml
Version: 2.5
Release: 1%{?dist}
Summary: YAML parser and emitter for Java
License: Apache-2.0
URL: https://bitbucket.org/snakeyaml/snakeyaml
Source0: https://bitbucket.org/snakeyaml/snakeyaml/get/snakeyaml-%{version}.tar.gz
Patch0: plain-java-test-fixtures.patch
BuildArch: noarch
BuildRequires: maven-local-openjdk25
BuildRequires: mvn(org.apache.maven.plugins:maven-enforcer-plugin)
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(org.apache.velocity:velocity-engine-core)
BuildRequires: mvn(joda-time:joda-time)
%if %{without bootstrap}
BuildRequires: mvn(com.fasterxml.jackson.dataformat:jackson-dataformat-yaml)
%endif

%description
SnakeYAML parses and emits YAML documents and maps their content to Java
objects. It supports Unicode input, custom constructors and representers.

%package javadoc
Summary: API documentation for SnakeYAML

%description javadoc
API documentation for SnakeYAML.

%prep
%autosetup -p1 -n snakeyaml-snakeyaml-225cf7b0166c
%pom_xpath_set pom:build/pom:testResources/pom:testResource/pom:filtering false
%pom_xpath_inject pom:build/pom:testResources/pom:testResource '<excludes><exclude>org/yaml/snakeyaml/issues/issue318/classpath.properties</exclude></excludes>'
%pom_xpath_inject pom:build/pom:testResources '<testResource><directory>${basedir}/src/test/resources</directory><filtering>true</filtering><includes><include>org/yaml/snakeyaml/issues/issue318/classpath.properties</include></includes></testResource>'
%pom_remove_dep org.projectlombok:lombok
%pom_remove_dep org.openjdk.jmh:jmh-core
%pom_remove_dep org.openjdk.jmh:jmh-generator-annprocess
rm src/test/java/org/yaml/snakeyaml/jmh/ParseBenchmark.java
rm src/test/java/org/yaml/snakeyaml/jmh/EmitterBenchmark.java
%pom_remove_plugin :maven-eclipse-plugin
%pom_remove_plugin :maven-changes-plugin
%pom_remove_plugin :maven-source-plugin
%pom_remove_plugin :maven-javadoc-plugin
%pom_remove_plugin :jmh-maven-plugin
%pom_remove_plugin :maven-license-plugin
%pom_remove_plugin :maven-site-plugin
%pom_remove_plugin :maven-release-plugin
%pom_remove_plugin :central-publishing-maven-plugin
%pom_remove_plugin :formatter-maven-plugin
%if %{with bootstrap}
%pom_remove_dep com.fasterxml.jackson.dataformat:jackson-dataformat-yaml
rm src/test/java/org/yaml/snakeyaml/issues/issue1100/JacksonTest.java
%endif

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%license LICENSE.txt
%doc README.md

%files javadoc -f .mfiles-javadoc
%license LICENSE.txt

%changelog
* Tue Sep 15 2026 w0fv1 <wofbi1@outlook.com> - 2.5-1
- Initial package
