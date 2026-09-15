%global commit ed5f1788d63ad39bf0c5e6f3837a0b369f501843

Name: fasterxml-oss-parent
Version: 70
Release: 1%{?dist}
Summary: Parent POM for FasterXML projects
License: Apache-2.0
URL: https://github.com/FasterXML/oss-parent
Source0: https://api.github.com/repos/FasterXML/oss-parent/tarball/%{commit}#/fasterxml-oss-parent-%{version}.tar.gz
BuildArch: noarch
BuildRequires: maven-local-openjdk25
BuildRequires: mvn(org.apache.maven.plugins:maven-enforcer-plugin)
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires: mvn(org.codehaus.mojo:build-helper-maven-plugin)

%description
Shared Maven project configuration for FasterXML libraries.

%prep
%autosetup -n FasterXML-oss-parent-ed5f178
%pom_remove_plugin :jacoco-maven-plugin
%pom_remove_plugin :maven-scm-plugin
%pom_remove_plugin :maven-site-plugin
%pom_remove_plugin :central-publishing-maven-plugin
%pom_xpath_remove pom:build/pom:extensions

%build
%mvn_build -j

%install
%mvn_install

%files -f .mfiles
%license LICENSE NOTICE
%doc README.creole

%changelog
* Tue Sep 15 2026 w0fv1 <wofbi1@outlook.com> - 70-1
- Initial package
