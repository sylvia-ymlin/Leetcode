
import os
import re

def contains_chinese(text):
    return bool(re.search(r'[\u4e00-\u9fff]', text))

columns = ["AI_Exam", "Group-A", "Group-C"]
files_with_chinese = []

for col in columns:
    if os.path.exists(col):
        for root, dirs, files in os.walk(col):
            for file in files:
                if file.endswith(".py") or file.endswith(".md") or file.endswith(".txt"):
                    filepath = os.path.join(root, file)
                    try:
                        with open(filepath, 'r', encoding='utf-8') as f:
                            content = f.read()
                            if contains_chinese(content):
                                files_with_chinese.append(filepath)
                    except Exception as e:
                        print(f"Error reading {filepath}: {e}")

print(f"Found {len(files_with_chinese)} files with Chinese content.")
for f in files_with_chinese:
    print(f)
