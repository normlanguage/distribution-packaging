import com.github.openjson.JSONObject;
import com.github.openjson.JSONArray;

public final class OpenjsonRoundTrip {
    public static void main(String[] args) {
        JSONObject original = new JSONObject().put("language", "Norm").put("count", 42)
            .put("items", new JSONArray().put(true).put(JSONObject.NULL));
        JSONObject restored = new JSONObject(original.toString());
        if (!restored.getString("language").equals("Norm") || restored.getInt("count") != 42
            || !restored.getJSONArray("items").getBoolean(0)
            || !restored.getJSONArray("items").isNull(1)) {
            throw new AssertionError(restored.toString());
        }
        System.out.println("Installed OpenJSON round trip passed");
    }
}
