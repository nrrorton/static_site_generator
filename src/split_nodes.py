import re

from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    node_list = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            node_list.append(node)
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

def extract_markdown_images(text):
    #Searching for pattern of alt text in ![] followed by URL in ()
    matches = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches

def extract_markdown_links(text):
    #Searching for pattern of anchor text in [] followed by URL in ()
    matches = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches
