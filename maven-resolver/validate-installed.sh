#!/usr/bin/bash
set -euo pipefail

expected_modules=(
    org.apache.maven.resolver
    org.apache.maven.resolver.connector.basic
    org.apache.maven.resolver.impl
    org.apache.maven.resolver.named.locks
    org.apache.maven.resolver.spi
    org.apache.maven.resolver.supplier
    org.apache.maven.resolver.transport.apache
    org.apache.maven.resolver.transport.file
    org.apache.maven.resolver.util
)

descriptions=$(for jar_file in /usr/share/java/maven-resolver/*.jar; do
    jar --describe-module --file "$jar_file" 2>&1
done)
for module in "${expected_modules[@]}"; do
    grep -q "^${module} automatic$" <<<"$descriptions"
done

java --module-path /usr/share/java/maven-resolver --validate-modules
xmvn-resolve org.apache.maven.resolver:maven-resolver-supplier-mvn3:2.0.21

resolver_classpath=$(find /usr/share/java/maven-resolver -name '*.jar' -printf ':%p')
maven_classpath=$(find /usr/share/java/maven -name '*.jar' ! -name 'maven-slf4j-provider.jar' -printf ':%p')
classpath="${resolver_classpath#:}${maven_classpath}:/usr/share/java/plexus/*:/usr/share/java/sisu/*:/usr/share/java/httpcomponents/*:/usr/share/java/guice/*:/usr/share/java/guava/*:/usr/share/java/slf4j/slf4j-api.jar:/usr/share/java/slf4j/slf4j-simple.jar"
javac -cp "$classpath" /tmp/InstalledCheck.java
java -cp "/tmp:$classpath" InstalledCheck
