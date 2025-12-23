import unittest

from split_nodes import split_nodes_delimiter
from textnode import TextNode, TextType

class TestHTMLNode(unittest.TestCase):

    def test_code_markdown(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(new_nodes, [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT)
        ])

    def test_bold_markdown(self):
        node = TextNode("This is text with a **bold** word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(new_nodes, [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" word", TextType.TEXT)
        ])

    def test_uneven_delimiter(self):
        node = TextNode("This is text with an _uneven delimiter count", TextType.TEXT)
        with self.assertRaises(Exception):
            split_nodes_delimiter([node], "_", TextType.ITALIC)

    def test_unsupported_delimiter(self):
        node = TextNode("This is text with an &unknown& delimiter", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "&", TextType.TEXT)
        self.assertEqual(new_nodes, [
            TextNode("This is text with an ", TextType.TEXT),
            TextNode("unknown", TextType.TEXT),
            TextNode(" delimiter", TextType.TEXT)
        ])

