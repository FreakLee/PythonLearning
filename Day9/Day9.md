# Day9-输入、输出、File及OS

## 输入与输出

### 读取键盘输入
Python 提供了 input() 内置函数从标准输入读入一行文本，默认的标准输入是键盘

``` py
str = input("请输入：")
print("你输入的内容是: "，str)
```

### 输出格式化
在Python中，有几种常用的方式来进行输出格式化，包括使用字符串格式化操作符（%）、使用字符串的format()方法和使用f-string（格式化字符串字面值）。

* 字符串格式化操作符（%）：是一种传统的格式化字符串的方式，它使用特定的占位符来表示要插入的值
    * %s：字符串
    * %d：整数
    * %f：浮点数
    * %r：表示使用repr()函数转换的字符串
* 字符串的format()方法：通过大括号 {} 来指示要插入的值的位置，并提供更灵活的格式化选项
* f-string（格式化字符串字面值）：f-string 是从 Python 3.6 版本开始引入的一种新的字符串格式化方式，它使用以字母 f 开头的字符串字面值，并在大括号 {} 内包含要插入的表达式

``` py
name = "Alice"
age = 25
height = 1.65

print("姓名：%s，年龄：%d，身高：%.2f" % (name, age, height))
# 输出：姓名：Alice，年龄：25，身高：1.65

print("姓名：{}，年龄：{}，身高：{:.2f}".format(name, age, height))
# 输出：姓名：Alice，年龄：25，身高：1.65

print(f"姓名：{name}，年龄：{age}，身高：{height:.2f}")
# 输出：姓名：Alice，年龄：25，身高：1.65
```

### 输出值的方式
* 使用print()函数：Python中常用的输出函数，它可以将值打印到标准输出流（通常是控制台）上
* 使用标准输出流sys.stdout的write()方法：Python的sys模块提供了与解释器相关的功能和变量，其中sys.stdout表示标准输出流。可以使用它的write()方法来输出值
* 使用文件对象的write()方法：在Python中，可以将值写入文件对象的write()方法来实现输出到文件的功能

``` py
name = "Charlie"
age = 35

sys.stdout.write("姓名: ")
sys.stdout.write(name + "\n")
sys.stdout.write("年龄: ")
sys.stdout.write(str(age) + "\n")

# 输出：
# 姓名: Charlie
# 年龄: 35

with open("output.txt", "w") as file:
    name = "Bob"
    age = 30

    file.write("姓名: ")
    file.write(name + "\n")
    file.write("年龄: ")
    file.write(str(age) + "\n")

# 将姓名和年龄写入文件output.txt
```

### str()和repr() 函数

str()
str()函数用于将对象转换为可读性好的字符串表示形式。它返回一个人类可读的字符串，通常用于输出、显示或日志记录等情况。对于大多数内置类型和自定义类，str()函数会调用对象的__str__()方法来获取字符串表示形式。

以下是str()函数的一些特点：
* 返回的字符串不包含任何特殊的转义字符或引号。
* str()函数适用于人类阅读，但可能不适合用于将对象的表示形式传递给eval()函数进行求值。

repr()
repr()函数用于将对象转换为它的官方字符串表示形式。它返回一个可以用来重新创建该对象的字符串，通常包含对象的类型信息和内部结构。对于大多数内置类型和自定义类，repr()函数会调用对象的__repr__()方法来获取它的字符串表示。

以下是repr()函数的一些特点：
* 返回的字符串通常是Python解释器可以接受的，并可以用于创建或重建原始对象。
* 字符串中可能包含特殊字符、引号或转义序列。
* repr()函数通常用于调试、开发和内部表示需求。

``` py
num = 42
print(str(num))   # 输出: 42
print(repr(num))  # 输出: 42

class Person:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Person: {self.name}"

p = Person("Alice")
print(str(p))   # 输出: Person: Alice
print(repr(p))  # 输出: Person('Alice')
```
在上面的示例中，使用str()函数分别将整数对象num和自定义类Person的对象p转换为字符串表示形式；使用repr()函数分别将整数对象num和自定义类Person的对象p转换为解释器易读的形式。

## File
File模块是Python标准库中的模块，用于处理文件的读取、写入和管理。

### open()
open() 是 Python 中用于打开文件的内置函数。它接受一个文件路径作为参数，并返回一个文件对象，可以用于读取、写入或操作文件。
open() 函数的基本语法如下：
``` py
open(filename, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
```
* filename：包含了你要访问的文件名称的字符串值。
* mode：决定了打开文件的模式：只读，写入，追加等。这个参数是非强制的，默认文件访问模式为只读(r)。
* 其他参数：例如 buffering、encoding、errors 等，用于控制文件的缓冲、编码方式和错误处理等。

常见的模式有：
* 'r'：只读模式
* 'w'：写入模式，会覆盖已有内容
* 'a'：追加模式，在文件末尾添加内容
* 'x'：创建模式，创建新文件并写入内容，如果文件已存在则抛出错误
* 'b'：二进制模式
* 't'：文本模式（默认）
* '+'：读写模式。

