import os
from shutil import copy, rmtree
from textnode import TextNode, TextType
from copystatic import *

def main():

    public_dir = "public"
    static_dir = "static"

    delete_and_mkdir(public_dir)
    copy_source_to_destination(static_dir, public_dir)


if __name__ == "__main__":
    main()