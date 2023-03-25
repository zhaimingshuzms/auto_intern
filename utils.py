import os
def delete_files_in_dir(dir_path):
    for i in os.listdir(dir_path):
        path = os.path.join(dir_path, i)
        os.remove(path)

def check_dir(dir_path):
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)