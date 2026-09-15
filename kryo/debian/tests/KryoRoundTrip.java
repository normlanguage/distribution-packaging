import com.esotericsoftware.kryo.Kryo;
import com.esotericsoftware.kryo.io.Input;
import com.esotericsoftware.kryo.io.Output;
import java.util.ArrayList;

public final class KryoRoundTrip {
    public static void main(String[] args) {
        Kryo kryo = new Kryo();
        kryo.setReferences(true);
        kryo.register(ArrayList.class);
        ArrayList<Object> shared = new ArrayList<>();
        shared.add("Norm serialization");
        shared.add(null);
        ArrayList<Object> original = new ArrayList<>();
        original.add(shared);
        original.add(shared);
        byte[] bytes;
        try (Output output = new Output(128, -1)) {
            kryo.writeObject(output, original);
            bytes = output.toBytes();
        }
        try (Input input = new Input(bytes)) {
            ArrayList<?> restored = kryo.readObject(input, ArrayList.class);
            if (!original.equals(restored) || restored.get(0) != restored.get(1)) {
                throw new AssertionError("Values or shared references changed");
            }
        }
        System.out.println("Kryo installed-package round trip passed");
    }
}
