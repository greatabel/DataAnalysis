import os

"""
我有一个工程（下面有html/js/python）但是可能存放在子目录（目录下还有目录），请写一个bash统计各种不同类型文件的行数

"""
# 初始化行数
html_lines = 0
js_lines = 0
python_lines = 0

# 遍历目录
for root, _, files in os.walk("."):
    for file in files:
        file_path = os.path.join(root, file)
        file_ext = os.path.splitext(file)[-1].lower()

        # 根据文件类型统计行数
        if file_ext in (".html", ".js", ".py"):
            with open(file_path, "r", encoding="utf-8") as f:
                lines = len(f.readlines())

            if file_ext == ".html":
                html_lines += lines
            elif file_ext == ".js":
                js_lines += lines
            elif file_ext == ".py":
                python_lines += lines

# 输出结果
print(f"HTML 文件行数: {html_lines}")
print(f"JS 文件行数: {js_lines}")
print(f"Python 文件行数: {python_lines}")
