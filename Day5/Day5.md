# Day5-推导式、函数、迭代器与生成器

## 推导式
Python 推导式是一种独特的数据处理方式，可从一个数据序列构建另一个新的数据序列的结构体。列表、字典、集合和元组都支持推导式

* 列表推导式：[out_exp_res for out_exp in input_list if condition]，if语句可选
* 字典推导式：{key_expr: value_expr for value in collection if condition}
* 集合推导式：{expression for item in Sequence if conditional}
* 元组推导式：(expression for item in Sequence if conditional)，元组推导式返回的结果是一个生成器对象

``` py
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
print(tuple(a)) #(1, 2, 3, 4, 5, 6, 7, 8, 9)
```

## 函数
### 函数定义
* 以 def 关键词开头，后接函数标识符名称和圆括号 ()，圆括号之间可以用于定义参数
* 函数内容以冒号 : 起始，并且缩进
* return [表达式] 结束函数，选择性地返回一个值给调用方，不带表达式的 return 相当于返回 None
* 函数或方法的参数列表不需要显式地声明参数类型。变量的类型是在运行时动态推断的，而不是在编译时静态确定的。Python 中的函数或方法可以接受任意类型的参数
* 在Python中，变量和函数的类型注释（Type Annotations）只是提供了一种可选的方式来说明变量和函数的参数类型和返回值类型，它们并不会影响程序的执行。这意味着，即使在定义函数时指定了参数类型和返回值类型，Python解释器在执行时也不会检查它们是否正确

### 函数参数
* 必需参数：须以正确的顺序传入函数。调用时的数量必须和声明时的一样
* 默认参数：如果函数调用时没有传递某个参数的值，那么该参数将使用默认值
* 关键字参数：使用参数名和参数值来指定函数参数的值。关键字参数的顺序可以是任意的
* 可变参数：以def functionname([formal_args,] *var_args_tuple):或者def functionname([formal_args,] **var_args_dict):形式传递可变参数。\* 号可以单独出现，单独出现的话，那么\*号后面的参数必须以关键字参数传递
* 可变关键字参数
* 强制位置参数：强制位置参数使用 \/ 来定义，即在参数列表中使用 \/ 将强制位置参数和其他参数分隔开来。强制位置参数只能按照位置传递，不能使用关键字参数传递，这意味着可以在函数定义时明确指定参数的使用方式，而不需要依赖文档或实现细节。强制位置参数只在 Python 3.8 及以上版本中可用。如果需要在早期版本的 Python 中使用强制位置参数，可以使用 inspect 模块中的 Signature 类

### 参数的传递
在Python中，string、tuple、number是不可更改的对象，而list、dict等则是可以修改的对象
* 不可变类型：变量赋值a=5，后再赋值a=10，这里实际是新生成一个int值对象10，再让a指向它，而5被丢弃，不是改变a的值，相当于新生成了a
* 可变类型：变量赋值a=[1,2,3,4]，后再赋值la[2]=5，则是将list la的第三个元素值更改，本la没有动，只是其内部的一部分值被修改了

Python中一切皆对象，严格意义不能说值传递还是引用传递，应该说传不可变对象和传可变对象。Python函数的参数传递：
* 不可变类型：类似 C++的值传递，如整数、字符串、元组。如fun(a)，传递的只是a的值，没有影响a对象本身。如果在fun(a)内部修改a的值，则是新生成一个a的对象
* 可变类型：类似 C++ 的引用传递，如列表，字典。如fun(la)，则是将la真正的传过去，修改后fun外部的la也会受影响

### 函数重载
Python不支持函数重载。在Python中，函数名被视为一个标识符，它只能绑定到一个对象。如果在同一作用域内定义两个同名的函数，后面的定义将覆盖前面的定义。可以通过使用默认参数值和可变参数来实现类似函数重载的效果

### 匿名函数
在 Python 中，匿名函数（Anonymous Function）也称为 lambda 函数，它是一种可以在一行代码内定义的小型函数。匿名函数可以作为参数传递给其他函数，也可以作为返回值返回。lambda 函数的语法：lambda [arg1 [,arg2,.....argn]]:expression
* lambda 函数通常用于定义简单的函数，例如在排序、过滤和映射等操作中使用。如果需要定义复杂的函数，建议使用普通函数来实现，以便提高代码的可读性和可维护性
* lambda 函数只能包含一个表达式，并且该表达式的结果将被作为函数的返回值。这意味着 lambda 函数不能包含赋值语句、控制语句（如 if、for、while 等）或多条语句
* lambda 函数可以访问其定义时所在的作用域，例如可以引用定义 lambda 函数的函数的变量。但是，lambda 函数无法修改其定义时所在的作用域中的变量，因为 lambda 函数的定义不会创建新的作用域。lambda 函数拥有自己的命名空间，且不能访问自己参数列表之外或全局命名空间里的参数
* 匿名函数也可以在其他函数内部定义，这些函数称为嵌套函数。在嵌套函数中定义的 lambda 函数可以访问其外部函数的变量，这被称为闭包
* 虽然 lambda 函数看起来只能写一行，却不等同于 C 或 C++ 的内联函数，内联函数的目的是调用小函数时不占用栈内存从而减少函数调用的开销，提高代码的执行速度

``` py
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
```

## 迭代器
在Python中，迭代器是一个实现了 __iter__() 和 __next__() 方法的对象。__iter__() 方法返回迭代器对象本身，而 __next__() 方法则返回迭代器中的下一个元素，如果没有更多的元素，则抛出 StopIteration 异常
* 迭代器是一个可以记住遍历的位置的对象
* 迭代器有两个基本的方法：iter() 和 next()
* 字符串，列表或元组对象都可用于创建迭代器

``` py
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
```

实际开发中，迭代器非常有用，它们可以让我们在遍历数据时只保留一个元素在内存中，这可以节省内存开销。Python内置函数和模块也使用迭代器来实现。例如，enumerate() 函数返回一个包含每个元素及其索引的迭代器，而文件对象也可以被视为一个迭代器，每次迭代返回文件中的下一行。

## 生成器
生成器是一种特殊的迭代器，它可以通过 yield 语句来实现。当一个函数包含 yield 语句时，该函数返回一个生成器对象，而函数的执行被暂停，直到下一次迭代时再继续执行

``` py
def my_generator(data):
    for item in data:
        yield item * 2

# 使用生成器遍历列表
my_generator_obj = my_generator(my_list)
for item in my_generator_obj:
    print(item)
```
实际开发中，生成器也非常有用，它们可以让我们更方便地编写迭代器。生成器可以使用更少的代码来实现迭代器，并且由于生成器只在需要时才计算下一个元素，因此也可以节省内存开销。Python内置函数和模块也使用生成器来实现。例如，range() 函数就是一个生成器，它只在需要时计算下一个整数。