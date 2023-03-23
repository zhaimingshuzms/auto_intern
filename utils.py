import os
def delete_files_in_dir(dir_path):
    for i in os.listdir(dir_path):
        path = os.path.join(dir_path, i)
        os.remove(path)