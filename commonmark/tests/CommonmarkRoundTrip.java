import org.commonmark.node.Node;
import org.commonmark.parser.Parser;
import org.commonmark.renderer.html.HtmlRenderer;

public final class CommonmarkRoundTrip {
    public static void main(String[] args) {
        Node document = Parser.builder().build().parse("# Norm\n\nHello **world**.\n");
        String html = HtmlRenderer.builder().build().render(document);
        if (!html.equals("<h1>Norm</h1>\n<p>Hello <strong>world</strong>.</p>\n")) {
            throw new AssertionError(html);
        }
        System.out.println("Installed CommonMark parser and HTML renderer passed");
    }
}
