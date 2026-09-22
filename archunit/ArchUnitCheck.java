import static com.tngtech.archunit.lang.syntax.ArchRuleDefinition.classes;

import com.tngtech.archunit.core.importer.ClassFileImporter;

public final class ArchUnitCheck {
  public static final class SampleType {}

  public static void main(String[] args) {
    var imported = new ClassFileImporter().importClasses(SampleType.class);
    classes().should().haveSimpleNameStartingWith("Sample").check(imported);
    if (!imported.get(SampleType.class).getName().equals(SampleType.class.getName())) {
      throw new AssertionError(imported);
    }
    System.out.println("ArchUnit installed API passed");
  }
}
