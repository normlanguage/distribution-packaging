%global commit 11222d46ff9d6209c5af51466000341cd5d29034

Name: minlog
Version: 1.3.1
Release: 1%{?dist}
Summary: Minimal overhead Java logging
License: BSD-3-Clause
URL: https://github.com/EsotericSoftware/minlog
Source0: https://github.com/EsotericSoftware/minlog/archive/%{commit}/minlog-%{version}.tar.gz
Source1: MinlogCheck.java
BuildArch: noarch
BuildRequires: maven-local-openjdk25
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires: mvn(junit:junit)

%description
MinLog provides lightweight Java logging with configurable levels and custom
log handlers.

%package javadoc
Summary: API documentation for MinLog

%description javadoc
API documentation for MinLog.

%prep
%autosetup -n minlog-%{commit}
%pom_remove_parent
%pom_remove_plugin :maven-source-plugin
%pom_remove_plugin :maven-javadoc-plugin
%pom_remove_plugin :maven-release-plugin
%pom_xpath_remove "pom:build/pom:plugins/pom:plugin[pom:artifactId='maven-jar-plugin']/pom:executions"

%build
%mvn_build -- -Dmaven.compiler.release=8

%install
%mvn_install

%check
javac -cp target/classes -d target/test-classes %{SOURCE1}
java -cp target/classes:target/test-classes MinlogCheck

%files -f .mfiles
%license license.txt
%doc README.md

%files javadoc -f .mfiles-javadoc
%license license.txt

%changelog
* Tue Sep 15 2026 w0fv1 <wofbi1@outlook.com> - 1.3.1-1
- Initial package
