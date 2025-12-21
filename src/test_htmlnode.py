import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):

    child_node1 = HTMLNode(None, "child text")
    child_node2 = HTMLNode(None, "child text")
    child_node3 = HTMLNode("span", "hello")

    def test_eq(self):
        node = HTMLNode("p", "HTMLNode text")
        node2 = HTMLNode("p", "HTMLNode text")
        self.assertEqual(node, node2)

    def test2_eq(self):
        node = HTMLNode("p", "HTMLNode text", [self.child_node1, self.child_node2], {"href": "https://www.nick-squared.com"})
        node2 = HTMLNode("p", "HTMLNode text", [self.child_node1, self.child_node2], {"href": "https://www.nick-squared.com"})
        self.assertEqual(node, node2)

    def test3_eq(self):
        node = HTMLNode("p", "HTMLNode text", [self.child_node1, self.child_node2], {"href": "https://www.nick-squared.com"})
        node2 = HTMLNode("p", "HTMLNode text", [self.child_node1, self.child_node2], {"href": "https://www.nick-squared.com"})
        self.assertEqual(node, node2)

    def test_uneq(self):
        node = HTMLNode("p", "HTMLNode text", [self.child_node1, self.child_node2], {"href": "https://www.nickorton.dev"})
        node2 = HTMLNode("p", "HTMLNode text", [self.child_node1, self.child_node2], {"href": "https://www.nick-squared.com"})
        self.assertNotEqual(node, node2)

    def test2_uneq(self):
        node = HTMLNode("p", "HTMLNode text", [self.child_node1, self.child_node2], {"href": "https://www.nick-squared.com"})
        node2 = HTMLNode("p", "HTMLNode text", [self.child_node1, self.child_node3], {"href": "https://www.nick-squared.com"})
        self.assertNotEqual(node, node2)

    def test3_uneq(self):
        node = HTMLNode("a", "HTMLNode text", [self.child_node1, self.child_node2], {"href": "https://www.nick-squared.com"})
        node2 = HTMLNode("p", "HTMLNode text", [self.child_node1, self.child_node2], {"href": "https://www.nick-squared.com"})
        self.assertNotEqual(node, node2)

    def test_prop_eq(self):
        node = HTMLNode(props={"href": "https://example.com"})
        self.assertEqual(node.props_to_html(), ' href="https://example.com"')

    def test_prop2_eq(self):
        node = HTMLNode(props=None)
        self.assertEqual(node.props_to_html(), "")

    def test_prop3_eq(self):
        node = HTMLNode(props={"href": "https://example.com", "target": "_blank"})
        self.assertEqual(node.props_to_html(), ' href="https://example.com" target="_blank"')

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span><b>grandchild</b></span></div>")

    def test_to_html_with_great_grandchildren(self):
        great_grandchild_node = LeafNode("i", "great_grandchild")
        grandchild_node = ParentNode("b", [great_grandchild_node])
        child_node = ParentNode("p", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><p><b><i>great_grandchild</i></b></p></div>")

    def test_parent_multiple_children(self):
        c1 = LeafNode("span", "one")
        c2 = LeafNode(None, "two")
        c3 = LeafNode("b", "three")
        parent = ParentNode("div", [c1, c2, c3])
        self.assertEqual(parent.to_html(), "<div><span>one</span>two<b>three</b></div>")

    def test_parent_with_props(self):
        child = LeafNode("span", "child")
        parent = ParentNode("div", [child], {"class": "container"})
        self.assertEqual(parent.to_html(), '<div class="container"><span>child</span></div>')

    def test_parent_no_tag_raises(self):
        child = LeafNode("span", "child")
        with self.assertRaises(ValueError):
            ParentNode(None, [child]).to_html()

    def test_parent_no_children_raises(self):
        with self.assertRaises(ValueError):
            ParentNode("div", None).to_html()
    

if __name__ == "__main__":
    unittest.main()