%global commit 2a26844ad13cf49562009867d55b30a084230f2b

Name: jackson-bom
Version: 2.20.2
Release: 1%{?dist}
Summary: Jackson dependency management and base POMs
License: Apache-2.0
URL: https://github.com/FasterXML/jackson-bom
Source0: https://api.github.com/repos/FasterXML/jackson-bom/tarball/%{commit}#/jackson-bom-%{version}.tar.gz
BuildArch: noarch
BuildRequires: maven-local-openjdk25
BuildRequires: mvn(org.apache.maven.plugins:maven-enforcer-plugin)
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires: mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires: mvn(com.fasterxml.jackson:jackson-parent:pom:) >= 2.20
BuildRequires: mvn(org.junit:junit-bom:pom:)
Requires: mvn(com.fasterxml.jackson:jackson-parent:pom:) >= 2.20
Requires: mvn(org.junit:junit-bom:pom:)

%description
Maven dependency management and base project configuration for Jackson.

%prep
%autosetup -n FasterXML-jackson-bom-2a26844
%pom_remove_plugin :central-publishing-maven-plugin base

%build
%mvn_build -j

%install
%mvn_install

%files -f .mfiles
%license LICENSE
%doc README.md

%changelog
* Tue Sep 15 2026 w0fv1 <wofbi1@outlook.com> - 2.20.2-1
- Initial package
