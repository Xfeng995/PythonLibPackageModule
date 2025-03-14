# __init__.py的几个主要用途

__init__.py的几个主要用途:
1 声明包的存在:让Python识别一个文件夹为包。
2 定制导入行为:通过在__init__.py中导入子模块或子包,简化用户的使用体验。
3 初始化代码执行:可以在导入包时自动执行某些初始化操作。

# 控制导入行为，简化模块的使用
# __init__.py
~~~
from .module_a import function_a
from .module_b import function_b
~~~
这样做的好处是,在main.py中,我们可以更加简洁地导入模块的功能:
# main.py
~~~
from my_package import function_a, function_b

function_a()
function_b()

from .module_a import function_a
from .module_b import function_b
~~~
# 执行初始化代码

假设我们有个需求,每次导入包时都要初始化一个数据库连接,可以在__init__.py中加入初始化代码:
# __init__.py
~~~
def init_db():
    print("数据库初始化")

init_db()
~~~
在包被导入时,任何必要的初始化操作都可以通过__init__.py自动完成.

def init_db():
    print("数据库初始化")
    
init_db()

