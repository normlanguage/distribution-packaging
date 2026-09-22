Name: lsp4j
Version: 1.0.0
Release: 1%{?dist}
Summary: Java binding for the Language Server Protocol
License: EPL-2.0
URL: https://github.com/eclipse-lsp4j/lsp4j
Source0: https://repo1.maven.org/maven2/org/eclipse/lsp4j/org.eclipse.lsp4j/%{version}/org.eclipse.lsp4j-%{version}-sources.jar
Source1: https://repo1.maven.org/maven2/org/eclipse/lsp4j/org.eclipse.lsp4j.jsonrpc/%{version}/org.eclipse.lsp4j.jsonrpc-%{version}-sources.jar
Source2: https://repo1.maven.org/maven2/org/eclipse/lsp4j/org.eclipse.lsp4j/%{version}/org.eclipse.lsp4j-%{version}.pom
Source3: https://repo1.maven.org/maven2/org/eclipse/lsp4j/org.eclipse.lsp4j.jsonrpc/%{version}/org.eclipse.lsp4j.jsonrpc-%{version}.pom
Source4: https://raw.githubusercontent.com/eclipse-lsp4j/lsp4j/1eb88b3cdc163a0de1bfba1bc3ace816e1d94097/LICENSE
Source5: build-source-release.sh
Source6: Lsp4jRoundTrip.java
BuildArch: noarch
BuildRequires: java-25-openjdk-devel
BuildRequires: maven-local-openjdk25
BuildRequires: google-gson

%description
LSP4J provides Java bindings for the Language Server Protocol and a generic
JSON-RPC implementation.

%prep
%setup -q -c -T
cp %{SOURCE4} LICENSE

%build
bash %{SOURCE5} build %{SOURCE0} %{SOURCE1} %{_javadir}/google-gson/gson.jar

%install
%mvn_artifact %{SOURCE2} build/org.eclipse.lsp4j.jar
%mvn_artifact %{SOURCE3} build/org.eclipse.lsp4j.jsonrpc.jar
%mvn_install

%check
java --module-path build:%{_javadir}/google-gson/gson.jar --validate-modules
javac --release 11 -cp build/org.eclipse.lsp4j.jar:build/org.eclipse.lsp4j.jsonrpc.jar:%{_javadir}/google-gson/gson.jar -d build/test-classes %{SOURCE6}
java -cp build/test-classes:build/org.eclipse.lsp4j.jar:build/org.eclipse.lsp4j.jsonrpc.jar:%{_javadir}/google-gson/gson.jar Lsp4jRoundTrip

%files -f .mfiles
%license LICENSE

%changelog
* Tue Sep 22 2026 w0fv1 <wofbi1@outlook.com> - 1.0.0-1
- Build LSP and JSON-RPC modules from the upstream source release
