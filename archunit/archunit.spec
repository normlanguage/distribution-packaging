%global commit 502d782bfbf2632a2c9f943a502ddd8cc3e3c46d

Name: archunit
Version: 1.5.0
Release: 1%{?dist}
Summary: Java architecture test library
License: Apache-2.0
URL: https://www.archunit.org/
Source0: https://github.com/TNG/ArchUnit/archive/%{commit}/ArchUnit-%{commit}.tar.gz
Source1: archunit.pom
Source2: build.sh
Source3: ArchUnitCheck.java
BuildArch: noarch
BuildRequires: java-25-openjdk-devel
BuildRequires: maven-local-openjdk25
BuildRequires: objectweb-asm
BuildRequires: guava
BuildRequires: slf4j
Requires: objectweb-asm
Requires: guava
Requires: slf4j

%description
ArchUnit is a Java testing library for checking architectural constraints in
Java code.

%prep
%autosetup -n ArchUnit-%{commit}

%build
classpath=$(build-classpath objectweb-asm guava slf4j/slf4j-api)
bash %{SOURCE2} "$PWD" build "$classpath"

%install
%mvn_artifact %{SOURCE1} build/archunit.jar
%mvn_install

%check
classpath="build/archunit.jar:$(build-classpath objectweb-asm guava slf4j/slf4j-api)"
javac --release 17 -cp "$classpath" -d build/check %{SOURCE3}
java -cp "build/check:$classpath" ArchUnitCheck
java --module-path "$classpath" --validate-modules

%files -f .mfiles
%license LICENSE NOTICE

%changelog
* Tue Sep 22 2026 w0fv1 <wofbi1@outlook.com> - 1.5.0-1
- Build the core architecture test library from source
