# Day8-面向对象编程

面向对象编程（Object-Oriented Programming，简称OOP）是一种编程范式，它以对象作为程序的基本单元，将数据和行为封装在一起，提高了代码的重用性、可维护性和可扩展性。类是创建实例的抽象模板，而实例则是一个个具体的对象，各个实例拥有的数据相互独立，互不干扰。比如一个Person类就是抽象模板，而一个个具体的人就是Person类具体对象，人都有一些共同的行为，比如吃、喝等，在面向对象编程中这些行为就是方法，每个人都有各自的身高、体重等特征，这些特征可以称为属性。先回顾一下面向对象编程中的一些重要概念：
* 类（Class）：类是一种抽象的数据类型，用于描述具有相同属性和方法的对象的集合。类定义了对象的属性和方法，可以创建多个实例对象。
* 对象（Object）：对象是类的一个实例，具有类定义的属性和方法。每个对象都有自己的状态和行为，可以与其他对象进行交互。
* 封装（Encapsulation）：封装是将数据和行为封装在一起，隐藏了对象内部的实现细节，只暴露必要的接口给外部调用。封装提高了代码的可维护性和可扩展性，同时也保护了对象的状态不被外部随意修改。
* 继承（Inheritance）：继承是一种机制，它允许定义一个类来继承另一个类的属性和方法。子类可以继承父类的所有属性和方法，并可以添加自己的属性和方法。继承提高了代码的重用性和可维护性，同时也提高了代码的可读性。
* 多态（Polymorphism）：多态是指同一种操作作用于不同的对象，可以有不同的解释和执行。例如，不同的类可以实现相同的方法名，但具体实现方式不同。多态提高了代码的灵活性和可扩展性，使得程序更容易适应不同的需求和场景。

## 类与对象

### 类定义
Python中创建的类的语法如下：
``` py
class ClassName:
    <statement-1>
    .
    .
    <statement-N>
```
### 类对象
类对象支持两种操作：属性引用和实例化。在Python中，实例和类都可以调用类方法和静态方法，实例方法只能通过实例调用。
``` py
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
```
## 方法

### 方法分类
在Python中，方法可以分为以下几类：
* 实例方法（Instance Method）：定义在类中，需要实例化后才能调用。第一个参数通常是self，表示当前实例本身，可以用来访问实例的属性和方法。
* 类方法（Class Method）：定义在类中，使用@classmethod装饰器修饰。第一个参数通常是cls，表示当前类本身，可以用来访问类的属性和方法。类方法可以通过类或实例来调用，但通常使用类来调用。通常用于操作类级别的属性和方法。
* 静态方法（Static Method）：定义在类中，使用@staticmethod装饰器修饰。没有特殊的参数，也不需要访问类或实例的状态，通常用于实现与类和实例无关的功能。静态方法可以通过类或实例来调用，但通常使用类来调用。通常用于实现与类和实例无关的功能。
* 特殊方法（Special Method）：定义在类中，以双下划线开头和结尾的方法，也称为魔术方法（Magic Methods）。用于实现对象的特殊行为，比如构造函数__init__、字符串表示函数__str__、比较函数__eq__等。
* 静态属性（Static Property）：定义在类中，使用@property装饰器修饰。没有特殊的参数，也不需要访问类或实例的状态，通常用于实现只读属性。
* 类属性（Class Property）：定义在类中，使用@property装饰器修饰。通常用于实现类级别的只读属性。

### 类方法与静态方法
在Python中，实例对象可以调用staticmethod和classmethod修饰的方法，是因为这两种方法的调用并不依赖于实例对象的状态或属性，因此不需要创建实例对象。

具体来说，staticmethod修饰的方法是在定义类时就存在的，不依赖于实例对象的创建和初始化。因此，实例对象可以直接调用staticmethod修饰的方法。

classmethod修饰的方法是在类定义时就存在的，其第一个参数是类本身，可以通过该参数访问类的属性和方法。因此，即使没有实例对象，也可以通过类名调用classmethod修饰的方法。同时，实例对象也可以调用classmethod修饰的方法，因为classmethod方法的第一个参数可以是类本身或实例对象。