``` py
# 以只读模式打开文件并读取内容
file = open('output.txt', 'r')  # 打开名为 output.txt 的文件，以只读模式
content = file.read()           # 读取文件内容
print(content)
file.close()                    # 关闭文件

# 以写入模式打开文件并写入内容
file = open('output.txt', 'w')  # 打开名为 output.txt 的文件，以写入模式
file.write('Hello, world!\n')   # 写入内容到文件
file.close()                    # 关闭文件

# 以追加模式打开文件并在文件末尾添加内容
file = open('output.txt', 'a')  # 打开名为 output.txt 的文件，以追加模式
file.write('Appending new content.\n')  # 在文件末尾添加内容
file.close()                    # 关闭文件

# 使用上下文管理器（with语句）自动处理文件的打开和关闭
with open('output.txt', 'r') as file:  # 打开名为 output.txt 的文件，以只读模式
    content = file.read()               # 读取文件内容
    print(content)                      # 输出文件内容，不需要手动关闭文件
```

### 其它常见文件操作方法
* read(size=-1)
    * 从文件中读取指定大小的数据，如果不指定大小，则读取整个文件
    * 返回一个字符串（文本模式）或字节对象（二进制模式）

* readline(size=-1)：
    * 从文件中读取一行数据，如果不指定大小，则读取整行
    * 返回一个字符串（文本模式）或字节对象（二进制模式）

* readlines()：
    * 从文件中读取所有行，并将每一行作为一个字符串放入列表中返回

* write(string)：
    * 将字符串或字节对象写入文件

* writelines(lines)：
    * 将一个包含多个字符串的列表写入文件，每个字符串表示一行数据
    
* seek(offset[, whence])：
    * 在文件中移动文件指针到指定的位置
    * offset：偏移量，表示要移动的字节数
    * whence：可选参数，指定偏移量的参考位置。默认为0，表示从文件开头计算偏移量；1 表示从当前位置计算偏移量；2 表示从文件末尾计算偏移量

``` py
# read()
with open('output.txt', 'r') as file:
    content = file.read()  # 读取整个文件内容
    print(content)

# readline()
with open('output.txt', 'r') as file:
    line = file.readline()  # 读取一行数据
    print(line)

# readlines()
with open('output.txt', 'r') as file:
    lines = file.readlines()  # 读取所有行数据
    print(lines)

# write()
with open('output.txt', 'w') as file:
    file.write('Hello, world!')  # 写入内容到文件

# writelines()
with open('output.txt', 'w') as file:
    lines = ['Line 1\n', 'Line 2\n', 'Line 3\n']
    file.writelines(lines)  # 写入多行数据到文件

# seek()
with open('output.txt', 'r') as file:
    file.seek(10)  # 将文件指针移动到偏移量为10的位置
```

## OS
OS模块是Python标准库中的模块，用于与操作系统进行交互，提供了许多与操作系统相关的功能和方法。

### 文件和目录操作
OS模块提供了一系列方法来进行文件和目录的操作，例如：
* os.getcwd()：获取当前工作目录的路径
* os.chdir(path)：改变当前工作目录到指定路径
* os.listdir(path)：返回指定目录下的文件和目录列表
* os.mkdir(path)：创建新目录
* os.rmdir(path)：删除指定目录

``` py
import os

current_dir = os.getcwd()  # 获取当前工作目录
# print(current_dir)

# os.chdir("/Users/..../PythonLearning/Day8")  # 改变当前工作目录

files = os.listdir(".")  # 获取当前目录下的文件列表
# print(files)

os.mkdir("new_directory")  # 创建新目录
os.rmdir("new_directory")  # 删除目录
```

### 文件和路径操作
OS模块还提供了一些方法来进行文件和路径的操作，例如：
* os.path.exists(path)：检查指定路径是否存在
* os.path.isfile(path)：检查指定路径是否为文件
* os.path.isdir(path)：检查指定路径是否为目录
* os.path.join(path, *paths)：将多个路径组合成一个完整路径
``` py
path = "/path/to/file.txt"

if os.path.exists(path):
    print("文件存在")
else:
    print("文件不存在")

if os.path.isfile(path):
    print("这是一个文件")
else:
    print("这不是一个文件")

if os.path.isdir(path):
    print("这是一个目录")
else:
    print("这不是一个目录")

full_path = os.path.join("/path/to", "file.txt")
print(full_path)
```

### 执行系统命令
OS模块还提供了os.system()方法，用于执行系统命令。
``` py
os.system("ls -l")  # 列出当前目录下的文件和目录
```
需要注意的是，os.system()方法执行系统命令时，会阻塞当前进程，直到命令执行完成。

除了上述介绍的功能和方法外，OS模块还提供了许多其他的功能，例如环境变量操作、进程管理、文件权限等。

