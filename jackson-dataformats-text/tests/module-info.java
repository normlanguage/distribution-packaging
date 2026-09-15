module check.jackson.yaml {
    requires com.fasterxml.jackson.core;
    requires com.fasterxml.jackson.databind;
    requires com.fasterxml.jackson.dataformat.yaml;
    uses com.fasterxml.jackson.core.JsonFactory;
    uses com.fasterxml.jackson.core.ObjectCodec;
    opens check to com.fasterxml.jackson.databind;
}
