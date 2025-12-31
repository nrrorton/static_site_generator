from copystatic import *
import sys

if len(sys.argv) > 1:
    basepath = sys.argv[1]
else:
    basepath = '/'

def main():

    public_dir = "docs"
    static_dir = "static"

    dir_path_content = "content"
    template_path = "template.html"
    dest_dir_path = "docs"

    delete_and_mkdir(public_dir)
    copy_source_to_destination(static_dir, public_dir)

    generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath)


if __name__ == "__main__":
    main()