
import sys
import os

# ---------------输入/输出-----------------
# 读取键盘输入
# str = input("请输入一段字符")
# print(str)

# 输出格式化
name = "Alice"
age = 25
height = 1.65

print("姓名：%s，年龄：%d，身高：%.2f" % (name, age, height))
# 输出：姓名：Alice，年龄：25，身高：1.65

print("姓名：{}，年龄：{}，身高：{:.2f}".format(name, age, height))
# 输出：姓名：Alice，年龄：25，身高：1.65

print(f"姓名：{name}，年龄：{age}，身高：{height:.2f}")
# 输出：姓名：Alice，年龄：25，身高：1.65


# 几种输出方式：print()、sys.stdout的write()方法、文件对象的write()方法
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


# str()和repr() 函数
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


# ---------------File-----------------
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


# ---------------OS-----------------
# 文件与目录操作
current_dir = os.getcwd()  # 获取当前工作目录
# print(current_dir)

# os.chdir("/Users/..../PythonLearning/Day8")  # 改变当前工作目录

files = os.listdir(".")  # 获取当前目录下的文件列表
# print(files)

os.mkdir("new_directory")  # 创建新目录
os.rmdir("new_directory")  # 删除目录

# 文件和路径操作
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


# 执行系统命令
os.system("ls -l")  # 列出当前目录下的文件和目录