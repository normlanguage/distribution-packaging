%global commit bbfaf93fbc7b33fa266b1e246efb099a41869917

Name: joda-time
Version: 2.14.3
Release: 1%{?dist}
Summary: Date and time library for Java
License: Apache-2.0 AND LicenseRef-Fedora-Public-Domain
URL: https://www.joda.org/joda-time/
Source0: https://api.github.com/repos/JodaOrg/joda-time/tarball/%{commit}#/joda-time-%{version}.tar.gz
BuildArch: noarch
BuildRequires: maven-local-openjdk25
BuildRequires: mvn(org.apache.maven.plugins:maven-enforcer-plugin)
BuildRequires: mvn(org.codehaus.mojo:exec-maven-plugin)
BuildRequires: mvn(org.joda:joda-convert)
BuildRequires: mvn(junit:junit)

%description
Joda-Time provides calendar systems, date and time types, duration and
interval handling, and formatting for Java applications. Time zone rules are
compiled from the accompanying source data.

%package javadoc
Summary: API documentation for Joda-Time

%description javadoc
API documentation for Joda-Time.

%prep
%autosetup -n JodaOrg-joda-time-bbfaf93
%pom_remove_plugin :maven-source-plugin
%pom_remove_plugin :maven-javadoc-plugin
%pom_remove_plugin :maven-release-plugin
%pom_remove_plugin :maven-site-plugin
%pom_remove_plugin :clirr-maven-plugin
%pom_xpath_remove "pom:profiles/pom:profile[pom:id='attach-additional-javadoc']"
%pom_xpath_remove "pom:build/pom:plugins/pom:plugin[pom:artifactId='maven-jar-plugin']/pom:executions/pom:execution[pom:id='no-tzdb']"

%build
%mvn_build -- -Dmaven.compiler.release=8

%install
%mvn_install

%files -f .mfiles
%license LICENSE.txt NOTICE.txt src/main/java/org/joda/time/tz/src/Readme.txt
%doc README.md

%files javadoc -f .mfiles-javadoc
%license LICENSE.txt NOTICE.txt

%changelog
* Tue Sep 15 2026 w0fv1 <wofbi1@outlook.com> - 2.14.3-1
- Initial package
