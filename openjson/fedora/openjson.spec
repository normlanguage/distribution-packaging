%global commit a83081b08f7f0fad0744aa087620982ec5843c16

Name: openjson
Version: 1.0.13
Release: 1%{?dist}
Summary: Simple JSON processing for Java
License: Apache-2.0
URL: https://github.com/openjson/openjson
Source0: https://github.com/openjson/openjson/archive/%{commit}/openjson-%{version}.tar.gz
BuildArch: noarch
BuildRequires: maven-local-openjdk25
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires: mvn(junit:junit)

%description
OpenJSON provides JSON objects, arrays and text processing for Java under
the Apache license.

%package javadoc
Summary: API documentation for OpenJSON

%description javadoc
API documentation for OpenJSON.

%prep
%autosetup -n openjson-%{commit}
%pom_remove_plugin :maven-source-plugin
%pom_remove_plugin :maven-javadoc-plugin
%pom_remove_plugin :maven-release-plugin
%pom_remove_plugin :jacoco-maven-plugin
%pom_xpath_remove "pom:build/pom:plugins/pom:plugin[pom:artifactId='maven-surefire-plugin']/pom:configuration/pom:argLine"
%pom_xpath_remove "pom:build/pom:plugins/pom:plugin[pom:artifactId='maven-compiler-plugin']/pom:configuration"

%build
%mvn_build -- -Dmaven.compiler.release=8

%install
%mvn_install

%files -f .mfiles
%license LICENSE.txt NOTICE
%doc README.md

%files javadoc -f .mfiles-javadoc
%license LICENSE.txt NOTICE

%changelog
* Tue Sep 15 2026 w0fv1 <wofbi1@outlook.com> - 1.0.13-1
- Initial package
