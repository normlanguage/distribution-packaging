package check;

import com.oracle.truffle.api.dsl.GenerateUncached;
import com.oracle.truffle.api.dsl.GenerateInline;
import com.oracle.truffle.api.dsl.Specialization;
import com.oracle.truffle.api.nodes.Node;

@GenerateUncached
@GenerateInline(false)
public abstract class AddOneNode extends Node {
    public abstract int execute(int value);

    @Specialization
    protected int addOne(int value) {
        return value + 1;
    }
}
