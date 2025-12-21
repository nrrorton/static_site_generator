

class HTMLNode():

    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        format_string = ""
        if self.props is None or self.props == {}:
            return format_string
        for key, value in self.props.items():
            format_string += f' {key}="{value}"'
        return format_string

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"

    def __eq__(self, other):
        if not isinstance(other, HTMLNode):
            return False
        return (self.tag == other.tag and self.value == other.value and self.children == other.children and self.props == other.props)


class LeafNode(HTMLNode):

    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value == None:
            raise ValueError
        if self.tag == None:
            return self.value
        if self.props == None:
            return f'<{self.tag}>{self.value}</{self.tag}>'
        else:
            props_line = self.props_to_html()
            return f'<{self.tag}{props_line}>{self.value}</{self.tag}>'
        

class ParentNode(HTMLNode):

    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag == None:
            raise ValueError
        if not self.children:
            raise ValueError("No children implies this is a LeafNode")
        
        children_html = ""
        for child in self.children:
            children_html += child.to_html()

        props_line = self.props_to_html()
        return f'<{self.tag}{props_line}>{children_html}</{self.tag}>'