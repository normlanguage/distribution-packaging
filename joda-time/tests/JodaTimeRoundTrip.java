import org.joda.time.DateTime;
import org.joda.time.DateTimeZone;
import org.joda.time.LocalDate;

public final class JodaTimeRoundTrip {
  public static void main(String[] args) {
    DateTime before = new DateTime(2026, 3, 8, 1, 30, DateTimeZone.forID("America/New_York"));
    DateTime after = before.plusHours(1);
    if (after.getHourOfDay() != 3 || after.getZone().getOffset(after) != -14400000) {
      throw new AssertionError(after);
    }
    if (DateTime.parse(after.toString()).getMillis() != after.getMillis()) {
      throw new AssertionError("Date round trip failed");
    }
    if (!new LocalDate(2024, 2, 29).plusYears(1).equals(new LocalDate(2025, 2, 28))) {
      throw new AssertionError("Leap year arithmetic failed");
    }
    try {
      LocalDate.parse("2026-02-30");
      throw new AssertionError("Invalid date was accepted");
    } catch (IllegalArgumentException expected) {
      System.out.println("Time zone, round trip, leap year and invalid date checks passed");
    }
  }
}
