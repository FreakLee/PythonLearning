# Day3-数据结构

## 数字
* 整型(int)：Python3 整型是没有限制大小的，可当作 Long 类型使用，所以 Python3 没有 Python2 的 Long 类型。布尔(bool)是整型的子类型
* 浮点型(float)
* 复数((complex))：可用a + bj,或者complex(a,b)表示

数字类型转换
* int(x)
* float(x)
* complex(x)：将x转换到一个复数，实数部分为 x，虚数部分为 0
* complex(x, y)：将 x 和 y 转换到一个复数，实数部分为 x，虚数部分为 y。x 和 y 是数字表达式

``` py
>>> complex(3)
(3+0j)
>>> complex(1,2)
(1+2j)
>>>
```

数学常量
* pi
* e 

## 字符串
* 创建字符串：用单引号或者双引号包裹，不支持单字符类型，单个字符也当做字符串处理
* 字符串连接：+
* 字符串访问：可通过索引访问字符串中的子串，语法为：变量[头下标:尾下标]，头下标跟尾下标均可省略。索引值以 0 为开始值，-1 为从末尾的开始位置
* 字符串长度：len(字符串)
* 多行字符串：用成对的三个双引号或者单引号包裹
* f-string：字面量格式化字符串，Python3.6以后新加的。f-string 格式化字符串以 f 开头，后面跟着字符串，字符串中的表达式用大括号 {} 包起来，它会将变量或表达式计算后的值替换进去
* count(str, beg= 0,end=len(string))：返回 str 在 string 里面出现的次数，如果 beg 或者 end 指定则返回指定范围内 str 出现的次数
* 字符串格式化：与 C 中 sprintf 函数一样的语法
* r/R：所有的字符串都是直接按照字面的意思来使用，没有转义特殊或不能打印的字符
* \*：重复输出字符串，如a = 'a',a*3，则‘aaa’

注意点
Python字符串不能修改，是immutable的。因此，为字符串中某个索引位置赋值会报错
* 如果不希望

``` py
str1 = "Hello World"
str2 = 'Hello World'
print(str1[0])    # 打印H
print(str1[1:-1]) # 打印ello Worl
print(str1[-1])   # 打印d

print(str1[0:]) # 打印Hello World
print(str1[:])  # 打印Hello World

# 左闭右开原则，即不包含最后一个字符
print(str1[0:-1]) # 打印Hello Worl
print(str1[:-1])  # 打印Hello Worl

print(str1.count) # <built-in method count of str object at 0x104fd9ef0> 字符串对象的方法（count）的内存地址
print(str1.count('l')) #打印3
print(str1.count('m')) #打印0
print(len(str1))       #打印11

#多行字符串
mutipleLinesStr = """我是
一个
多行字符串
"""
print(mutipleLinesStr)

name = 'Jack'
print(f"Hello {name}") #Hello Jack
print(r'C:\some\name') #C:\some\ame
```

## 列表
Python有6个序列的内置类型，但最常见的是列表和元组。列表都可以进行的操作包括索引，切片，加，乘，检查成员。列表的数据项不需要具有相同的类型。列表也支持索引、切片，切片操作返回包含请求元素的新列表。列表是可变类型

``` py
list1 = [1,2,3,4,'Bob']

# 访问
print(list1[-1])  #Bob
print(list1[:-1]) #[1, 2, 3, 4]

# 修改
list1[0] = 0
print(list1[0]) # 0

# 删除
del list1[-1]
print(list1) #[1, 2, 3, 4]

# 拼接
list1.append(5)
print(list1) # [1, 2, 3, 4, 5,]

# 长度
print(len(list1)) # 5

# 最大值
print(max(list1))

# 最小值
print(min(list1))

# 组合
list2 = [6,7,8]
list1 = list1 +list2
print(list1)  # [1, 2, 3, 4, 5, 6, 7, 8]

# 判断元素是否在列表里面
print(0 in list1) #False

# 迭代
for x in list1: print(x)

# 重复
print('Hi' * 3) #HiHiHi

# 比较,导入operator模块
a = [1, 2]
b = [2, 3]
c = [2, 3]
print("operator.eq(a,b): ", operator.eq(a,b)) #False
print("operator.eq(c,b): ", operator.eq(c,b)) #True
```

## 元组
Python中元组通列表类似，不同之处在于元组的元素不能修改，元组使用()创建。元组中只包含一个元素时，需要在元素后面添加逗号, ，否则括号会被当作运算符使用

``` py
# 空元组
emptyTup = ()

# 创建
tup = (404,"network error")

# 访问
print(tup[0],tup[1])
print(tup[0],tup[-1])

# 修改
# 元组中的元素值是不允许修改的
# TypeError: 'tuple' object does not support item assignment
# tup[0] = 502  

tup1 = (123,456)
tup2 = ('abc','xyz')
tup3 = tup1 + tup2
print(tup3) # (123, 456, 'abc', 'xyz')

# 删除：元组中的元素值是不允许删除的，但可以使用del语句来删除整个元组
# del tup
# print ("删除后的元组 tup : ")
# NameError: name 'tup' is not defined
# print (tup)

# 元组与列表相互转换
tupToList = list(tup1)
print(tupToList)

listToTup = tuple(tupToList)
print(listToTup)

# 其它：元祖也有len、max、min等跟列表类似的函数
```

## 字典
字典也是一种可变容器模型，可存储任意类型对象。字典的每个键值 key=>value 对用冒号 : 分割，每个对之间用逗号(,)分割，整个字典包括在花括号 {} 中。键必须是唯一的，但值则不必；值可以取任何数据类型，但键必须是不可变的，如字符串，数字

``` py
# 空字典
emptyDict = {}
emptyDict1 = dict()

# 访问
dict = {'Name': 'Jack', 'Age': 7}
print(dict['Name'],dict['Age'])

# 修改
dict['Age'] = 8

# 删除
del dict['Age']

# 清空
# del dict
```

## 集合
集合（set）是一个无序的不重复元素序列，可以进行交集、并集、差集等常见的集合操作。可以使用大括号 { } 创建集合，元素之间用逗号,分隔，也可以使用 set() 函数创建集合

* 创建：{x1,x2,x3} 或者 set() 函数
* 添加：s.add(x) 或者 s.update(x)
* 移除：s.remove(x) 或者 s.discard(x) ，后者若不存在x，则不会报错。s.pop()随机删除一个元素
* 清空：s.clear()

``` py
# 创建
s = set() # 空集合，注意空集合不能直接用{}创建

set1 = {1, 2, 3, 4}           # 直接使用大括号创建集合
set2 = set([4, 5, 6, 7])      # 使用 set() 函数从列表创建集合

# 添加
s.add(1)
s.update({2,3},(4,5)) # 参数可以是列表，元组，字典,x可以有多个，用逗号隔开
print(s)

# 删除
s.remove(1)
s.discard(1)
s.pop()

# 元素个数
print(len(s))

# 判断是否包含某个元素
print(2 in s)
print({2,3} in s)
```