与其他语言相比，Python中实例对象可以调用staticmethod和classmethod修饰的方法的主要原因是Python将类和对象都看作是一等公民，即类和对象都是可以直接操作和访问的。而在其他一些语言中，类和对象是有区别的，例如Java中静态方法只能通过类名调用，而不能通过实例对象调用。

### 方法与函数
在Python中，方法（Method）和函数（Function）都是用来封装代码的工具，但它们之间有一些异同点。

不同点：
* 定义方式不同：方法是定义在类中的，函数是定义在模块中的
* 参数不同：方法的第一个参数通常是self，表示当前实例本身；函数没有这个参数
* 调用方式不同：方法需要通过实例进行调用，可以访问实例的属性和方法；函数可以直接进行调用，无法访问实例的属性和方法

相同点：
* 都可以用来封装代码，实现特定的功能
* 都可以传递参数和返回值
* 都可以使用装饰器、注释等方式来扩展和装饰

需要注意的是未必定义在类中的就是方法。主要看是否与类或者实例有无绑定关系。
* 与类和实例有绑定关系的function都属于方法（method）
* 与类和实例无绑定关系的function都属于函数（function）

一般的，静态方法都属于函数（function），实例调用实例方法和classmethod时都属于方法（method），类名调用classmethod时属于方法（method），类名调用实例方法时属于函数（function）。

``` py
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
```

### 魔术方法
在Python中，魔术方法（Magic methods），也称为特殊方法（Special methods）或双下划线方法（Double underscore methods），是具有特殊命名和功能的方法。这些方法以双下划线（__）开头和结尾，用于实现对象的特定行为和功能。以下是一些常见的魔术方法：

1.对象初始化和销毁：

* \__init__(self, ...): 构造方法，在创建对象时调用，用于对对象的属性进行初始化
* \__del__(self): 析构方法，在对象被销毁时调用，用于释放资源和执行清理操作

2.对象表示：

* \__str__(self): 对象的字符串表示，使用str(obj)或print(obj)时调用
* \__repr__(self): 对象的字符串表示，使用repr(obj)时调用，通常用于调试和开发

3.属性访问：

* \__getattr__(self, name): 在访问不存在的属性时调用
* \__setattr__(self, name, value): 在设置属性值时调用
* \__getattribute__(self, name): 在访问任何属性时调用，无论属性是否存在

4.集合类型：

* \__len__(self): 对象的长度，使用len(obj)时调用
* \__getitem__(self, key): 获取指定键的值，使用obj[key]访问元素时调用
* \__setitem__(self, key, value): 设置指定键的值，使用obj[key] = value时调用
* \__delitem__(self, key): 删除指定键的值，使用del obj[key]时调用

5.比较运算：

* \__eq__(self, other): 等于，使用==进行比较时调用
* \__ne__(self, other): 不等于，使用!=进行比较时调用
* \__lt__(self, other): 小于，使用<进行比较时调用
* \__gt__(self, other): 大于，使用>进行比较时调用
* \__le__(self, other): 小于等于，使用<=进行比较时调用
* \__ge__(self, other): 大于等于，使用>=进行比较时调用


__new__方法和__init__方法在Python中有着不同的作用和执行时机，它们的主要区别如下：

1.角色和调用时机：

* __new__方法是一个类级别的方法，用于创建并返回一个新的实例对象。它在对象的构造过程的早期阶段被调用，在实例对象创建之前执行
* __init__方法是一个实例级别的方法，用于初始化实例的状态。它在对象的构造过程的稍后阶段被调用，在实例对象创建后执行

2.参数：

* __new__方法的第一个参数是类（cls），表示当前正在创建实例的类。它可以接受任意多个额外的参数作为输入
* __init__方法的第一个参数是实例本身（通常命名为self），表示要初始化的实例。它可以接受任意多个额外的参数作为输入

3.返回值：

* __new__方法负责创建并返回一个新的实例对象。它的返回值通常是一个类的实例
* __init__方法不返回任何值，它主要负责对实例对象进行初始化操作

4.控制流：

