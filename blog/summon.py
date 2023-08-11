import os
import json
import re

# 获取当前目录下的所有 .md 文件
md_files = [file for file in os.listdir() if file.endswith('.md')]

# 存储博客数据的字典，键为分类，值为博客数据列表
blog_data_by_category = {}

# 遍历每个 .md 文件并获取分类、最后一次编辑日期、标题和文件名
for md_file in md_files:
    with open(md_file, 'r', encoding='utf-8') as f:
        content = f.read()
        # 使用正则表达式匹配分类、日期和标题
        category_match = re.search(r'category:\s*(.+)', content)
        date_match = re.search(r'date:\s*([0-9]{4}-[0-9]{2}-[0-9]{2})', content)
        title_match = re.search(r'title:\s*(.+)', content)
        
        if category_match and date_match and title_match:
            category = category_match.group(1)
            date = date_match.group(1)
            title = title_match.group(1)
            slug = md_file.replace('.md', '')
            
            if category not in blog_data_by_category:
                blog_data_by_category[category] = []
            
            blog_data_by_category[category].append({
                'title': title,
                'slug': slug,
                'date': date
            })

# 将博客数据写入 JSON 文件
with open('posts.json', 'w', encoding='utf-8') as json_file:
    json.dump(blog_data_by_category, json_file, indent=2, ensure_ascii=False)

print('JSON data has been written to blog/posts.json')
