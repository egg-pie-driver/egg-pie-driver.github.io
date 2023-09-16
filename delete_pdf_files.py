import os
import sys

def delete_pdf_files(directory):
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        
        if os.path.isfile(file_path) and filename.endswith(".pdf"):
            os.remove(file_path)
            
        elif os.path.isdir(file_path):
            delete_pdf_files(file_path)

if __name__ == '__main__':
    path = sys.argv[1]
    # 调用函数
    delete_pdf_files(path)
