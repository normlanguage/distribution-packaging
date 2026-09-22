%global commit b043a90d792645869b7fc4dfc60e67fac38347a0
%global metadata_version 1.0.13

Name: graalvm-native-build-tools
Version: 1.1.12
Release: 1%{?dist}
Summary: Shared libraries for GraalVM Native Build Tools
License: UPL-1.0
URL: https://github.com/graalvm/native-build-tools
Source0: https://github.com/graalvm/native-build-tools/archive/%{commit}/native-build-tools-%{commit}.tar.gz
Source1: https://repo1.maven.org/maven2/org/graalvm/buildtools/utils/%{version}/utils-%{version}.pom
Source2: https://repo1.maven.org/maven2/org/graalvm/buildtools/graalvm-reachability-metadata/%{version}/graalvm-reachability-metadata-%{version}.pom
Source3: build.sh
Source4: check.sh
Patch0: relax-backoff-timing-test.patch
BuildArch: noarch
BuildRequires: java-25-openjdk-devel
BuildRequires: maven-local-openjdk25
BuildRequires: openjson
BuildRequires: junit5
BuildRequires: jimfs
BuildRequires: guava
BuildRequires: picocli
BuildRequires: apiguardian
BuildRequires: opentest4j

%description
This package contains shared utility and metadata handling libraries used to
configure code accessed from GraalVM native images.

%prep
%autosetup -n native-build-tools-%{commit} -p1

%build
bash %{SOURCE3} "$PWD" build %{_javadir}/openjson/openjson.jar %{version} %{metadata_version}

%install
%mvn_artifact %{SOURCE1} build/utils.jar
%mvn_artifact %{SOURCE2} build/graalvm-reachability-metadata.jar
%mvn_install

%check
test_classpath=$(
  build-classpath junit5 jimfs guava picocli apiguardian opentest4j
)
bash %{SOURCE4} "$PWD" build %{_javadir}/openjson/openjson.jar "$test_classpath"

%files -f .mfiles
%license common/utils/LICENSE
%license common/graalvm-reachability-metadata/LICENSE

%changelog
* Tue Sep 22 2026 w0fv1 <wofbi1@outlook.com> - 1.1.12-1
- Build the utility and reachability metadata libraries from source