* __new__方法可以通过返回不同的实例对象来控制实例的创建方式，包括返回缓存的实例、返回其他类的实例等
* __init__方法主要用于对实例对象的属性进行初始化，通常不会改变实例对象本身

总的来说，__new__方法负责实例的创建阶段，可以控制实例的创建方式，而__init__方法负责实例的初始化阶段，对实例的属性进行初始化操作。__new__方法在对象创建之前被调用，__init__方法在对象创建之后被调用。

``` py
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
```
在Python中，__del__是一个特殊的方法，也被称为析构函数（destructor）。它用于在对象被销毁之前执行一些清理操作和释放资源。

当对象不再被引用或程序执行结束时，Python的垃圾回收机制会自动销毁对象。在对象被销毁之前，如果定义了__del__方法，该方法会被自动调用。

在__del__方法中，可以执行一些清理任务，例如关闭文件、释放网络连接、回收资源等。请注意，__del__方法并不是在对象被销毁时立即调用的，而是在垃圾回收机制确定对象不再被引用时才会被调用。

需要注意的是，尽管__del__方法提供了执行清理操作的机会，但它的使用需要慎重。由于垃圾回收机制的工作方式和时机不确定，依赖于__del__方法来释放资源可能不是一个可靠的做法。更好的做法是使用上下文管理器（with语句）或显式地调用适当的方法来确保资源的正确释放。

## 继承
在Python中，如果一个类没有显式地指定基类，它会默认继承自一个称为object的基类。object是Python中的根基类，几乎所有的类都直接或间接地继承自它。Python也是支持多继承的编程语言。语法如下：
``` py
class DerivedClassName(Base1, Base2, Base3):
    <statement-1>
    .
    .
    .
    <statement-N>
```
继承中__init__方法的一些规则及注意事项：
* 子类的__init__方法不会自动调用父类的__init__方法：子类的__init__方法不会自动调用其父类的__init__方法。如果子类需要执行父类的初始化操作，必须显式调用父类的__init__方法。可以使用super()函数来调用父类的__init__方法
* 多重继承时的__init__方法调用顺序：当一个类继承自多个父类时，其__init__方法的调用顺序遵循所谓的"方法解析顺序"（Method Resolution Order, MRO）。MRO 定义了多个父类之间的继承顺序，决定了super()函数在多重继承中的调用顺序。
* 初始化参数的传递：在类层级之间的__init__方法中，可以通过参数的传递来进行初始化操作。子类的__init__方法可以接收额外的参数，并将这些参数传递给父类的__init__方法

### 方法重写
在Python中，方法重写（Method Overriding）是指子类定义了与父类相同名称的方法，并且在子类中使用该方法覆盖了父类中的实现。方法重写允许子类修改或扩展从父类继承的方法的行为。

* 方法名称和参数列表必须与父类中被重写的方法相同：在子类中重写方法时，必须使用与父类中被重写的方法相同的名称和参数列表。否则，它将被视为子类中的新方法，而不是重写父类的方法。
* 使用super()函数调用父类方法：在子类的重写方法中，可以使用super()函数来调用父类的方法。这样可以在子类中扩展父类方法的行为，而不是完全覆盖它。通过super()调用父类方法时，可以确保父类的逻辑仍然被执行。
* 方法重写可以修改方法的行为：通过方法重写，子类可以修改从父类继承的方法的行为，包括添加新的逻辑、修改参数、修改返回值等。子类可以根据自身的需求来定制继承的方法。

### 多继承
Python中多继承的一些注意事项：
* 方法解析顺序（Method Resolution Order, MRO）：当一个类继承自多个父类时，Python 使用 C3 线性化算法来确定方法的解析顺序。MRO 定义了多个父类之间的继承顺序，决定了方法在多重继承中的调用顺序。MRO 可以通过子类的__mro__属性进行查看。
* 使用super()函数调用父类方法：在多继承中，可以使用super()函数来调用父类的方法。通过super()函数，可以按照方法解析顺序依次调用父类的方法。
* 显式调用指定父类的方法：在多继承中，可以通过指定父类名称来显式调用特定父类的方法。
* 钻石继承（Diamond Inheritance）问题：当多个父类中存在共同的父类时，形成了钻石继承结构。例如，类A是类B和类C的父类，而类D继承自类B和类C。这种情况下，如果在类D中调用共同父类的方法，会出现方法冲突的问题。
``` py
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
```

