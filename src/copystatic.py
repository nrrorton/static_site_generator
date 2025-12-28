import os
import shutil

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
    
