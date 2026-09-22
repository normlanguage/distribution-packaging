%global commit fe81fc370ef85def8513f9691a25e572083128c7

Name: maven-resolver
Epoch: 1
Version: 2.0.21
Release: 1%{?dist}
Summary: Apache Maven Artifact Resolver library
License: Apache-2.0
URL: https://maven.apache.org/resolver/
Source0: https://github.com/apache/maven-resolver/archive/%{commit}/maven-resolver-%{commit}.tar.gz
BuildArch: noarch

BuildRequires: maven-local-openjdk25
BuildRequires: mvn(com.google.code.gson:gson)
BuildRequires: mvn(com.google.inject:guice)
BuildRequires: mvn(com.google.jimfs:jimfs)
BuildRequires: mvn(commons-codec:commons-codec)
BuildRequires: mvn(javax.inject:javax.inject)
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires: mvn(org.apache.httpcomponents:httpclient)
BuildRequires: mvn(org.apache.httpcomponents:httpcore)
BuildRequires: mvn(org.apache.maven:maven-model-builder)
BuildRequires: mvn(org.apache.maven:maven-parent:pom:)
BuildRequires: mvn(org.apache.maven:maven-resolver-provider)
BuildRequires: mvn(org.codehaus.plexus:plexus-utils)
BuildRequires: mvn(org.eclipse.sisu:org.eclipse.sisu.inject)
BuildRequires: mvn(org.eclipse.sisu:sisu-maven-plugin)
BuildRequires: mvn(org.junit.jupiter:junit-jupiter-api)
BuildRequires: mvn(org.junit.jupiter:junit-jupiter-params)
BuildRequires: mvn(org.mockito:mockito-core)
BuildRequires: mvn(org.slf4j:jcl-over-slf4j)
BuildRequires: mvn(org.slf4j:slf4j-api)
BuildRequires: mvn(org.slf4j:slf4j-simple)

%description
Apache Maven Artifact Resolver is a library for working with artifact
repositories and dependency resolution. This package includes the core,
connector, file and Apache transports, and the Maven 3 instance supplier.

%prep
%autosetup -n maven-resolver-%{commit}

rm maven-resolver-supplier-mvn3/src/test/java/org/eclipse/aether/supplier/RepositorySystemSupplierTest.java
rm maven-resolver-transport-apache/src/test/java/org/eclipse/aether/transport/apache/ApacheTransporterTest.java
%pom_remove_dep :maven-resolver-test-http maven-resolver-transport-apache
%pom_remove_dep org.eclipse.jetty:jetty-bom pom.xml
%pom_remove_dep org.openjdk.jmh: maven-resolver-util
%pom_remove_plugin :maven-compiler-plugin maven-resolver-util
rm -rf maven-resolver-util/src/jmh
rm maven-resolver-util/src/test/java/org/eclipse/aether/util/graph/transformer/ConflictResolverJMHBenchmark.java

for pom in $(find . -name pom.xml -exec grep -l '<artifactId>bnd-maven-plugin</artifactId>' {} +); do
  %pom_remove_plugin :bnd-maven-plugin "$pom"
done
for pom in $(find . -name pom.xml -exec grep -l '<artifactId>animal-sniffer-maven-plugin</artifactId>' {} +); do
  %pom_remove_plugin org.codehaus.mojo:animal-sniffer-maven-plugin "$pom"
done
for pom in $(find . -name pom.xml -exec grep -l '<artifactId>japicmp-maven-plugin</artifactId>' {} +); do
  %pom_remove_plugin :japicmp-maven-plugin "$pom"
done
for pom in $(find . -name pom.xml -exec grep -l '<artifactId>maven-enforcer-plugin</artifactId>' {} +); do
  %pom_remove_plugin :maven-enforcer-plugin "$pom"
done

%pom_disable_module maven-resolver-demos
%pom_disable_module maven-resolver-generator-gnupg
%pom_disable_module maven-resolver-generator-sigstore
%pom_disable_module maven-resolver-named-locks-hazelcast
%pom_disable_module maven-resolver-named-locks-ipc
%pom_disable_module maven-resolver-named-locks-redisson
%pom_disable_module maven-resolver-supplier-mvn4
%pom_disable_module maven-resolver-test-http
%pom_disable_module maven-resolver-tools
%pom_disable_module maven-resolver-transport-classpath
%pom_disable_module maven-resolver-transport-jdk-parent
%pom_disable_module maven-resolver-transport-jetty
%pom_disable_module maven-resolver-transport-minio
%pom_disable_module maven-resolver-transport-url
%pom_disable_module maven-resolver-transport-wagon
%mvn_package :maven-resolver-test-util __noinstall

for module in \
  api \
  connector-basic \
  impl \
  named-locks \
  spi \
  supplier-mvn3 \
  test-util \
  transport-apache \
  transport-file \
  util; do
  pom="maven-resolver-$module/pom.xml"
  case "$module" in
    api) module_name=org.apache.maven.resolver ;;
    supplier-mvn3) module_name=org.apache.maven.resolver.supplier ;;
    *) module_name="org.apache.maven.resolver.${module//-/.}" ;;
  esac
  %pom_add_plugin "org.apache.felix:maven-bundle-plugin" $pom \
  "<configuration>
    <instructions>
      <Bundle-SymbolicName>$module_name</Bundle-SymbolicName>
      <Automatic-Module-Name>$module_name</Automatic-Module-Name>
      <Export-Package>!org.eclipse.aether.internal*,org.eclipse.aether*</Export-Package>
      <_nouses>true</_nouses>
    </instructions>
  </configuration>
  <executions>
    <execution>
      <id>create-manifest</id>
      <phase>process-classes</phase>
      <goals><goal>manifest</goal></goals>
    </execution>
  </executions>"
done
%pom_add_plugin "org.apache.maven.plugins:maven-jar-plugin" pom.xml \
"<configuration>
  <archive>
    <manifestFile>\${project.build.outputDirectory}/META-INF/MANIFEST.MF</manifestFile>
  </archive>
</configuration>"

%mvn_alias 'org.apache.maven.resolver:maven-resolver{*}' 'org.eclipse.aether:aether@1'
%mvn_alias 'org.apache.maven.resolver:maven-resolver-transport-wagon' 'org.eclipse.aether:aether-connector-wagon'
%mvn_file ':maven-resolver{*}' %{name}/maven-resolver@1 aether/aether@1

%build
%mvn_build -j

%install
%mvn_install

%files -f .mfiles
%license LICENSE

%changelog
* Tue Sep 22 2026 w0fv1 <wofbi1@outlook.com> - 1:2.0.21-1
- Update to Maven Resolver 2.0.21
