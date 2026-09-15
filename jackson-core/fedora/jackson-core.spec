%global commit 7d66273aefcdfc1a77127ddad18937cef735d57e

Name: jackson-core
Version: 2.20.2
Release: 1%{?dist}
Summary: Streaming JSON processing for Java
License: Apache-2.0
URL: https://github.com/FasterXML/jackson-core
Source0: https://api.github.com/repos/FasterXML/jackson-core/tarball/%{commit}#/jackson-core-%{version}.tar.gz
Patch0: system-fastdoubleparser-module.patch
BuildArch: noarch
BuildRequires: maven-local-openjdk25
BuildRequires: mvn(com.fasterxml.jackson:jackson-base:pom:) >= 2.20.2
BuildRequires: mvn(ch.randelshofer:fastdoubleparser) >= 2.0.1
BuildRequires: mvn(org.apache.maven.plugins:maven-enforcer-plugin)
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires: mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires: mvn(com.google.code.maven-replacer-plugin:replacer)
BuildRequires: mvn(org.moditect:moditect-maven-plugin)
BuildRequires: mvn(org.junit.jupiter:junit-jupiter)
BuildRequires: mvn(org.assertj:assertj-core)

%description
Jackson Core provides a streaming API for reading and writing JSON documents.
Its numeric parsing uses the system FastDoubleParser library.

%package javadoc
Summary: API documentation for Jackson Core

%description javadoc
API documentation for Jackson Core.

%prep
%autosetup -p1 -n FasterXML-jackson-core-7d66273
%pom_remove_plugin :maven-shade-plugin
%pom_remove_plugin :jacoco-maven-plugin
%pom_remove_plugin :cyclonedx-maven-plugin
%pom_remove_plugin :gradle-module-metadata-maven-plugin
%pom_remove_plugin :animal-sniffer-maven-plugin
%pom_remove_plugin :maven-site-plugin
%pom_xpath_remove "pom:build/pom:plugins/pom:plugin[pom:artifactId='maven-enforcer-plugin']/pom:executions/pom:execution[pom:id='enforce-jacoco-exec']"
%pom_xpath_set pom:properties/pom:osgi.import '*'
mv src/main/resources/META-INF/jackson-core-LICENSE src/main/resources/META-INF/LICENSE
mv src/main/resources/META-INF/jackson-core-NOTICE src/main/resources/META-INF/NOTICE

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%license LICENSE src/main/resources/META-INF/NOTICE
%doc README.md

%files javadoc -f .mfiles-javadoc
%license LICENSE src/main/resources/META-INF/NOTICE

%changelog
* Tue Sep 15 2026 w0fv1 <wofbi1@outlook.com> - 2.20.2-1
- Initial package
