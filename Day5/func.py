
# ---------------推导式-----------------
# 列表推导式
squares = []
squares = [x**2 for x in range(10) if x%2 == 0]
print(squares) #[0, 4, 16, 36, 64]

# 字典推导式
dic = {x: x**2 for x in (1, 3, 5)}
print(dic) #{1: 1, 3: 9, 5: 25}

# 集合推导式
s = {i**2 for i in (1,2,3)}
print(s) #{1, 4, 9}

# 元组推导式
# 可以利用区间、元组、列表、字典和集合等数据类型，快速生成一个满足指定需求的元组
a = (x for x in range(1,10))
print(a) #<generator object <genexpr> at 0x1087fdff0> 返回生成器对象
print(tuple(a))



# ---------------函数-----------------
# 函数定义
#虽然Python的参数及返回值类型不是必须的，但是可以给它指定类型。然而Python解释器并不会强制执行类型检查。所以以下两种方式都可以运行成功
def add(x, y):
    return x + y
"""
def add(x: int, y: int) -> int:
    return x + y
"""

# 函数调用
print(add(1, 2))             # 输出 3
print(add("hello", "world")) # 输出 helloworld
print(add([1, 2], [3, 4]))   # 输出 [1, 2, 3, 4]

# 必需参数
def printme( str ):
   "打印任何传入的字符串"
   print (str)
   return
 
# 调用 printme 函数，不加参数会报错
# TypeError: printme() missing 1 required positional argument: 'str'
# printme()

# 默认参数
def greet(name="world"):
    "默认参数"
    print(f"Hello, {name}!")

greet()         # 输出 Hello, world!
greet("Alice")  # 输出 Hello, Alice!

# 关键字参数
def greet(name, message="Hello"):
    "关键字参数"
    print(f"{message}, {name}!")

greet(name="Alice", message="Hi")  # 输出 Hi, Alice!
greet(message="Hi", name="Alice")  # 输出 Hi, Alice!

# 可变参数

"""
一个星号 ** 的参数会以元组的形式导入
def functionname([formal_args,] *var_args_tuple):
   "函数_文档字符串"
   function_suite
   return [expression]
"""
def add(*args):
    print(f"一个*号参数：{args}")
    result = 0
    for arg in args:
        result += arg
    return result

print(add(1, 2, 3))  # 输出 6
print(add(1, 2, 3, 4, 5))  # 输出 15

"""
两个星号 ** 的参数会以字典的形式导入
def functionname([formal_args,] **var_args_dict):
   "函数_文档字符串"
   function_suite
   return [expression]
"""
def printinfo(arg1, **vardict):
   "打印任何传入的参数"
   print(f"两个*号参数：{vardict}")
 
# 调用printinfo 函数
printinfo(1,a=2,b=3)

# 可变关键字参数
def greet(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

greet(name="Alice", message="Hello")  # 输出 name: Alice, message: Hello
greet(message="Hi", name="Bob")       # 输出 message: Hi, name: Bob

# 强制位置参数
def greet(name, /, greeting='Hello'):
    return f'{greeting}, {name}!'

print(greet('Alice'))               # 输出: Hello, Alice!
print(greet('Bob', 'Hi'))           # 输出: Hi, Bob!
print(greet('Bob', greeting='Hi'))  # 输出: Hi, Bob!
# name 参数是强制位置参数，不能使用关键字参数传递
#print(greet(name='Charlie'))  # 报错: TypeError: greet() got some positional-only arguments passed as keyword arguments: 'name'

# 参数传递

# 传递不可变对象
def change(a):
    print(id(a))   # 指向的是同一个对象
    a=10
    print(id(a))   # 一个新对象
 
a=1
print(id(a)) #id()函数来查看内存地址变化
change(a)

# 传递可变对象
def changeme(mylist):
   "修改传入的列表"
   mylist.append([1,2,3,4])
   print ("函数内取值: ", mylist)
   return
 
# 调用changeme函数
mylist = [10,20,30]
changeme( mylist )
print ("函数外取值: ", mylist)

# 函数重载：Python不支持
def foo(x):
    print("foo(x) is called")

def foo(x, y):
    print("foo(x, y) is called")
# 后面函数会覆盖前一个
foo(1, 2)  # 输出 foo(x, y) is called

def add(x, y=0, z=0):
    "类似函数重载的效果"
    return x + y + z

print(add(1))        # 输出: 1
print(add(1, 2))     # 输出: 3
print(add(1, 2, 3))  # 输出: 6

# 匿名函数
add = lambda x, y: x + y
print(add(2, 3))  # 输出: 5

# 使用 lambda 函数作为参数
fruits = ["Banana","Apple","Pineapple","Orange"]

sorted_fruits = sorted(fruits, key=lambda x: x[1])
print(sorted_fruits)

# 使用普通函数作为参数
def sort_key(fruit):
    "对 fruits 列表进行排序，排序的依据是每个水果的第二个字母"
    return fruit[1]
sorted_fruits = sorted(fruits, key=sort_key)
print(sorted_fruits)


# 嵌套函数
def outer():
    def inner():
        print("Hello, world!")
    inner()
outer()  # 输出 Hello, world!


# 函数作为返回值
def make_adder(x):
    def adder(y):
        return x + y
    return adder

add5 = make_adder(5)
print(add5(3))   # 输出 8


# 函数作为参数
def apply(func, x):
    return func(x)

def double(x):
    return x * 2

result = apply(double, 3)
print(result)  # 输出 6



# ---------------迭代器-----------------
list = [0,1,2,3]
it = iter(list)    # 创建迭代器对象
print (next(it))   # 输出迭代器的下一个元素

# 迭代器对象可以使用常规for语句进行遍历
for x in it:
    print (x)

#自定义迭代器
class MyIterator:
    def __init__(self, data):
        self.index = 0
        self.data = data

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        result = self.data[self.index]
        self.index += 1
        return result

# 使用迭代器遍历列表
my_list = [1, 2, 3]
my_iterator = MyIterator(my_list)
for item in my_iterator:
    print(item)

# ---------------生成器-----------------
def my_generator(data):
    for item in data:
        yield item * 2

# 使用生成器遍历列表
my_generator_obj = my_generator(my_list)
for item in my_generator_obj:
    print(item)