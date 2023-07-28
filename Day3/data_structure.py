
import operator

#复数
print(complex(3)) #打印(3+0j)
print(complex(1,2)) #打印(1+2j)

# --------字符串------------
str1 = "Hello World"
str2 = 'Hello World'
print(str1[0])
print(str1[1:-1])
print(str1[-1])

print(str1[0:])
print(str1[:])

print(str1[0:-1])
print(str1[:-1])

print(str1.count)
print(str1.count('l'))
print(str1.count('m'))
print(len(str1)) 

mutipleLinesStr = """我是
一个
多行字符串
"""
print(mutipleLinesStr)

name = 'Jack'
print(f"Hello {name}")

print(r'C:\some\name')


# --------列表------------
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


# --------元组------------
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


# --------字典------------
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


# --------集合------------
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


# 再论对象的可变与不可变
a = ['c','a','b']
a.sort()
print(a) #['a','b','c']

aStr = "abc"
bStr = aStr.replace('a','A')
print(aStr,bStr) # abc Abc

