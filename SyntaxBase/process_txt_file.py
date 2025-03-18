# Python处理文本的优势主要体现在其简洁性、功能强大和灵活性。具体来说，Python提供了丰富的库和工具，使得对文件的读写、处理变得轻而易举。简洁的文件操作接口Python通过内置的open()函数，可以方便地打开文件进行读取或写入。例如，使用open('example.txt', 'r')可以快速打开一个文件进行读取。使用上下文管理器（with语句），可在操作完成后自动关闭文件，避免资源泄露。灵活的文件类型处理Python不仅支持文本文件的处理，还能处理二进制文件、JSON、XML等多种类型的文件，这得益于其丰富的标准库和第三方库。跨平台兼容性Python的文件处理功能在不同的操作系统上（如Windows、macOS、Linux）都能无缝运行，这为跨平台应用程序的开发提供了极大的便利。为了更直观了解Python处理文本的优势，本文给出25个Python常用的案例。打开文件并读取内容# 打开文件并读取内容
with open('example.txt', 'r') as file:
    content = file.read()
print(content)

# 写入文件
with open('example.txt', 'w') as file:
    file.write('Hello, World!')

# 追加内容到文件
with open('example.txt', 'a') as file:
    file.write('New line')

# 读取文件的某一行
with open('example.txt', 'r') as file:
    line = file.readlines()[0]
print(line)

# 逐行读取文件
with open('example.txt', 'r') as file:
    for line in file:
        print(line.strip())

# 使用fileinput模块修改文件内容
import fileinput

# 使用fileinput模块修改文件内容
for line in fileinput.input('example.txt', inplace=True):
    print(line.replace('old_text', 'new_text'), end='')

# 复制文件
with open('example.txt', 'r') as source, open('copy.txt', 'w') as destination:
    destination.write(source.read())

# 移动文件
import os

os.rename('example.txt', 'moved_example.txt')

# 删除文件
import os

os.remove('example.txt')

# 重命名文件
import os

os.rename('example.txt', 'renamed_example.txt')

# 创建文件夹
import os

os.mkdir('new_folder')

# 删除文件夹
import os

os.rmdir('new_folder')

# 遍历文件夹中的所有文件
import os

for file in os.listdir('.'):
    print(file)

# 获取文件大小
import os

file_size = os.path.getsize('example.txt')
print(file_size)

# 检查文件是否存在
import os

if os.path.exists('example.txt'):
    print("文件存在")
else:
    print("文件不存在")

# 读取文件并去除空格
with open('example.txt', 'r') as file:
    content = file.read().strip()
print(content)

# 读取文件并按行分割
with open('example.txt', 'r') as file:
    lines = file.read().splitlines()
print(lines)

# 读取文件并统计行数
with open('example.txt', 'r') as file:
    line_count = sum(1 for line in file)
print(line_count)

# 读取文件并查找特定文本
with open('example.txt', 'r') as file:
    if 'target_text' in file.read():
        print("找到目标文本")
    else:
        print("未找到目标文本")

# 将文件内容转换为列表
with open('example.txt', 'r') as file:
    content_list = file.read().split()
print(content_list)

# 将文件内容转换为字典
with open('example.txt', 'r') as file:
    content_dict = dict(line.split() for line in file)
print(content_dict)

# 写入多行内容到文件
with open('example.txt', 'w') as file:
    file.write('Line 1
Line 2
Line 3')

# 使用pathlib模块复制文件
from pathlib import Path

source = Path('example.txt')
destination = Path('copy.txt')
source.replace(destination)

# 使用pathlib模块移动文件
from pathlib import Path

file = Path('example.txt')
file.rename('moved_example.txt')

# 使用pathlib模块创建和删除文件夹
from pathlib import Path

# 创建文件夹
new_folder = Path('new_folder')
new_folder.mkdir()

# 删除文件夹
new_folder.rmdir()