package check;

import com.oracle.truffle.api.nodes.RootNode;
import java.util.Map;
import org.graalvm.polyglot.Context;
import org.graalvm.polyglot.proxy.ProxyExecutable;
import org.graalvm.polyglot.proxy.ProxyObject;

public final class TruffleCheck {
    public abstract static class Greeter {
        public abstract String greet(String name);
    }

    public static void main(String[] args) {
        if (AddOneNodeGen.getUncached().execute(41) != 42) {
            throw new AssertionError("Generated DSL node");
        }
        if (!Integer.valueOf(42).equals(RootNode.createConstantNode(42).getCallTarget().call())) {
            throw new AssertionError("Truffle call target");
        }
        try (Context context = Context.newBuilder().allowAllAccess(true).build()) {
            ProxyExecutable greet = values -> "Hello, " + values[0].asString();
            var proxy = ProxyObject.fromMap(Map.of("greet", greet));
            Greeter adapter = context.asValue(proxy).as(Greeter.class);
            if (!"Hello, \u96ea".equals(adapter.greet("\u96ea"))) {
                throw new AssertionError("ASM host adapter");
            }
        }
        System.out.println("Generated DSL node, Truffle call target and ASM host adapter passed");
    }
}
