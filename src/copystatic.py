import os
import shutil
from split_nodes import *
from htmlnode import *

def delete_and_mkdir(dst):
    if os.path.exists(dst):
        shutil.rmtree(dst)
    os.mkdir(dst)


def copy_source_to_destination(src, dst):
    if not os.path.exists(dst):
        os.mkdir(dst)
        
    items = os.listdir(src)
    for item in items:
        src_item = os.path.join(src, item)
        dst_item = os.path.join(dst, item)

        if os.path.isfile(src_item):
            shutil.copy(src_item, dst_item)
        else:
            os.mkdir(dst_item)
            copy_source_to_destination(src_item, dst_item)
    

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    with open(from_path) as f:
        md = f.read()
    with open(template_path) as t:
        tmp = t.read()
        
    html_string = markdown_to_html_node(md).to_html()
    title = extract_title(md)

    page_with_title = tmp.replace("{{ Title }}", title)
    final_html = page_with_title.replace("{{ Content }}", html_string)

    dirpath = os.path.dirname(dest_path)
    if dirpath != "":
        os.makedirs(dirpath, exist_ok=True)

    with open(dest_path, "w") as d:
        d.write(final_html)
    
    