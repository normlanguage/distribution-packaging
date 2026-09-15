%global commit e51bbfa5b0f9b7e11da972a2c48385b330309fa8

Name: jackson-parent
Version: 2.20
Release: 1%{?dist}
Summary: Parent POM for Jackson projects
License: Apache-2.0
URL: https://github.com/FasterXML/jackson-parent
Source0: https://api.github.com/repos/FasterXML/jackson-parent/tarball/%{commit}#/jackson-parent-%{version}.tar.gz
BuildArch: noarch
BuildRequires: maven-local-openjdk25
BuildRequires: mvn(org.apache.maven.plugins:maven-enforcer-plugin)
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires: mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires: mvn(com.fasterxml:oss-parent:pom:) >= 70
Requires: mvn(com.fasterxml:oss-parent:pom:) >= 70

%description
Shared Maven project configuration for Jackson libraries.

%prep
%autosetup -n FasterXML-jackson-parent-e51bbfa

%build
%mvn_build -j

%install
%mvn_install

%files -f .mfiles
%doc README.md

%changelog
* Tue Sep 15 2026 w0fv1 <wofbi1@outlook.com> - 2.20-1
- Initial package
