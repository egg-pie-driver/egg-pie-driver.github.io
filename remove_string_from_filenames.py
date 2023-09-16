import os
import sys

def remove_string_from_filenames(directory):
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        new_filename = filename.replace("【海量资源：666java.com】", "")
        new_file_path = os.path.join(directory, new_filename)
        
        os.rename(file_path, new_file_path)
        if os.path.isdir(new_file_path):
            remove_string_from_filenames(new_file_path)

if __name__ == '__main__':
    path = sys.argv[1]
    # 调用函数
    remove_string_from_filenames(path)
