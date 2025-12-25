import unittest

from blocktype import *

class TestTextNode(unittest.TestCase):
    
    def test_heading(self):
        block_text = "#### This is a heading"
        block_type = block_to_block_type(block_text)
        self.assertEqual(block_type, BlockType.HEADING)

    def test_paragraph(self):
        block_text = "This is a paragraph"
        block_type = block_to_block_type(block_text)
        self.assertEqual(block_type, BlockType.PARAGRAPH)

    def test_code(self):
        block_text = "```This is code```"
        block_type = block_to_block_type(block_text)
        self.assertEqual(block_type, BlockType.CODE)

    def test_quote(self):
        block_text = ">quote \n>second quote"
        block_type = block_to_block_type(block_text)
        self.assertEqual(block_type, BlockType.QUOTE)

    def test_unordered_list(self):
        block_text = "- Item 1 \n- Item 2 \n- Item 3"
        block_type = block_to_block_type(block_text)
        self.assertEqual(block_type, BlockType.UNORDERED_LIST)

    def test_ordered_list(self):
        block_text = "1. Item 1 \n2. Item 2 \n3. Item 3"
        block_type = block_to_block_type(block_text)
        self.assertEqual(block_type, BlockType.ORDERED_LIST)