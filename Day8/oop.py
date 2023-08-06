
from types import MethodType,FunctionType

# ---------------类-----------------
# 类的定义
class MyClass:
    """一个简单的类实例"""
    i = 12345

    def instance_method(self):
        print(f"instance_method, self={self}, self:{id(self)}, self.__class__={self.__class__}")

    @classmethod
    def class_method(cls):
        print(f"class_method, cls:{id(cls)}, cls={cls}")

    @staticmethod
    def static_method():
        print(f"static_method, i={MyClass.i}")

 
# 实例化类
x = MyClass()
 
# 实例访问类的属性
print("实例访问 MyClass 类的属性 i 为：", x.i)

# 类访问类的属性
print("类访问 MyClass 类的属性 i 为：", MyClass.i)

print(f"instance_method 调用前, x={x}, x:{id(x)}, x.__class__={x.__class__}")

print("---------实例开始调用-----------")
x.instance_method()
x.class_method()
x.static_method()


print(f"class_method 调用前, cls:{id(MyClass)}, cls={MyClass}")

print("---------类开始调用-----------")
MyClass.instance_method(1) 
MyClass().instance_method()
MyClass.class_method()
MyClass.static_method()

#----------------------可以重复定义，下面的类会覆盖上面的类--------------------

class MyClass:
    class_variable = 0

    # 构造方法
    def __init__(self, instance_variable):
        self.instance_variable = instance_variable

    # 析构方法
    # def __del__(self):
    #     print("Object destroyed")

    def instance_empty_method(self):
        "Python中的方法或者函数必须包含至少一条语句"
        pass 
    
    def instance_method(self):
        #self.__class__.class_variable = 10
        print(f"This is a instance method,instance_variable={self.instance_variable},class_variable={self.__class__.class_variable}")

    @classmethod
    def class_method(cls):
        cls.class_variable += 1
        print(f"This is a class method, class_variable={cls.class_variable}")
    
    @staticmethod
    def static_method(a, b):
        print(f"This is a static method, sum={a+b}, class_variable={MyClass.class_variable}")



my_instance = MyClass("instance_variable_1")
my_instance.instance_method() # 输出：This is a instance method,instance_variable=instance_variable_1,class_variable=0

MyClass.class_method()                # 输出：This is a class method, class_variable=1
my_instance.class_method()            # 输出：This is a class method, class_variable=2
my_instance.__class__.class_method()  # 输出：This is a class method, class_variable=3

MyClass.static_method(1, 2)           # 输出：This is a static method, sum=3
my_instance.static_method(3, 4)       # 输出：This is a static method, sum=7

my_instance.instance_variable = "😄"
my_instance.instance_method()         # 输出：This is a instance method,instance_variable=😄,class_variable=3


my_instance2 = MyClass("instance_variable_2")
print(f"my_instance2.class_variable={my_instance2.class_variable}") # 输出：my_instance2.class_variable=3


print("----------isinstance-my_instance 开始------------")
print(isinstance(my_instance.instance_method,MethodType))   # 输出：True
print(isinstance(my_instance.instance_method,FunctionType)) # 输出：False

print(isinstance(my_instance.class_method,MethodType))      # 输出：True
print(isinstance(my_instance.class_method,FunctionType))    # 输出：False

print(isinstance(my_instance.static_method,MethodType))     # 输出：False
print(isinstance(my_instance.static_method,FunctionType))   # 输出：True

print("----------isinstance-MyClass 开始------------")

print(isinstance(MyClass.instance_method,MethodType))   # 输出：False
print(isinstance(MyClass.instance_method,FunctionType)) # 输出：True

print(isinstance(MyClass.class_method,MethodType))      # 输出：True
print(isinstance(MyClass.class_method,FunctionType))    # 输出：False

print(isinstance(MyClass.static_method,MethodType))     # 输出：False
print(isinstance(MyClass.static_method,FunctionType))   # 输出：True

print("----------isinstance-my_instance 打印函数开始------------")
print(my_instance.instance_method) # <bound method MyClass.instance_method of <__main__.MyClass object at 0x10a118790>>
print(my_instance.class_method)    # <bound method MyClass.class_method of <class '__main__.MyClass'>>
print(my_instance.static_method)   # <function MyClass.static_method at 0x10a1042c0>
 
print("----------isinstance-MyClass 打印函数开始------------")
print(MyClass.instance_method)     # <function MyClass.instance_method at 0x10a104180>
print(MyClass.class_method)        # <bound method MyClass.class_method of <class '__main__.MyClass'>>
print(MyClass.static_method)       # <function MyClass.static_method at 0x10a1042c0>


class MyClass:
    def __new__(cls, *args, **kwargs):
        print("Creating a new instance")
        instance = super().__new__(cls)
        # 对实例对象进行必要的初始化或其他操作
        # ...
        return instance

    def __init__(self, *args, **kwargs):
        print("Initializing the instance")
        # 对实例进行初始化操作
        # 设置属性的初始值
        # ...

    def __del__(self):
        print("__del__")
        # 执行清理操作和资源释放
        # ...

obj = MyClass()  # Creating a new instance"
                 # Initializing the instance"
                 # __del__

class ParentClassA:
    def __init__(self, value):
        self.value = value
    def some_method(self):
        print("This is the parent classA method.")

class ParentClassB:
    def some_method(self):
        print("This is the parent classB method.")

class ChildClass(ParentClassA,ParentClassB):
    def __init__(self, value, name):
        super().__init__(value)  # 将value参数传递给父类的__init__方法
        self.name = name
    
    def some_method(self):
        super().some_method()          # 调用父类的some_method方法
        print("This is the child class method.")
        ParentClassB.some_method(self) # 显式调用ParentClassB的some_method方法

obj = ChildClass(10, "John")
print(obj.value)  # 输出：10
print(obj.name)   # 输出："John"

# 使用类的__mro__属性来查看 MRO 顺序
print(ChildClass.__mro__)  # 输出：(<class '__main__.ChildClass'>, <class '__main__.ParentClass1'>, <class '__main__.ParentClass2'>, <class 'object'>)

obj.some_method()


#------------钻石继承问题---------------
class ParentClassA:
    def some_method(self):
        print("ParentClassA method.")

class ParentClassB(ParentClassA):
    pass

class ParentClassC(ParentClassA):
    def some_method(self):
        print("ParentClassC method.")

class ChildClass(ParentClassB, ParentClassC):
    pass

obj = ChildClass()
obj.some_method()


# --------------------------属性---------------------

class MyClass:

    class_attribute = "Class Attribute"

    def __init__(self, public_variable, private_variable, protected_variable):
        self.public_variable = public_variable
        self.__private_variable = private_variable
        self._protected_variable = protected_variable

    @property
    def private_variable(self):
        return self.__private_variable

    @private_variable.setter
    def private_variable(self, value):
        self.__private_variable = value

my_instance = MyClass("public_variable_1", "private_variable_1", "protected_variable_1")

# 实例访问类属性
print(my_instance.class_attribute)  # 输出：Class Attribute
# 实例设置类属性
my_instance.class_attribute = "class_attribute update instance"
print(my_instance.class_attribute)  # 输出：class_attribute update instance

# 类访问类属性
print(MyClass.class_attribute)  # 输出：Class Attribute
# 类设置类属性
MyClass.class_attribute = "class_attribute update MyClass"
print(MyClass.class_attribute) # 输出：class_attribute update MyClass

print(my_instance.public_variable)  # 输出：public_variable_1
my_instance.public_variable = "public_variable_2"
print(my_instance.public_variable)  # 输出：public_variable_2

# print(my_instance.__private_variable)  # 报错：'MyClass' object has no attribute '__private_variable'
# 使用属性访问器获取属性值
print(my_instance.private_variable)  # 输出：private_variable_1
# 使用属性访问器设置属性值
my_instance.private_variable = "private_variable_2"
print(my_instance.private_variable)  # 输出：private_variable_2

print(my_instance._protected_variable)  # 输出：protected_variable_1
my_instance._protected_variable = "protected_variable_2"
print(my_instance._protected_variable)  # 输出：protected_variable_2


# ---------------__class__属性-------------
class MyClass:
    class_variable = 0

    def __init__(self, instance_variable):
        self.instance_variable = instance_variable

my_instance = MyClass("instance_variable_1")

# 实例调用__class__属性
print(my_instance.__class__)  # 输出：<class '__main__.MyClass'>

# 类调用__class__属性
print(MyClass.__class__)  # 输出：<class 'type'>

# 其他对象调用__class__属性
a = 1
print(a.__class__)  # 输出：<class 'int'>


# ---------运算符重载-----------
class Point:
   def __init__(self, x, y):
      self.x = x
      self.y = y
 
   def __str__(self):
      return 'Point (%d, %d)' % (self.x, self.y)
   
   def __add__(self,other):
      return Point(self.x + other.x, self.y + other.y)
 
p1 = Point(2,10)
p2 = Point(5,-2)
print (p1, p2, p1 + p2) # Point (2, 10) Point (5, -2) Point (7, 8)


# ---------------------命名空间与作用域-------------
x = 10  # 全局命名空间

def outer():
    y = 20  # outer()函数的局部命名空间
    def inner():
        z = 30  # inner()函数的局部命名空间
        print(x, y, z)  # 在inner()函数中访问全局变量x和外部函数变量y
    
    inner()
outer()


x = 10  # 全局变量

def func():
    global x  # 声明x为全局变量
    x = 20

print(x)  # 输出: 10
func()
print(x)  # 输出: 20


def outer():
    x = 10  # 外部函数的局部变量

    def inner():
        nonlocal x  # 声明x为非局部变量
        x = 20

    print(x)  # 输出: 10
    inner()
    print(x)  # 输出: 20

outer()