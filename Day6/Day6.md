# Day6-模块

## 模块
在 Python 中，模块（module）是指一个包含 Python 代码的文件。模块可以包含变量、函数、类和其他可执行代码，也可以是一个包含多个模块的包，可以在其他 Python 程序中使用 import 语句进行导入，以便在另一个程序中重用代码。在 Python 中，包是一种包含多个模块的目录，其中必须包含一个名为 __init__.py 的文件，以便 Python 将其识别为一个包。可以使用 import 语句来导入包或包中的模块，语法如下：

* import package_name
* import package_name.module_name
* from package_name import module_name
* from package_name.module_name import function_name

### import和from...import
* import语句用于导入一个模块或一个模块中的一个或多个对象
* from...import语句允许从一个模块中导入指定的对象

两者之间的区别：
* 命名冲突：使用import语句导入整个模块时，需要使用模块名.对象名的方式来访问模块中的对象。使用from...import语句时，可以直接使用对象名，但是如果多个模块中都有同名对象，那么可能会导致命名冲突
* 可读性：使用import语句导入整个模块时，可以清楚地知道代码中使用的模块来自哪里。使用from...import语句时，代码中没有明确指出使用的是哪个模块，可能会使代码不够清晰
* 性能：从一个模块中导入一个或多个对象可能比导入整个模块更快，因为只有需要的对象会被加载到内存中。但是，在导入多个对象时，使用from...import语句可能会导致名称冲突和代码可读性问题

### 导入不同模块的方法：
* 使用绝对路径导入模块：如果要使用绝对路径导入下级目录的模块，可以使用 sys.path 列表来添加目录路径，然后再使用 import 语句导入模块
* 使用相对路径导入模块：from .. import module_name，..表示上一级目录

需要注意的地方：
1、相对导入基于当前模块名。因为主模块名是 "\__main__" ，所以 Python 程序的主模块必须始终使用绝对导入。
2、在导入模块时还可以指定别名，以便在代码中更方便地使用。可以使用 as 关键字来指定别名：
- import module_name as mod
- from .. import module_name as mod

### from … import *
把一个模块的所有内容全都导入到当前的命名空间

### __main__属性
__main__ 是一个特殊的属性，用于指示正在执行的模块是否为主模块（也称为顶级脚本）。当 Python 解释器执行一个脚本文件时，会创建一个特殊的模块对象，并将其命名为 __main__，并且执行这个模块中的代码。如果一个模块是作为一个库被导入到其他模块中，那么它的 __name__ 属性就会被设置为该模块的名称，而不是 __main__

### __name__属性
一个模块被另一个程序第一次引入时，其主程序将运行。如果我们想在模块被引入时，模块中的某一程序块不执行，我们可以用__name__属性来使该程序块仅在该模块自身运行时执行

### dir() 函数
内置的函数 dir() 可以找到模块内定义的所有名称。以一个字符串列表的形式返回

### __pycache__目录
\__pycache__ 是 Python 3 中引入的一个目录，用于存储已经编译过的 Python 模块的缓存文件。在 Python 3 中，如果一个模块被导入到另一个模块中，那么 Python 解释器会在 \__pycache__ 目录中缓存编译后的 .pyc 文件，以便下次导入同一模块时可以更快地执行

在 \__pycache__ 目录中，每个缓存文件的名称都由以下三部分组成：
- 模块的名称
- Python 版本号
- 编译器标识符

\__pycache__ 目录是自动生成的，如果你的 Python 程序中没有使用到任何模块，那么该目录就不会被创建。如果你想手动删除 \__pycache__ 目录下的缓存文件，可以使用 python -m compileall 命令来重新编译所有的 Python 模块，或者手动删除缓存文件。

需要注意的是，在 Python 2 中没有 \__pycache__ 目录，而是使用 .pyc 文件和 .pyo 文件来缓存已编译的 Python 模块。在 Python 3 中，.pyc 文件仍然存在，但是它们被存储在 \__pycache__ 目录中。

### 使用第三方模块
利用pip工具安装第三方模块：pip install 模块名

* 可以使用 import 语句检查是否安装了某个第三方模块。如果模块已经安装，那么 import 语句会成功导入该模块；如果模块未安装，则会抛出 ModuleNotFoundError 异常
* 也可以使用 pkg_resources 模块中的 working_set 属性来列出所有已经安装的模块，然后检查某个特定的模块是否存在

### 包、模块冲突问题
* 使用别名
* 修改搜索路径
* 使用虚拟环境：虚拟环境是一种隔离的 Python 运行环境，可以在其中安装指定版本的 Python 和第三方模块，避免不同项目之间出现名称冲突。可以使用 Python 内置的 venv 模块来创建虚拟环境：python -m venv myenv。然后可以在虚拟环境中安装需要的 Python 版本和第三方模块，以避免名称冲突
* 使用包的绝对路径

``` py
import pkg_resources

#import mymodule
from mymodule import work

from SubModules import my_sub_module
# import sys
# sys.path.append('/路径/SubModules')
# import my_sub_module
# 以上两种方式都行

#mymodule.greet('Alice')
work()

my_sub_module.subWork()


# __name__属性：每个模块都有一个__name__属性，当其值是'__main__'时，表明该模块自身在运行，否则是被引入
if __name__ == '__main__':
   print('程序自身在运行')
else:
   print('我来自另一模块')


# 检查是否安装了某个第三方模块
try:
    import requests
except ModuleNotFoundError:
    print('requests module not found')
else:
    print('requests module is installed')

try:
    pkg_resources.get_distribution('requests')
except pkg_resources.DistributionNotFound:
    print('requests module not found')
else:
    print('requests module is installed')
```