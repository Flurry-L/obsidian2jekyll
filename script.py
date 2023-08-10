import os
import sys
import shutil
import re

def process_markdown_file(src_path, dest_path, markdown_file):
    with open(os.path.join(src_path, markdown_file), 'r', encoding='utf-8') as f:
        content = f.read()

    date_match = re.search(r'date:\s*(\d{4}-\d{2}-\d{2})', content)
    if date_match:
        date = date_match.group(1)
    else:
        date = 'unknown'

    def image_repl(match_obj):
        image_path = match_obj.group(1)
        image_name = os.path.basename(image_path)
        new_image_path = f'/assets/{image_name}'
        image_path_full = os.path.abspath(os.path.join(src_path, image_path))
        dest_image_path = os.path.abspath(os.path.join(dest_path, 'assets', image_name))
        os.makedirs(os.path.dirname(dest_image_path), exist_ok=True)
        shutil.copy2(image_path_full, dest_image_path)

        return f'![]({new_image_path})'

    def link_repl(match_obj):
        link_text = match_obj.group(1)
        link_target = link_text.replace(" ", "-")
        link_target = os.path.join('../', link_target)
        return f'[{link_text}]({link_target})'

    content = re.sub(r'!\[\[(.*?)\]\]', image_repl, content)
    content = re.sub(r'\[\[(.*?)\]\]', link_repl, content)


    file_name = os.path.basename(markdown_file)
    file_name = f'{date}-{file_name}'
    dest_path = os.path.join(dest_path, "_posts", file_name)
    print("converting: ", dest_path)
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    with open(dest_path, 'w', encoding='utf-8') as f:
        f.write(content)

def main():
    if len(sys.argv) != 3:
        print("Usage: python script.py <src_directory> <dest_directory>")
        return

    src_path = sys.argv[1]
    dest_path = sys.argv[2]
    

    for root, dirs, files in os.walk(src_path):
        relative_dir = os.path.relpath(root, src_path)
        #dest_dir = os.path.join(dest_path, relative_dir)
        #os.makedirs(dest_dir, exist_ok=True)

        for file in files:
            if file.endswith('.md'):
                process_markdown_file(root, dest_path, file)

if __name__ == "__main__":
    main()
