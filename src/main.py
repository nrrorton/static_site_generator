from textnode import TextNode, TextType

def main():

    node = TextNode("This is test anchor text", TextType.LINK, "https://www.boot.dev")
    print(node)

if __name__ == "__main__":
    main()