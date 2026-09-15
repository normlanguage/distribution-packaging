%global commit 687ad4f318cd633eb0000f888bbb936c328dddde

Name: jackson-dataformat-yaml
Version: 2.21.5
Release: 1%{?dist}
Summary: YAML support for Jackson
License: Apache-2.0
URL: https://github.com/FasterXML/jackson-dataformats-text
Source0: https://api.github.com/repos/FasterXML/jackson-dataformats-text/tarball/%{commit}#/jackson-dataformats-text-%{version}.tar.gz
BuildArch: noarch
BuildRequires: maven-local-openjdk25
BuildRequires: mvn(com.fasterxml.jackson:jackson-base:pom:) >= 2.21.5
BuildRequires: mvn(com.fasterxml.jackson.core:jackson-core) >= 2.21.5
BuildRequires: mvn(com.fasterxml.jackson.core:jackson-databind) >= 2.21.5
BuildRequires: mvn(com.fasterxml.jackson.core:jackson-annotations) >= 2.21
BuildRequires: mvn(org.yaml:snakeyaml) >= 2.5
BuildRequires: mvn(org.apache.maven.plugins:maven-enforcer-plugin)
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires: mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires: mvn(com.google.code.maven-replacer-plugin:replacer)
BuildRequires: mvn(org.moditect:moditect-maven-plugin)
BuildRequires: mvn(org.junit.jupiter:junit-jupiter)
BuildRequires: mvn(org.assertj:assertj-core)
Requires: mvn(com.fasterxml.jackson.core:jackson-core) >= 2.21.5
Requires: mvn(com.fasterxml.jackson.core:jackson-databind) >= 2.21.5
Requires: mvn(org.yaml:snakeyaml) >= 2.5

%description
Jackson YAML provides streaming and object mapping support for YAML documents
using the Jackson API and the system SnakeYAML library.

%package javadoc
Summary: API documentation for Jackson YAML

%description javadoc
API documentation for Jackson YAML.

%prep
%autosetup -n FasterXML-jackson-dataformats-text-687ad4f
%pom_disable_module csv
%pom_disable_module properties
%pom_disable_module toml
%pom_remove_plugin :cyclonedx-maven-plugin yaml
%pom_remove_plugin :gradle-module-metadata-maven-plugin yaml

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%license LICENSE
%doc README.md

%files javadoc -f .mfiles-javadoc
%license LICENSE

%changelog
* Tue Sep 15 2026 w0fv1 <wofbi1@outlook.com> - 2.21.5-1
- Initial package
