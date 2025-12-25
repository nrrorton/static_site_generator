from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"


def block_to_block_type(block_text):
    count = 0
    for char in block_text:
        if char == '#':
            count += 1
        else:
            break

    is_heading = True   
    if count == 0 or count > 6:
        is_heading = False
    if len(block_text) <= count or block_text[count] != ' ':
        is_heading = False
    if is_heading:
        return BlockType.HEADING

    if block_text[0:3] == '```' and block_text[-3:] == '```':
        return BlockType.CODE

    lines = block_text.split('\n')

    is_quote = True
    for line in lines:
        if not line or line[0] != '>':
            is_quote = False
            break
    if is_quote:
        return BlockType.QUOTE

    is_unordered_list = True
    for line in lines:
        if not line or line[0:2] != '- ':
            is_unordered_list = False
            break
    if is_unordered_list:
        return BlockType.UNORDERED_LIST

    is_ordered_list = True
    for index, line in enumerate(lines, start=1):
        if  len(line) < 3 or line[0:3] != f'{index}. ':
            is_ordered_list = False
            break
    if is_ordered_list:
        return BlockType.ORDERED_LIST
    
    return BlockType.PARAGRAPH


block_text = "```This is code'''"
block_type = block_to_block_type(block_text)
print(block_type)