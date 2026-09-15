import com.esotericsoftware.minlog.Log;
import java.util.ArrayList;
import java.util.List;

public final class MinlogCheck {
    public static void main(String[] args) {
        List<String> messages = new ArrayList<>();
        RuntimeException expected = new RuntimeException("expected");
        Log.setLogger(new Log.Logger() {
            public void log(int level, String category, String message, Throwable error) {
                if (error != null && error != expected) throw new AssertionError("Throwable changed");
                messages.add(level + ":" + category + ":" + message);
            }
        });
        Log.WARN();
        Log.info("hidden");
        Log.warn("norm", "warning");
        Log.error("norm", "failure", expected);
        if (!messages.equals(List.of("4:norm:warning", "5:norm:failure"))) {
            throw new AssertionError(messages);
        }
        Log.NONE();
        Log.error("hidden");
        if (messages.size() != 2) throw new AssertionError("Disabled logger emitted a message");
        System.out.println("MinLog behavior checks passed");
    }
}
