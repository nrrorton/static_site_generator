import unittest

from textnode import TextNode, TextType, text_node_to_html_node


class TestTextNode(unittest.TestCase):
    
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test2_eq(self):
        node = TextNode("Test text node", TextType.IMAGE, None)
        node2 = TextNode("Test text node", TextType.IMAGE, None)
        self.assertEqual(node, node2)

    def test3_eq(self):
        node = TextNode("Testing text node", TextType.CODE, "www.nickorton.dev")
        node2 = TextNode("Testing text node", TextType.CODE, "www.nickorton.dev")
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("Unequal text node", TextType.ITALIC, None)
        node2 = TextNode("Not equal text node", TextType.ITALIC, None)
        self.assertNotEqual(node, node2)

    def test2_not_eq(self):
        node = TextNode("This is a text node", TextType.TEXT, "www.nick-squared.com")
        node2 = TextNode("This is a text node", TextType.BOLD, "www.nick-squared.com")
        self.assertNotEqual(node, node2)

    def test3_not_eq(self):
        node = TextNode("This is a text node", TextType.TEXT, "www.nick-squared.com")
        node2 = TextNode("This is a text node", TextType.TEXT, "www.nickorton.dev")
        self.assertNotEqual(node, node2)

    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_bold(self):
        node = TextNode("This is a BOLD node", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is a BOLD node")

    def test_link(self):
        node = TextNode("Boot.dev", TextType.LINK, "https://boot.dev")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "Boot.dev")
        self.assertEqual(html_node.props, {"href": "https://boot.dev"})

    def test_image(self):
        node = TextNode("alt text", TextType.IMAGE, "https://example.com/image.png")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.props["src"], "https://example.com/image.png")
        self.assertEqual(html_node.props["alt"], "alt text")


if __name__ == "__main__":
    unittest.main()