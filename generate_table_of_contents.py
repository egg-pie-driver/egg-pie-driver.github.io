import os
import sys

def generate_table_of_contents(directory):
    toc_lines = []
    md_files = []
    
    # 获取目录下的所有 md 文件
    for filename in os.listdir(directory):
        if filename.endswith('.md') and filename != 'README.md':
            md_files.append(filename)
    
    if md_files:
        # 对 md 文件按文件名进行字典序排序
        md_files.sort()
        
        # 生成链接列表
        for filename in md_files:
            title = os.path.splitext(filename)[0]
            link = f'- [{title}]({filename})\n'
            toc_lines.append(link)
            
        # 在 README.md 文件中生成排序后的目录
        if toc_lines:
            toc_content = '## Table of Contents\n\n' + '\n'.join(toc_lines)
            with open(os.path.join(directory, 'README.md'), 'w+') as readme_file:
                contents = readme_file.read()
                if '## Table of Contents' in contents:
                    contents = contents.split('## Table of Contents')[0]
                readme_file.seek(0)
                readme_file.write(contents + toc_content)
                readme_file.truncate()
                print(f"Generated sorted Table of Contents in README.md")
    else:
        print("No Markdown files found in the directory.")

if __name__ == '__main__':
    path = sys.argv[1]  
    # 使用示例：在 README.md 中生成目录
    generate_table_of_contents(path)