## 属性
在Python中，属性是与对象关联的值或数据。属性可以是类属性（class attribute）或实例属性（instance attribute），它们分别与类和类的实例相关联。
* 类属性（Class attributes）：
类属性是属于类本身的属性，而不是类的实例。它们在类定义中使用，并且对所有该类的实例共享相同的值。可以通过类名或实例访问类属性。
* 实例属性（Instance attributes）：
实例属性是与类的实例相关联的属性。每个类的实例都有自己独立的实例属性。实例属性在类的方法中使用 self 关键字定义，并且只能通过实例来访问。
* 属性访问器（Property Accessors）：
属性访问器是一种特殊的方法，用于控制对属性的访问。通过使用 @property 装饰器来定义属性访问器。属性访问器允许你在访问属性时执行自定义的操作，例如计算、验证或转换。

### __class__属性
__class__是一个特殊的属性，用于返回对象所属的类。它可以被任何对象调用，包括实例、类和其他对象。

* 当实例调用__class__时，它返回该实例所属的类。
* 当类调用__class__时，它返回类本身。
* 当其他对象调用__class__时，它返回该对象所属的类（通常是object类或其子类）。

需要注意的是，__class__属性只能被访问，不能被直接赋值。如果需要动态修改对象所属的类，可以使用type()函数来创建一个新类，并将对象的类型修改为该新类。

``` py
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
```

## 运算符重载
在 Python 中，运算符重载是指通过定义特定的双下划线方法（魔术方法）来改变内置运算符的行为。通过重载运算符，可以使自定义类的对象支持与内置类型相似的操作。

以下是一些常见的运算符及其对应的双下划线方法：

1.算术运算符：
* 加法：+ --> \__add__
* 减法：- --> \__sub__
* 乘法：* --> \__mul__
* 除法：/ --> \__truediv__
* 取余：% --> \__mod__
* 幂运算：** --> \__pow__

2.比较运算符：
* 相等性：== --> \__eq__
* 不等性：!= --> \__ne__
* 大于：> --> \__gt__
* 小于：< --> \__lt__
* 大于等于：>= --> \__ge__
* 小于等于：<= --> \__le__

3.逻辑运算符：
* 与：and --> \__and__
* 或：or --> \__or__
* 非：not --> \__not__

4.索引和切片运算符：
* 索引：[] --> \__getitem__
* 赋值索引：[] --> \__setitem__
* 切片：[:] --> \__getitem__ 和 \__setitem__

通过在自定义类中实现这些双下划线方法，可以定义对象在相应的运算符下的行为。例如，可以定义两个自定义类对象相加的行为，或者定义对象如何进行索引和切片操作。

以下是一个简单的示例，演示了如何重载加法运算符：
``` py
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
```

## 命名空间与作用域

### 命名空间

* 命名空间是一个存储变量名称和对应对象的映射关系的系统。
* 在Python中，每个命名空间都是一个字典，其中变量名是字典中的键，对应的对象是字典中的值。
* 可以通过变量名来访问和操作命名空间中的对象。
* 命名空间提供了一种组织和管理变量的机制，以防止命名冲突并提供变量的可见性。

Python中主要有以下几种命名空间：
* 内建命名空间built-in namespace）：包含了Python解释器中预定义的函数和对象，如print()和len()。
* 全局命名空间（global namespace）：是在模块级别定义的命名空间，它包含了在整个模块中定义的变量、函数、其它导入的模块、模块级的变量和常量。
* 局部命名空间局部命名空间（local namespace）：是在函数、方法或代码块内定义的命名空间，它包含了在该函数、方法或代码块中定义的变量和函数。

命名空间查找顺序:
* 假设我们要使用变量 a，则 Python 的查找顺序为：局部的命名空间 -> 全局命名空间 -> 内置命名空间。
* 如果找不到变量 a，它将放弃查找并引发一个 NameError 异常:


