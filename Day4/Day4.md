# Day4-条件控制与循环语句

## if语句：if – elif – else
* 每个条件后面要使用冒号 :，表示接下来是满足条件后要执行的语句块
* 使用缩进来划分语句块，相同缩进数的语句在一起组成一个语句块
* Python 中没有 switch...case 语句，但在 Python3.10 版本添加了 match...case，功能也类似

``` py
# if语句
age = int(input("请输入你家狗狗的年龄: "))
if age <= 0:
    print("你是在逗我吧!")
elif age == 1:
    print("相当于 14 岁的人。")
elif age == 2:
    print("相当于 22 岁的人。")
elif age > 2:
    human = 22 + (age -2)*5
    print("对应人类年龄: ", human)
 
# 退出提示
input("点击 enter 键退出")


# if嵌套
num = int(input("输入一个数字："))
if num%2 == 0:
    if num%3 == 0:
        print ("你输入的数字可以整除 2 和 3")
    else:
        print ("你输入的数字可以整除 2，但不能整除 3")
else:
    if num%3 == 0:
        print ("你输入的数字可以整除 3，但不能整除 2")
    else:
        print  ("你输入的数字不能整除 2 和 3")

# match...case
# 一个 case 也可以设置多个匹配条件，条件使用 ｜ 隔开
def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case _: #case _: 类似于其它语言中的default:，当其他 case 都无法匹配时，匹配这条，保证永远会匹配成功
            return "Something's wrong with the internet"
        
mystatus = 400 
print(http_error(400)) # Bad request
```

## while语句

``` py
n = 10

sum = 0
counter = 1
while counter <= n:
    sum = sum + counter
    counter += 1
print("1 到 %d 之和为: %d" % (n,sum))

#while...else语句
"""
while <expr>:
    <statement(s)>
else:
    <additional_statement(s)>
"""
```

## for语句

``` py
"""
for <variable> in <sequence>:
    <statements>
else:
    <statements>

"""
for x in [1,2,3]:
    print(x)
else:
    print("循环已结束")
```

## range()函数常用于遍历数字序列

``` py
for x in range(3):
    print(x)
```

## pass语句
pass是空语句，是为了保持程序结构的完整性，不做任何事情，一般用做占位语句

``` py
for letter in 'Hello': 
   if letter == 'l':
      pass
      print ('执行 pass 块')
   print ('当前字母 :', letter)
 
print ("Good bye!")
```
