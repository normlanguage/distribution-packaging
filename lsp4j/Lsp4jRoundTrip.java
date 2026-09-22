import java.io.PipedInputStream;
import java.io.PipedOutputStream;
import java.util.concurrent.CompletableFuture;
import java.util.concurrent.Executors;
import java.util.concurrent.TimeUnit;
import org.eclipse.lsp4j.jsonrpc.Launcher;
import org.eclipse.lsp4j.jsonrpc.services.JsonRequest;

public final class Lsp4jRoundTrip {
  public interface EchoService {
    @JsonRequest("echo")
    CompletableFuture<String> echo(String value);
  }

  public static final class EchoServiceImpl implements EchoService {
    @Override
    public CompletableFuture<String> echo(String value) {
      return CompletableFuture.completedFuture("reply:" + value);
    }
  }

  public static void main(String[] args) throws Exception {
    var serverExecutor = Executors.newCachedThreadPool();
    var clientExecutor = Executors.newCachedThreadPool();
    try (var serverInput = new PipedInputStream();
        var clientOutput = new PipedOutputStream(serverInput);
        var clientInput = new PipedInputStream();
        var serverOutput = new PipedOutputStream(clientInput)) {
      var server =
          new Launcher.Builder<EchoService>()
              .setLocalService(new EchoServiceImpl())
              .setRemoteInterface(EchoService.class)
              .setInput(serverInput)
              .setOutput(serverOutput)
              .setExecutorService(serverExecutor)
              .create();
      var client =
          new Launcher.Builder<EchoService>()
              .setLocalService(new EchoServiceImpl())
              .setRemoteInterface(EchoService.class)
              .setInput(clientInput)
              .setOutput(clientOutput)
              .setExecutorService(clientExecutor)
              .create();
      var serverListening = server.startListening();
      var clientListening = client.startListening();
      var reply = client.getRemoteProxy().echo("unicode-你好").get(10, TimeUnit.SECONDS);
      if (!reply.equals("reply:unicode-你好")) {
        throw new AssertionError(reply);
      }
      serverListening.cancel(true);
      clientListening.cancel(true);
      System.out.println(reply);
    } finally {
      serverExecutor.shutdownNow();
      clientExecutor.shutdownNow();
    }
  }
}