命名空间的生命周期取决于对象的作用域，如果对象执行完成，则该命名空间的生命周期就结束。因此，我们无法从外部命名空间访问内部命名空间的对象。

1.模块级别命名空间（Module-level Namespace）：

* 模块级别命名空间是在一个模块文件中定义的命名空间，包含了在该模块中定义的变量、函数和类。
* 该命名空间的生命周期从模块被导入开始，直到解释器退出或模块被显式地重新加载、卸载或修改。
    
2.类级别命名空间（Class-level Namespace）：

* 类级别命名空间是在类定义中定义的命名空间，包含了在类中定义的变量、方法和嵌套类。
* 该命名空间的生命周期从类被定义开始，直到程序执行结束或类被显式地重新定义或删除。

3.实例级别命名空间（Instance-level Namespace）：

* 实例级别命名空间是在类的实例化过程中创建的命名空间，包含了实例的属性和方法。
* 该命名空间的生命周期从实例被创建开始，直到实例被销毁或垃圾回收。

4.函数级别命名空间（Function-level Namespace）：

* 函数级别命名空间是在函数调用时创建的命名空间，包含了函数的参数、局部变量和内部定义的函数。
* 该命名空间的生命周期从函数被调用开始，直到函数返回或垃圾回收。

### 作用域

作用域是指变量在程序中的可访问性和可见性范围。Python中有以下几种作用域：

* 局部作用域（Local Scope）：是在函数、方法或代码块内部定义的作用域，只在其定义的函数、方法或代码块内部可见。
* 嵌套作用域（Enclosing Scope）：是指在一个函数内部定义的函数所创建的作用域。内部函数可以访问外部函数的变量。
* 全局作用域（Global Scope）：在整个程序中都是可见的，定义在模块级别的变量属于全局作用域。
* 内建作用域（Built-in）：包含了内建的变量/关键字等，最后被搜索。

Python使用LEGB规则来解析变量的作用域。LEGB的含义是：Local（局部作用域）→ Enclosing（嵌套作用域）→ Global（全局作用域）→ Built-in（内建作用域）。
这意味着Python首先在局部作用域中查找变量，然后是嵌套作用域、全局作用域和最后是内建作用域。

作用域和命名空间的关系：
* 每个作用域都有对应的命名空间，用于存储变量名称和对象的映射关系。
* 当在某个作用域中创建一个变量时，该变量会存储在该作用域的命名空间中。
* 在变量解析时，Python会按照LEGB规则从最内层的作用域开始查找对应的变量，直到找到第一个匹配的变量或查找完所有作用域。
* 如果变量在当前作用域中找不到，则会继续向上一级作用域查找，直到找到为止。如果找不到，将引发NameError异常。

``` py
x = 10  # 全局命名空间

def outer():
    y = 20  # outer()函数的局部命名空间
    def inner():
        z = 30  # inner()函数的局部命名空间
        print(x, y, z)  # 在inner()函数中访问全局变量x和外部函数变量y
    
    inner()
outer()
```

global关键字：
global关键字用于在函数内部声明一个变量为全局变量，使其在函数内外都可访问和修改。
``` py
x = 10  # 全局变量

def func():
    global x  # 声明x为全局变量
    x = 20

print(x)  # 输出: 10
func()
print(x)  # 输出: 20
```
在这个例子中，global x语句将变量x声明为全局变量，使得在函数func()内部对x的修改也影响到了函数外部对x的访问。

nonlocal关键字：
nonlocal关键字用于在嵌套函数内部声明一个变量为非局部变量，使其可以在嵌套函数的外部函数中进行访问和修改。
``` py
def outer():
    x = 10  # 外部函数的局部变量

    def inner():
        nonlocal x  # 声明x为非局部变量
        x = 20

    print(x)  # 输出: 10
    inner()
    print(x)  # 输出: 20

outer()
```
在这个例子中，nonlocal x语句将变量x声明为非局部变量，使得在内部函数inner()中对x的修改也影响到了外部函数outer()中对x的访问。