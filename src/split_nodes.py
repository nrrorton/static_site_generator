import re

from textnode import *
from blocktype import *


def extract_markdown_images(text):
    #Searching for pattern of alt text in ![] followed by URL in ()
    matches = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches


def extract_markdown_links(text):
    #Searching for pattern of anchor text in [] followed by URL in ()
    matches = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    node_list = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            node_list.append(node)
            continue
        else:
            sections = node.text.split(delimiter)
            if len(sections) % 2 == 0:
                raise Exception("Both an opening and closing delimiter are required")
            split_nodes = []
            for i in range(len(sections)):
                if sections[i] == "":
                    continue
                if i % 2 == 0:
                    split_nodes.append(TextNode(sections[i], TextType.TEXT))
                else:
                    split_nodes.append(TextNode(sections[i], text_type))
            node_list.extend(split_nodes)

    return node_list


def split_nodes_image(old_nodes):
    node_list = []
    
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            node_list.append(node)
            continue

        original_text = node.text
        alt_text_and_url = extract_markdown_images(original_text)
        if not alt_text_and_url:
            node_list.append(node)
            continue

        for alt, url in alt_text_and_url:
            sections = original_text.split(f"![{alt}]({url})", 1)
            before = sections[0]
            after = sections[1]
            if before != "":
                node_list.append(TextNode(before, TextType.TEXT))
            node_list.append(TextNode(alt, TextType.IMAGE, url))
            original_text = after

        if original_text != "":
            node_list.append(TextNode(original_text, TextType.TEXT))

    return node_list


def split_nodes_link(old_nodes):
    node_list = []
    
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            node_list.append(node)
            continue

        original_text = node.text
        alt_text_and_url = extract_markdown_links(original_text)
        if not alt_text_and_url:
            node_list.append(node)
            continue
        
        for alt, url in alt_text_and_url:
            sections = original_text.split(f"[{alt}]({url})", 1)
            before = sections[0]
            after = sections[1]
            if before != "":
                node_list.append(TextNode(before, TextType.TEXT))
            node_list.append(TextNode(alt, TextType.LINK, url))
            original_text = after

        if original_text != "":
            node_list.append(TextNode(original_text, TextType.TEXT))

    return node_list


def text_to_textnodes(text):
    node_list = []
    nodes = TextNode(text, TextType.TEXT)
    node_list.append(nodes)
    node_list = split_nodes_delimiter(node_list, "**", TextType.BOLD)
    node_list = split_nodes_delimiter(node_list, "_", TextType.ITALIC)
    node_list = split_nodes_delimiter(node_list, "`", TextType.CODE)
    node_list = split_nodes_image(node_list)
    node_list = split_nodes_link(node_list)

    return node_list


def markdown_to_blocks(markdown):
    blocks = []
    sep_blocks = markdown.strip().split('\n\n')
    for block in sep_blocks:
        if not block:
            continue
        blocks.append(block)
    return blocks


def count_char(block_text):
    count = 0
    for char in block_text:
        if char == '#':
            count += 1
        else:
            break
    return count


def text_to_children(text):
    nodes = []
    textnodes = text_to_textnodes(text)
    for node in textnodes:
        html_node = text_node_to_html_node(node)
        nodes.append(html_node)
    return nodes


def markdown_to_html_node(markdown):
    parent_list = []
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        lines = block.split('\n')
        block_type = block_to_block_type(block)

        if block_type == BlockType.HEADING:
            num_hash = count_char(block.text)
            text = block[num_hash+1:]
            html_nodes = text_to_children(text)
            parent = ParentNode(f"h{num_hash}", html_nodes)
            parent_list.append(parent)

        if block_type == BlockType.CODE:

            text_node = TextNode(block[4:-3], TextType.TEXT)
            html_node = [text_node_to_html_node(text_node)]
            parent = [ParentNode("code", html_node)]
            parents = ParentNode("pre", parent)
            parent_list.append(parents)

        if block_type == BlockType.QUOTE:
            cleand_lines = []
            for line in lines:
                cleaned_lines.append(line[1:].strip())
            text = " ".join(cleaned_lines)
            html_nodes = text_to_children(text)
            parent = ParentNode("blockquote", html_nodes)
            parent_list.append(parent)

        if block_type == BlockType.UNORDERED_LIST:
            list_items = []
            for line in lines:
                item_text = line[2:]
                item_children = text_to_children(item_text)
                list_items.append(ParentNode("li", item_children))
            final_list_parent = ParentNode("ul", list_items)
            parent_list.append(final_list_parent)

        if block_type == BlockType.ORDERED_LIST:
            list_items = []
            for line in lines:
                position = line.find(' ')
                item_text = line[position + 2:]
                item_children = text_to_children(item_text)
                list_items.append(ParentNode("li", item_children))
            final_list_parent = ParentNode("ol", list_items)
            parent_list.append(final_list_parent)

        if block_type == BlockType.PARAGRAPH:
            
            text = " ".join(lines)
            html_nodes = text_to_children(text)
            parent = ParentNode("p", html_nodes)
            parent_list.append(parent)

    return ParentNode("div", parent_list)
