import java.io.PrintWriter;
import org.junit.platform.engine.discovery.DiscoverySelectors;
import org.junit.platform.launcher.core.LauncherDiscoveryRequestBuilder;
import org.junit.platform.launcher.core.LauncherFactory;
import org.junit.platform.launcher.listeners.SummaryGeneratingListener;

public final class JSpecifyIntegrationRunner {
    public static void main(String[] args) {
        LauncherDiscoveryRequestBuilder request = LauncherDiscoveryRequestBuilder.request();
        for (String className : args) {
            request.selectors(DiscoverySelectors.selectClass(className));
        }
        SummaryGeneratingListener listener = new SummaryGeneratingListener();
        LauncherFactory.create().execute(request.build(), listener);
        listener.getSummary().printTo(new PrintWriter(System.out, true));
        listener.getSummary().printFailuresTo(new PrintWriter(System.out, true));
        if (listener.getSummary().getTestsSucceededCount() == 0
            || listener.getSummary().getTestsFailedCount() != 0
            || listener.getSummary().getContainersFailedCount() != 0) {
            throw new AssertionError("JUnit integration checks failed");
        }
    }
}
