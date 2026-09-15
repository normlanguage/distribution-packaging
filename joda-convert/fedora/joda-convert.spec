%global commit 158fc7a1d1ad725a9803a83bda866325d448f071

Name: joda-convert
Version: 3.0.1
Release: 1%{?dist}
Summary: Object and string conversion for Java
License: Apache-2.0
URL: https://www.joda.org/joda-convert/
Source0: https://api.github.com/repos/JodaOrg/joda-convert/tarball/%{commit}#/joda-convert-%{version}.tar.gz
BuildArch: noarch
BuildRequires: maven-local-openjdk25
BuildRequires: mvn(org.apache.maven.plugins:maven-enforcer-plugin)
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires: mvn(com.google.guava:guava)
BuildRequires: mvn(org.threeten:threetenbp)
BuildRequires: mvn(org.junit.jupiter:junit-jupiter)
BuildRequires: mvn(org.assertj:assertj-core)

%description
Joda-Convert converts objects to and from strings using annotations and
registered converters. It supports standard Java types and optional
integration with Guava and ThreeTen Backport.

%package javadoc
Summary: API documentation for Joda-Convert

%description javadoc
API documentation for Joda-Convert.

%prep
%autosetup -n JodaOrg-joda-convert-158fc7a
%pom_remove_plugin :maven-source-plugin
%pom_remove_plugin :maven-javadoc-plugin
%pom_remove_plugin :maven-checkstyle-plugin
%pom_remove_plugin :jacoco-maven-plugin
%pom_remove_plugin :maven-release-plugin
%pom_remove_plugin :maven-site-plugin
%pom_xpath_set "pom:build/pom:plugins/pom:plugin[pom:artifactId='maven-surefire-plugin']/pom:executions/pom:execution[pom:id='no-threetenbp']/pom:configuration/pom:classpathDependencyExcludes/pom:classpathDependencyExclude" org.threeten:threetenbp

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%license LICENSE.txt NOTICE.txt
%doc README.md

%files javadoc -f .mfiles-javadoc
%license LICENSE.txt NOTICE.txt

%changelog
* Tue Sep 15 2026 w0fv1 <wofbi1@outlook.com> - 3.0.1-1
- Initial package
