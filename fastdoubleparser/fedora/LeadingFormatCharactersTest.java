package ch.randelshofer.fastdoubleparser;

import java.nio.charset.StandardCharsets;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertThrows;

public class LeadingFormatCharactersTest {
    @Test
    public void parsesUtf8ExponentFormatCharacters() {
        ConfigurableDoubleParser parser = new ConfigurableDoubleParser();
        for (String prefix : new String[]{"\u061c", "\u200e", "\u200f"}) {
            String input = "3.00E" + prefix + "-9";
            assertEquals(3e-9, parser.parseDouble(input));
            assertEquals(3e-9, parser.parseDouble(input.getBytes(StandardCharsets.UTF_8)));
        }
    }

    @Test
    public void parsesUtf8FormatPrefixesAndSlices() {
        ConfigurableDoubleParser parser = new ConfigurableDoubleParser();
        for (String prefix : new String[]{"\u061c", "\u200e", "\u200f", "\u200e\u200f"}) {
            for (String number : new String[]{"123.5", "-123.5", "Infinity", "-Infinity", "NaN"}) {
                double expected = Double.parseDouble(number);
                String input = prefix + number;
                assertEquals(expected, parser.parseDouble(input));
                assertEquals(expected, parser.parseDouble(input.toCharArray()));
                assertEquals(expected, parser.parseDouble(input.getBytes(StandardCharsets.UTF_8)));
                byte[] wrapped = ("x" + input + "y").getBytes(StandardCharsets.UTF_8);
                assertEquals(expected, parser.parseDouble(wrapped, 1, wrapped.length - 2));
            }
        }
        assertThrows(IllegalArgumentException.class, () -> parser.parseDouble(new byte[]{(byte) 0xe2, (byte) 0x80}));
        assertThrows(IllegalArgumentException.class, () -> parser.parseDouble(new byte[]{1}, -1, 1));
    }
}
