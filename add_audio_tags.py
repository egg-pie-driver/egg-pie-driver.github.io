import os
import sys

def add_audio_tags(directory):
    for filename in os.listdir(directory):
        if filename.endswith('.md'):
            md_filepath = os.path.join(directory, filename)
            audio_filepath = os.path.join(directory, f'{os.path.splitext(filename)[0]}.mp3')
            if os.path.isfile(audio_filepath):
                with open(md_filepath, 'r+') as md_file:
                    contents = md_file.readlines()
                    new_contents = []
                    for line in contents:
                        new_contents.append(line)
                        if line.startswith('# '):
                            title = line.strip('# \n')
                            audio_tag = f"<audio src='./{os.path.basename(audio_filepath)}' controls></audio>\n"
                            new_contents.append(audio_tag)
                    md_file.seek(0)
                    md_file.write(''.join(new_contents))
                    md_file.truncate()
                    print(f"Added audio tag in {md_filepath}")

if __name__ == '__main__':
    path = sys.argv[1]
    # 使用示例：将目录中的所有md文件的标题下面加上audio标签
    add_audio_tags(path)
