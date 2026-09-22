import java.nio.file.Files;
import java.nio.file.Path;
import java.util.jar.JarEntry;
import java.util.jar.JarOutputStream;
import org.eclipse.aether.RepositorySystem;
import org.eclipse.aether.RepositorySystemSession.CloseableSession;
import org.eclipse.aether.artifact.DefaultArtifact;
import org.eclipse.aether.repository.RemoteRepository;
import org.eclipse.aether.resolution.ArtifactRequest;
import org.eclipse.aether.supplier.RepositorySystemSupplier;
import org.eclipse.aether.supplier.SessionBuilderSupplier;

public final class InstalledCheck {
    public static void main(String[] args) throws Exception {
        Path root = Files.createTempDirectory("resolver-installed-check");
        Path remote = root.resolve("remote");
        Path artifactFile = remote.resolve("test/demo/1.0/demo-1.0.jar");
        Files.createDirectories(artifactFile.getParent());
        try (JarOutputStream jar = new JarOutputStream(Files.newOutputStream(artifactFile))) {
            jar.putNextEntry(new JarEntry("fixture.txt"));
            jar.write("resolved".getBytes());
            jar.closeEntry();
        }

        try (RepositorySystem system = new RepositorySystemSupplier().get();
             CloseableSession session = new SessionBuilderSupplier(system)
                     .get()
                     .withLocalRepositoryBaseDirectories(root.resolve("local"))
                     .build()) {
            ArtifactRequest request = new ArtifactRequest()
                    .setArtifact(new DefaultArtifact("test:demo:jar:1.0"))
                    .addRepository(new RemoteRepository.Builder(
                            "fixture", "default", remote.toUri().toString()).build());
            Path resolved = system.resolveArtifact(session, request)
                    .getArtifact()
                    .getPath();
            if (!Files.isRegularFile(resolved) || Files.mismatch(artifactFile, resolved) != -1) {
                throw new IllegalStateException("Resolved artifact differs from fixture");
            }
            System.out.println("resolved=" + resolved);
        }
    }
}
