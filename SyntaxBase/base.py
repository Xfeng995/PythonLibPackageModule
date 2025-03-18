# Python 以其简洁易懂的语法和强大的功能，成为了编程入门和实际应用的热门选择。本文将介绍 20 个 Python 中常用的经典编程案例，希望能帮助大家更好地学习Python。
# 一、基础语法与数据类型打印输出：最基础的程序。
print("Hello, World!")
# 变量与数据类型： 演示变量的定义和不同数据类型的使用。
name = "Alice"  
# 字符串
age = 30        
# 整数
height = 1.75   
# 浮点数
is_student = False 
# 布尔值
print(f"Name: {name}, Age: {age}, Height: {height}, Is student: {is_student}")
# 运算符： 演示算术、比较和逻辑运算符的使用。
x = 10
y = 3
print(f"x + y = {x + y}")  # 加法
print(f"x - y = {x - y}")  # 减法
print(f"x * y = {x * y}")  # 乘法
print(f"x / y = {x / y}")  # 除法
print(f"x // y = {x // y}") # 整除
print(f"x % y = {x % y}")  # 取余
print(f"x > y is {x > y}") # 大于
print(f"x == y is {x==y}") # 等于
# 条件语句： 演示 if-elif-else 语句的使用。
score = 85
if score >= 90:
    print("优秀")
elif score >= 80:
    print("良好")
elif score >= 60:
    print("及格")
else:
    print("不及格")
# 循环语句： 演示 for 和 while 循环的使用。
# for 循环
for i in range(5):
    print(i)

# while 循环
i = 0
while i < 5:
    print(i)
    i += 1

# 二、数据结构列表： 演示列表的创建、访问和修改。
fruits = ["apple", "banana", "orange"]
print(fruits[0])     # 访问第一个元素
fruits.append("grape") # 添加元素
print(fruits)
# 元组： 演示元组的创建和访问（元组不可修改）。
point = (10, 20)
print(point[0])
# 字典： 演示字典的创建、访问和修改。
person = {"name": "Alice", "age": 30}
print(person["name"])
person["city"] = "Beijing"
print(person)
# 集合： 演示集合的创建和基本操作（去重）。
numbers = [1, 2, 2, 3, 3, 3]
unique_numbers = set(numbers)
print(unique_numbers)

# 三、函数与模块函数定义与调用： 演示如何定义和调用函数。
def greet(name):
    print(f"Hello, {name}!")

greet("Bob")
# 模块导入： 演示如何导入和使用模块。
import math
print(math.sqrt(16))

# 四、文件操作文件读取： 演示如何读取文件内容。
with open("example.txt", "r") as f:
    content = f.read()
    print(content)
# 文件写入： 演示如何向文件写入内容。
with open("output.txt", "w") as f:
    f.write("Hello, file!")

# 五、异常处理try-except 语句： 演示如何处理异常。
try:
    result = 10 / 0
except ZeroDivisionError:
    print("除数不能为 0")

# 六、面向对象编程类与对象： 演示如何定义类和创建对象。
class Dog:
    def __init__(self, name):
        self.name = name
    def bark(self):
        print("Woof!")

my_dog = Dog("Buddy")
my_dog.bark()

# 七、常用模块应用字符串操作： 演示常用的字符串方法。
text = "Hello, Python!"
print(text.lower()) 
# 转换为小写
print(text.replace("Python", "World")) 
# 替换
# 日期时间处理： 演示 datetime 模块的使用。
import datetime
now = datetime.datetime.now()
print(now)
# 正则表达式： 演示 re 模块的使用。
import re
text = "This is a test string."
match = re.search(r"test", text)
if match:
    print("找到匹配")
# 网络请求： 使用 requests 库发送网络请求。
import requests
response = requests.get("https://www.baidu.com")
print(response.status_code)
# JSON 处理： 使用 json 模块处理 JSON 数据。
import json
data = {"name": "Alice", "age": 30}
json_str = json.dumps(data)
print(json_str)
data_back = json.loads(json_str)
print(data_back)