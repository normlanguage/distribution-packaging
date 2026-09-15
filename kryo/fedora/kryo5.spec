%global commit fee63879ddcec23fbd09ac7785bc04a3de758483

Name: kryo5
Version: 5.6.2
Release: 1%{?dist}
Summary: Fast Java serialization library
License: BSD-3-Clause
URL: https://github.com/EsotericSoftware/kryo
Source0: https://github.com/EsotericSoftware/kryo/archive/%{commit}/kryo-%{version}.tar.gz
BuildArch: noarch
BuildRequires: maven-local-openjdk25
BuildRequires: mvn(org.apache.maven.plugins:maven-enforcer-plugin)
BuildRequires: mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires: mvn(com.esotericsoftware:minlog)
BuildRequires: mvn(com.esotericsoftware:reflectasm)
BuildRequires: mvn(org.objenesis:objenesis)
BuildRequires: mvn(org.junit.jupiter:junit-jupiter-api)
BuildRequires: mvn(org.junit.jupiter:junit-jupiter-engine)
BuildRequires: mvn(org.junit.jupiter:junit-jupiter-params)
BuildRequires: mvn(org.apache.commons:commons-lang3)

%description
Kryo provides fast and efficient Java object graph serialization with support
for references, customizable serialization and object copying.

%package javadoc
Summary: API documentation for Kryo

%description javadoc
API documentation for Kryo.

%prep
%autosetup -n kryo-%{commit}
find . -type f -name '*.jar' -delete
%pom_disable_module main-versioned
%pom_disable_module benchmarks
%pom_remove_plugin :maven-assembly-plugin main
%pom_remove_plugin :clirr-maven-plugin main
%mvn_file :kryo kryo5/kryo5

%build
%mvn_build -- -DskipKotlin=true -Dsource=8

%install
%mvn_install

%files -f .mfiles
%license LICENSE.md
%doc README.md

%files javadoc -f .mfiles-javadoc
%license LICENSE.md

%changelog
* Tue Sep 15 2026 w0fv1 <wofbi1@outlook.com> - 5.6.2-1
- Initial package
