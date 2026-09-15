package check;

import com.fasterxml.jackson.core.JsonFactory;
import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.core.JsonToken;
import com.fasterxml.jackson.core.ObjectCodec;
import com.fasterxml.jackson.core.StreamReadFeature;
import com.fasterxml.jackson.dataformat.yaml.YAMLFactory;
import com.fasterxml.jackson.dataformat.yaml.YAMLGenerator;
import com.fasterxml.jackson.dataformat.yaml.YAMLMapper;
import com.fasterxml.jackson.dataformat.yaml.YAMLParser;
import java.util.List;
import java.util.ServiceLoader;

public final class JacksonYamlCheck {
    public record Settings(String name, int count, List<String> flags) {}

    public static void main(String[] args) throws Exception {
        YAMLFactory factory = YAMLFactory.builder()
                .enable(StreamReadFeature.STRICT_DUPLICATE_DETECTION)
                .disable(YAMLGenerator.Feature.WRITE_DOC_START_MARKER)
                .build();
        YAMLMapper mapper = new YAMLMapper(factory);
        Settings value = new Settings("Norm", 3, List.of("\u96ea", "\u03bb"));
        String encoded = mapper.writeValueAsString(value);
        if (encoded.startsWith("---") || !value.equals(mapper.readValue(encoded, Settings.class))) {
            throw new AssertionError("Unicode record round trip and document marker");
        }
        for (String invalid : List.of("name: [", "name: first\nname: second\n")) {
            try {
                mapper.readTree(invalid);
                throw new AssertionError("Invalid or duplicate mapping was accepted");
            } catch (JsonProcessingException expected) {
            }
        }
        boolean anchor = false;
        boolean alias = false;
        try (YAMLParser parser = factory.createParser("first: &ref {value: 1}\nsecond: *ref\n")) {
            while (parser.nextToken() != null) {
                anchor |= parser.getObjectId() != null;
                alias |= parser.isCurrentAlias();
            }
        }
        boolean tag = false;
        try (YAMLParser parser = factory.createParser("value: !!str 42\n")) {
            while (parser.nextToken() != null) {
                tag |= parser.getTypeId() != null;
            }
        }
        int documents = 0;
        try (YAMLParser parser = factory.createParser("---\nvalue: 1\n---\nvalue: 2\n")) {
            while (parser.nextToken() != null) {
                if (parser.currentToken() == JsonToken.START_OBJECT) {
                    documents++;
                    parser.skipChildren();
                }
            }
        }
        if (!anchor || !alias || !tag || documents != 2) {
            throw new AssertionError("Object graph metadata or document boundaries");
        }
        if (ServiceLoader.load(JsonFactory.class).stream().noneMatch(provider -> provider.type() == YAMLFactory.class)
                || ServiceLoader.load(ObjectCodec.class).stream().noneMatch(provider -> provider.type() == YAMLMapper.class)) {
            throw new AssertionError("YAML service providers");
        }
        if (!"2.21.5".equals(factory.version().toString())) {
            throw new AssertionError("Generated version");
        }
        System.out.println("YAML round trip, strict parsing, graph metadata, document boundaries and service discovery passed");
    }
}
