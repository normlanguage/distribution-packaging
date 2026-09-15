import java.time.LocalDate;
import org.joda.convert.FromString;
import org.joda.convert.StringConvert;
import org.joda.convert.ToString;

public final class JodaConvertRoundTrip {
  public static void main(String[] args) throws Exception {
    for (String name : new String[]{"org.threeten.bp.LocalDate", "com.google.common.reflect.TypeToken"}) {
      try {
        Class.forName(name);
        throw new AssertionError("Optional dependency unexpectedly present: " + name);
      } catch (ClassNotFoundException expected) {
      }
    }
    LocalDate date = LocalDate.of(2026, 9, 15);
    String text = StringConvert.INSTANCE.convertToString(date);
    if (!date.equals(StringConvert.INSTANCE.convertFromString(LocalDate.class, text))) {
      throw new AssertionError("Standard date round trip failed");
    }
    Identifier value = StringConvert.INSTANCE.convertFromString(Identifier.class, "norm-42");
    if (!"norm-42".equals(StringConvert.INSTANCE.convertToString(value))) {
      throw new AssertionError("Annotated type round trip failed");
    }
    System.out.println("Standard and annotated conversions passed without optional dependencies");
  }

  public static final class Identifier {
    private final String value;

    private Identifier(String value) {
      this.value = value;
    }

    @FromString
    public static Identifier parse(String value) {
      return new Identifier(value);
    }

    @ToString
    public String encode() {
      return value;
    }
  }
}
