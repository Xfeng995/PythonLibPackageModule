# 一、字符串操作字符串反转s = "hello"
print(s[::-1])  
# 输出：olleh
# 字符串拼接words = ["Python", "is", "awesome"]
print(" ".join(words))  
# 输出：Python is awesome
# 字符串格式化（f-string）name = "Alice"
age = 25
print(f"{name} is {age} years old.")  
# Python 3.6+
# 分割字符串成列表text = "apple,banana,cherry"
print(text.split(','))  
# 输出：['apple', 'banana', 'cherry']
# 替换字符串内容s = "I like Java"
print(s.replace("Java", "Python"))  
# 输出：I like Python
# 二、列表操作列表去重lst = [1, 2, 2, 3, 3, 3]
unique = list(set(lst))  
# 输出：[1, 2, 3]
# 列表推导式
squares = [x**2 for x in range(5)]  # 输出：[0, 1, 4, 9, 16]
# 过滤列表中的元素numbers = [1, 2, 3, 4, 5]
even = [x for x in numbers if x % 2 == 0]  
# 输出：[2, 4]
# 列表排序（原地修改）
lst = [3, 1, 4, 1, 5]
lst.sort()  
# 输出：[1, 1, 3, 4, 5]
# 合并两个列表
list1 = [1, 2]
list2 = [3, 4]
merged = list1 + list2  
# 输出：[1, 2, 3, 4]
# 三、字典操作合并字典
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3}
merged = {**dict1, **dict2}  
# 输出：{'a': 1, 'b': 2, 'c': 3}
# 字典推导式
squares = {x: x**2 for x in range(5)}  
# {0:0, 1:1, 2:4, 3:9, 4:16}
# 获取字典默认值d = {'a': 1}
value = d.get('b', 0)  
# 若键不存在，返回0
# 遍历字典键值对
for key, value in d.items():
    print(f"{key}: {value}")
# 字典按值排序
d = {'apple': 5, 'banana': 2, 'cherry': 8}
sorted_d = sorted(d.items(), key=lambda x: x[1])  
# 按值升序排列
# 四、文件操作读取文件内容
with open('file.txt', 'r') as f:
    content = f.read()
# 逐行读取文件
with open('file.txt', 'r') as f:
    lines = [line.strip() for line in f]
# 写入文件
with open('output.txt', 'w') as f:
    f.write("Hello, Python!")
# 追加内容到文件
with open('log.txt', 'a') as f:
    f.write("New log entry\n")
# 处理CSV文件
import csv
with open('data.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
# 五、函数与类默认参数函数
def greet(name="World"):
    print(f"Hello, {name}!")
# **可变参数（*args 和 kwargs）
def func(*args, **kwargs):
    print("Args:", args)
    print("Keyword Args:", kwargs)
# Lambda函数
add = lambda x, y: x + y
print(add(3, 5))  
# 输出：8
# 装饰器
def my_decorator(func):
    def wrapper():
        print("Before function")
        func()
        print("After function")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()
# 类的继承
class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        print("Woof!")

dog = Dog()
dog.speak()
# 六、数据处理使用map函数
numbers = [1, 2, 3]
squared = list(map(lambda x: x**2, numbers))  
# 输出：[1, 4, 9]
使用filter函数numbers = [1, 2, 3, 4]
even = list(filter(lambda x: x % 2 == 0, numbers))  
# 输出：[2, 4]
使用zip合并列表names = ["Alice", "Bob"]
ages = [25, 30]
combined = list(zip(names, ages))  
# [('Alice',25), ('Bob',30)]
# 列表展开（扁平化）
nested = [[1, 2], [3, 4]]
flat = [item for sublist in nested for item in sublist]  
# [1,2,3,4]
# 统计元素频率
from collections import Counter
lst = ['a', 'b', 'a', 'c', 'b', 'a']
count = Counter(lst)  
# Counter({'a':3, 'b':2, 'c':1})
# 七、实用技巧交换变量值
a, b = 1, 2
a, b = b, a  
# a=2, b=1
# 链式比较
x = 5
if 0 < x < 10:
    print("Valid")
# 三元表达式
age = 20
status = "Adult" if age >= 18 else "Minor"
# 生成随机数
# import random
print(random.randint(1, 10))  
# 生成1-10之间的整数
# 时间戳转换
import time
timestamp = time.time()  
# 当前时间戳
local_time = time.ctime(timestamp)  
# 转换为可读时间
# 八、高级操作生成器表达式
gen = (x**2 for x in range(5))
for num in gen:
    print(num)  
    # 输出：0,1,4,9,16
# 上下文管理器（自定义）
class MyContextManager:
    def __enter__(self):
        print("Entering context")
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Exiting context")

with MyContextManager():
    print("Inside the context")
# 枚举遍历
fruits = ['apple', 'banana', 'cherry']
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")
# 递归目录遍历
import os
for root, dirs, files in os.walk('/path'):
    print(f"Current directory: {root}")
# 使用collections.defaultdict
from collections import defaultdict
d = defaultdict(int)
d['a'] += 1  
# 默认值为0
# 九、网络与模块发送HTTP请求
import requests
response = requests.get('https://api.example.com/data')
print(response.json())
# 解析JSON
import json
data = '{"name": "Alice", "age": 25}'
obj = json.loads(data)
print(obj['name']) 
# Alice
# 读取环境变量
import os
api_key = os.getenv('API_KEY')
# 命令行参数解析
# import sys
args = sys.argv[1:]  
# 获取命令行参数列表
# 使用argparse模块
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--input', help='Input file')
args = parser.parse_args()
# 十、算法与数学斐波那契数列（生成器）
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

print(list(fibonacci(5)))  
# [0,1,1,2,3]
# 判断质数
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
# 列表元素排列组合
import itertools
lst = [1, 2, 3]
perms = list(itertools.permutations(lst))  
# 所有排列
combs = list(itertools.combinations(lst, 2))  
# 两两组合
# 快速排序
def quicksort(lst):
    if len(lst) <= 1:
        return lst
    pivot = lst[len(lst)//2]
    left = [x for x in lst if x < pivot]
    middle = [x for x in lst if x == pivot]
    right = [x for x in lst if x > pivot]
    return quicksort(left) + middle + quicksort(right)
# 类型提示（Python 3.5+）
def add(a: int, b: int) -> int:
    return a + b