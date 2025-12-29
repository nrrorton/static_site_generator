from copystatic import *

def main():

    public_dir = "public"
    static_dir = "static"

    from_path = "content/index.md"
    template_path = "template.html"
    dest_path = "public/index.html"

    delete_and_mkdir(public_dir)
    copy_source_to_destination(static_dir, public_dir)

    generate_page(from_path, template_path, dest_path)


if __name__ == "__main__":
    main()