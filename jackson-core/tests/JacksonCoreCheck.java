package check;

import com.fasterxml.jackson.core.JsonFactory;
import com.fasterxml.jackson.core.JsonFactoryBuilder;
import com.fasterxml.jackson.core.JsonGenerator;
import com.fasterxml.jackson.core.JsonParseException;
import com.fasterxml.jackson.core.JsonParser;
import com.fasterxml.jackson.core.JsonToken;
import com.fasterxml.jackson.core.StreamReadFeature;
import java.io.StringWriter;
import java.math.BigInteger;
import java.util.ServiceLoader;

public final class JacksonCoreCheck {
    public static void main(String[] args) throws Exception {
        JsonFactory factory = new JsonFactoryBuilder()
                .enable(StreamReadFeature.USE_FAST_DOUBLE_PARSER)
                .enable(StreamReadFeature.USE_FAST_BIG_NUMBER_PARSER)
                .build();
        String integer = "1234567890".repeat(30);
        String text = "hello \u4e16\u754c";
        StringWriter output = new StringWriter();
        try (JsonGenerator generator = factory.createGenerator(output)) {
            generator.writeStartArray();
            generator.writeNumber(1.2345678901234567);
            generator.writeNumber(new BigInteger(integer));
            generator.writeString(text);
            generator.writeEndArray();
        }
        try (JsonParser parser = factory.createParser(output.toString())) {
            if (parser.nextToken() != JsonToken.START_ARRAY
                    || parser.nextToken() != JsonToken.VALUE_NUMBER_FLOAT
                    || parser.getDoubleValue() != 1.2345678901234567
                    || parser.nextToken() != JsonToken.VALUE_NUMBER_INT
                    || !new BigInteger(integer).equals(parser.getBigIntegerValue())
                    || parser.nextToken() != JsonToken.VALUE_STRING
                    || !text.equals(parser.getText())
                    || parser.nextToken() != JsonToken.END_ARRAY
                    || parser.nextToken() != null) {
                throw new AssertionError("JSON round trip");
            }
        }
        try (JsonParser parser = factory.createParser("[1,]")) {
            while (parser.nextToken() != null) {
                parser.skipChildren();
            }
            throw new AssertionError("Invalid JSON was accepted");
        } catch (JsonParseException expected) {
            if (!"2.20.2".equals(factory.version().toString())) {
                throw new AssertionError("Generated version");
            }
        }
        if (ServiceLoader.load(JsonFactory.class).stream().noneMatch(provider -> provider.type() == JsonFactory.class)) {
            throw new AssertionError("JsonFactory service provider");
        }
        System.out.println("Fast numeric parsing, Unicode round trip, invalid input, version and service discovery passed");
    }
}
