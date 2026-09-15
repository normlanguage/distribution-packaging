import org.threeten.bp.LocalDate;
import org.threeten.bp.ZoneId;
import org.threeten.bp.ZonedDateTime;
import org.threeten.bp.format.DateTimeParseException;

public final class ThreeTenRoundTrip {
  public static void main(String[] args) {
    ZonedDateTime before = ZonedDateTime.of(2026, 3, 8, 1, 30, 0, 0, ZoneId.of("America/New_York"));
    ZonedDateTime after = before.plusHours(1);
    if (after.getHour() != 3 || after.getOffset().getTotalSeconds() != -14400) {
      throw new AssertionError(after);
    }
    if (!ZonedDateTime.parse(after.toString()).equals(after)) {
      throw new AssertionError("Zoned date round trip failed");
    }
    try {
      LocalDate.parse("2026-02-30");
      throw new AssertionError("Invalid date was accepted");
    } catch (DateTimeParseException expected) {
      System.out.println("Time zone transition, round trip and invalid date checks passed");
    }
  }
}
