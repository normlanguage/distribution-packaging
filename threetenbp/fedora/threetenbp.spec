%global commit 4032d4137bcce776f72839c208ad4a8947e9f891
%global tzversion 2026cgtz

Name: threetenbp
Version: 1.7.4
Release: 1%{?dist}
Summary: Date and time library for Java
License: BSD-3-Clause AND LicenseRef-Fedora-Public-Domain
URL: https://www.threeten.org/threetenbp/
Source0: https://api.github.com/repos/ThreeTen/threetenbp/tarball/%{commit}#/threetenbp-%{version}.tar.gz
Source1: https://github.com/JodaOrg/global-tz/releases/download/%{tzversion}/tzdata%{tzversion}-rearguard.tar.gz
Patch0: jdk25-portuguese-weekdays.patch
BuildArch: noarch
BuildRequires: maven-local-openjdk25
BuildRequires: mvn(org.apache.maven.plugins:maven-enforcer-plugin)
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires: mvn(org.codehaus.mojo:exec-maven-plugin)
BuildRequires: mvn(org.testng:testng)

%description
ThreeTen Backport provides the Java date and time API as a separate library.
It includes calendar types, formatting, parsing and time zone rules.

%package javadoc
Summary: API documentation for ThreeTen Backport

%description javadoc
API documentation for ThreeTen Backport.

%prep
%autosetup -p1 -n ThreeTen-threetenbp-4032d41
mkdir -p src/tzdb/%{tzversion}
tar -xf %{SOURCE1} -C src/tzdb/%{tzversion}
rm src/main/resources/org/threeten/bp/TZDB.dat
%pom_remove_plugin :maven-source-plugin
%pom_remove_plugin :maven-javadoc-plugin
%pom_xpath_remove "pom:profiles/pom:profile[pom:id='attach-additional-javadoc']"
%pom_xpath_remove "pom:build/pom:plugins/pom:plugin[pom:artifactId='maven-jar-plugin']/pom:executions/pom:execution[pom:id='no-tzdb']"
%pom_xpath_remove "pom:build/pom:plugins/pom:plugin[pom:artifactId='maven-surefire-plugin']/pom:configuration/pom:properties"
%pom_xpath_set "pom:profiles/pom:profile[pom:id='tzdb-update']/pom:build/pom:plugins/pom:plugin/pom:executions/pom:execution/pom:phase" process-classes
%pom_xpath_set "pom:profiles/pom:profile[pom:id='tzdb-update']/pom:build/pom:plugins/pom:plugin/pom:configuration/pom:arguments/pom:argument[4]" '${project.build.outputDirectory}/org/threeten/bp'
%pom_xpath_set "pom:build/pom:plugins/pom:plugin[pom:artifactId='maven-bundle-plugin']/pom:executions/pom:execution/pom:configuration/pom:instructions/pom:Require-Capability" 'osgi.ee;filter:="(&amp;(osgi.ee=JavaSE)(version=1.8))"'

%build
%mvn_build -- -Dtzdb-update -Dmaven.compiler.release=8

%install
%mvn_install

%files -f .mfiles
%license LICENSE.txt src/tzdb/%{tzversion}/LICENSE
%doc README.md

%files javadoc -f .mfiles-javadoc
%license LICENSE.txt

%changelog
* Tue Sep 15 2026 w0fv1 <wofbi1@outlook.com> - 1.7.4-1
- Initial package
