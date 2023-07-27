# Day2-Python基础

## 标识符
Python中的标识符跟多数编程语言的标识符规则类似。
* 字母或者下划线开头
* 只能包含字母、数字和下划线
* 区分大小写

Python3中变量是支持中文的，非ASCII标识符也是允许的。

``` py
哈哈 = 5
print(哈哈)
>>> 5
```

## 保留字

Python中的保留字不能作为标识符，可以通过标注库keyword获取所有保留字。

``` py
import keyword
print(keyword.kwlist)

['False', 'None', 'True', '__peg_parser__', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

```

## 注释

* 单行注释以#开头
* 多行注释成对的三个单引号‘或者双引号"

``` py
"""
这是一个多行注释
哈哈
"""

'''
这又是一个多行注释
嘿嘿
'''
```

## 缩进

Python中使用缩进表示代码块，而不需要大括号{}。缩进的空格长度是可以变化，但是同一代码块的缩进长度要保持一致。

``` py
if True:
    print("true")
    print("第二个 true")
else:
        print("false")
    print("第二个 false") #此处报错，与上一行缩进长度不一致
```

## 基本数据类型

* Number（数字），有 int、float、bool、complex（复数,eg：1 + 2j）
* String（字符串）
* bool（布尔类型）
* List（列表）
* Tuple（元组）
* Set（集合）
* Dictionary（字典）

Python3中常见的数据类型有以上六种，其中不可变数据（3 个）：Number（数字）、String（字符串）、Tuple（元组）；可变数据（3 个）：List（列表）、Dictionary（字典）、Set（集合）

## 运算符

* 算术运算符：+、-、*、/、%、**（幂）、//（取整除 - 往小的方向取整数）
* 比较运算符：==、！=、>=、<=、>、<
* 赋值运算符：=、+=、-=、*=、/=、%=、**=、//=、:=（海象运算符，可在表达式内部为变量赋值。Python3.8 版本新增运算符）
* 逻辑运算符：and、or、not
* 位运算符：&、|、^、~、<<、>>
* 成员运算符：in、not in(判断实例中包含了一系列的成员，包括字符串，列表或元组)
* 身份运算符：is、is not

### 算术运算符
~~~ py
2 ** 3  #输出8
17 / 4  #输出4.25
8 / 4   #输出2.0 除法总是输出浮点数
17 // 4 #输出4
~~~

### 身份运算符
* is：判断两个标识符是不是引用自一个对象
* is not：判断两个标识符是不是引用自不同对象
* is 与 == 区别：is 用于判断两个变量引用对象是否为同一个， == 用于判断引用变量的值是否相等
~~~ py
a = 20
b = 20
 
if ( a is b ):
   print ("1 - a 和 b 有相同的标识")
else:
   print ("1 - a 和 b 没有相同的标识")
 
# id() 函数用于获取对象内存地址
if ( id(a) == id(b) ):
   print ("2 - a 和 b 有相同的标识")
else:
   print ("2 - a 和 b 没有相同的标识")
 
# 修改变量 b 的值
b = 30
if ( a is b ):
   print ("3 - a 和 b 有相同的标识")
else:
   print ("3 - a 和 b 没有相同的标识")
 
if ( a is not b ):
   print ("4 - a 和 b 没有相同的标识")
else:
   print ("4 - a 和 b 有相同的标识")

#输出
1 - a 和 b 有相同的标识
2 - a 和 b 有相同的标识
3 - a 和 b 没有相同的标识
4 - a 和 b 没有相同的标识

a = [1, 2, 3]
b = a
print(b is a) #True
print(b == a) #True

b = a[:]
print(b is a) #False
print(b == a) #True

if (1 in a ):
   print ("1 在给定的列表中 list a 中") #打印
else:
   print ("1 不在给定的列表中 list a 中")

if (1 not in a ):
   print ("1 不在给定的列表中 list a 中")
else:
   print ("1 在给定的列表中 list a 中") #打印
~~~


## 数据类型转换

* 隐式类型转换：自动完成
* 显示类型转换：需要借助类型转换函数

~~~ py
# 隐式类型转换
>>> num_int = 5
>>> num_flo = 4.5
>>> num_new = num_int + num_flo
>>> num_new
9.5

# 显示类型转换
>>> str = "1"
>>> int(str)
1
~~~
