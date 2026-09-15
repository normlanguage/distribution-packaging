import ch.randelshofer.fastdoubleparser.JavaDoubleParser;
import ch.randelshofer.fastdoubleparser.ConfigurableDoubleParser;
import ch.randelshofer.fastdoubleparser.JavaBigDecimalParser;
import ch.randelshofer.fastdoubleparser.JavaBigIntegerParser;
import java.math.BigDecimal;
import java.math.BigInteger;
import java.nio.charset.StandardCharsets;

public final class FastDoubleParserCheck {
  public static void main(String[] args) {
    for (String text : new String[]{"0", "-0.0", "1.2345678901234567", "4.9e-324", "1.7976931348623157e308", "0x1.fffffffffffffp1023", "NaN", "-Infinity"}) {
      long expected = Double.doubleToLongBits(Double.parseDouble(text));
      if (expected != Double.doubleToLongBits(JavaDoubleParser.parseDouble(text))) {
        throw new AssertionError(text);
      }
      if (expected != Double.doubleToLongBits(JavaDoubleParser.parseDouble(text.toCharArray()))) {
        throw new AssertionError("Character array: " + text);
      }
      if (expected != Double.doubleToLongBits(JavaDoubleParser.parseDouble(text.getBytes(StandardCharsets.US_ASCII)))) {
        throw new AssertionError("Byte array: " + text);
      }
    }
    String integer = "1234567890".repeat(100);
    if (!new BigInteger(integer).equals(JavaBigIntegerParser.parseBigInteger(integer))) {
      throw new AssertionError("Large integer");
    }
    String decimal = integer + ".123456789e-100";
    if (!new BigDecimal(decimal).equals(JavaBigDecimalParser.parseBigDecimal(decimal))) {
      throw new AssertionError("Large decimal");
    }
    ConfigurableDoubleParser configurable = new ConfigurableDoubleParser();
    if (configurable.parseDouble("\u200e-123.5".getBytes(StandardCharsets.UTF_8)) != -123.5
        || configurable.parseDouble("3.0E\u061c-9".getBytes(StandardCharsets.UTF_8)) != 3e-9) {
      throw new AssertionError("UTF-8 format characters");
    }
    try {
      JavaDoubleParser.parseDouble("1.2.3");
      throw new AssertionError("Invalid number was accepted");
    } catch (NumberFormatException expected) {
      System.out.println("Boundary values, all input forms and invalid input checks passed");
    }
  }
}
