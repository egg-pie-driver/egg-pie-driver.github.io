import sys

from add_audio_tags import add_audio_tags 
from delete_pdf_files import delete_pdf_files 
from remove_string_from_filenames import remove_string_from_filenames 
from generate_table_of_contents import generate_table_of_contents 

def main(path):
    delete_pdf_files(path)
    remove_string_from_filenames(path)
    add_audio_tags(path)
    generate_table_of_contents(path)

path = sys.argv[1]
# 调用函数
main(path)