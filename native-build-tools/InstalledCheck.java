import java.nio.file.Files;
import java.util.List;
import org.graalvm.buildtools.utils.SharedConstants;
import org.graalvm.reachability.DirectoryConfiguration;

public final class InstalledCheck {
  public static void main(String[] args) throws Exception {
    var source = Files.createTempDirectory("reachability-source");
    var destination = Files.createTempDirectory("reachability-destination");
    Files.writeString(source.resolve("reflect-config.json"), "[]");
    DirectoryConfiguration.copy(
        List.of(new DirectoryConfiguration("dev.w0fv1", "norm", "1", source, true)),
        destination);
    var copied =
        destination.resolve("META-INF/native-image/dev.w0fv1/norm/1/reflect-config.json");
    var properties =
        destination.resolve("META-INF/native-image/dev.w0fv1/norm/1/reachability-metadata.properties");
    if (!Files.readString(copied).equals("[]")) {
      throw new AssertionError(copied);
    }
    if (!Files.readString(properties).equals("override=true\n")) {
      throw new AssertionError(properties);
    }
    if (!SharedConstants.METADATA_REPO_DEFAULT_VERSION.equals("1.0.13")) {
      throw new AssertionError(SharedConstants.METADATA_REPO_DEFAULT_VERSION);
    }
    System.out.println("reachability metadata installed API passed");
  }
}
