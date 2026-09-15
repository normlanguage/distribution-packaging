import java.lang.module.ModuleFinder;
import java.nio.file.Path;

public final class DescribeModules {
    public static void main(String[] args) {
        for (String argument : args) {
            var modules = ModuleFinder.of(Path.of(argument)).findAll();
            if (modules.size() != 1) {
                throw new IllegalArgumentException("Expected one module in " + argument);
            }
            System.out.println(modules.iterator().next().descriptor().name());
        }
    }
}
