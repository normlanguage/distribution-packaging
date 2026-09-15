%global commit 7f3e47f4854c0b029847561cefffc3308ae0d6fb

Name: reflectasm
Version: 1.11.9
Release: 1%{?dist}
Summary: High performance Java reflection using code generation
License: BSD-3-Clause
URL: https://github.com/EsotericSoftware/reflectasm
Source0: https://github.com/EsotericSoftware/reflectasm/archive/%{commit}/reflectasm-%{version}.tar.gz
Patch0: generate_1_6_classes.patch
Patch1: switching_to_OpenJDK17.patch
Patch2: check-owned-classloaders.patch
BuildArch: noarch
BuildRequires: maven-local-openjdk25
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires: mvn(org.ow2.asm:asm)
BuildRequires: mvn(junit:junit)

%description
ReflectASM generates bytecode for efficient access to Java constructors,
methods and fields. This package uses the system ASM library.

%package javadoc
Summary: API documentation for ReflectASM

%description javadoc
API documentation for ReflectASM.

%prep
%autosetup -n reflectasm-%{commit} -p1
find . -name '*.jar' -delete
%pom_remove_parent
%pom_remove_plugin :maven-shade-plugin
%pom_xpath_remove "pom:build/pom:plugins/pom:plugin[pom:artifactId='maven-compiler-plugin']/pom:configuration"
%pom_xpath_remove "pom:build/pom:plugins/pom:plugin[pom:artifactId='maven-bundle-plugin']/pom:configuration/pom:instructions/pom:Import-Package"

%build
%mvn_build -- -Dmaven.compiler.release=8

%install
%mvn_install

%files -f .mfiles
%license license.txt
%doc README.md

%files javadoc -f .mfiles-javadoc
%license license.txt

%changelog
* Tue Sep 15 2026 w0fv1 <wofbi1@outlook.com> - 1.11.9-1
- Initial package
