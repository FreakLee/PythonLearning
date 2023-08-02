# Day7-异常处理、调试与测试

## 异常处理
在 Python 中，错误可以分为两种：语法错误和运行时错误。语法错误是在编译时发现的错误，例如拼写错误、缺少括号等。运行时错误是在程序运行时发生的错误，例如除以零、访问不存在的变量等。

### try-except 语句
try-except 语句用于捕获和处理运行时错误。try 语句块包含可能引发错误的代码，如果代码正常执行，则跳过 except 语句块。如果代码引发了异常，则执行 except 语句块中的代码

### try-except-else 语句
try-except-else 语句与 try-except 语句类似，但是还提供了一个 else 语句块，用于处理没有引发异常的情况。如果 try 语句块中的代码正常执行，则跳过 except 语句块，执行 else 语句块中的代码

### try-finally 语句
try-finally 语句用于在发生错误时执行清理操作。finally 语句块中的代码始终会被执行，无论是否发生错误，可以用于清理资源，例如关闭文件、释放内存等

### raise 语句
raise 语句用于手动引发异常，可以用于自定义异常和错误处理

### assert 语句
assert 语句用于检查条件是否成立，如果不成立，则引发 AssertionError 异常

### 自定义异常
通过创建一个新的异常类来拥有自己的异常。异常类继承自 Exception 类，可以直接继承，或者间接继承

``` py
# try-except
"""
try:
    # 可能引发错误的代码
    ...
except Exception as e:
    # 处理错误的代码
    print(e)
"""
def test(x):
    try:
        # 可能引发错误的代码
        print(f"0-代码正常运行时：1/{x} = {1/x}")
    except Exception as e:
        # 处理错误的代码
        print(e)
        print("错误-0-结束")
test(0)
test(1)


# try-except-else
"""
try:
    # 可能引发错误的代码
    ...
except Exception as e:
    # 处理错误的代码
    print(e)
else:
    # 没有错误的代码
    ...
"""
def test1(x):
    try:
        # 可能引发错误的代码
        res = 1/x
        print(f"1-try-代码正常运行时：1/{x} = {res}")
        str1 = "1-try中的变量"
    except Exception as e:
        # 处理错误的代码
        print(e)
        print("错误-1-结束")
    else:
        print(f"1-else-代码正常运行时：1/{x} = {res}---{str1}")

test1(0)
test1(1)


# try-finally
"""
try:
    # 可能引发错误的代码
    ...
except:
    # 处理错误的代码
    ...
else:
    # 没有错误的代码
    ...
finally:
    # 清理代码
    ...
"""

def test2(x):
    
    try:
        # 可能引发错误的代码
        1/x
        print(f"2-try-代码正常运行时：1/{x}")
        a = 6
    except Exception as e:
        # 处理错误的代码
        print(e)
        print("错误-2-结束")
        #b = 7
    else:
        print("2-else-正常运行代码")
    finally:
        # 清理代码
        print(f"2-finally-最后都会运行：1/{x}") #不能访问try except else中的对象

test2(0)
test2(1)


# raise
"""
raise [Exception [, args [, traceback]]]
"""
def test3(x):
    try:
        if x == 0:
            raise ValueError("raise：除数不能为0")
    except ValueError as e:
        print(e)

test3(0)

# assert
"""
raise [Exception [, args [, traceback]]]
"""
def test4(x):
    try:
        assert x != 0, "assert：除数不能为0"
    except AssertionError as e:
        print(e)

test4(0)
```

## 调试

* 使用print语句：在代码中添加print语句以输出变量的值，从而检查代码的执行路径和结果
* 使用pdb模块：pdb是Python的调试器，可以在代码执行过程中停止程序并查看变量的值，以及跟踪程序的执行路径。pdb模块可以通过在代码中插入断点来使用，例如在代码中插入import pdb; pdb.set_trace()语句即可在该位置打断点
* 使用IDE集成的调试器：许多Python集成开发环境（IDE）都具有内置的调试器，可以使用该调试器在代码执行过程中检查变量和跟踪程序的执行路径
* 使用第三方调试器：除了pdb以外，还有一些第三方调试器，如PyCharm、VS Code等

在开发中，日志打印是最简单、最常用的调试方法。可以用assert替换一部分print语句，更多的时候是用logging这个库来打印日志信息。相比print语句，logging库提供了丰富的日志级别、日志格式和日志输出方式等配置选项，可以根据实际需求进行灵活配置。下面简单总结一下logging的使用方法：
* 导入logging库，并进行基本配置
    ``` py
    import logging
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    ```
* 在需要记录日志的地方，调用logging库中的方法进行日志记录
    ``` py
    def add(a, b):
        logging.info(f"Adding {a} and {b}")
        return a + b
    ```
* 运行程序，查看日志记录
    ``` py
    if __name__ == '__main__':
    result = add(2, 3)
    logging.info(f"Result: {result}")
    ```
* 运行上面程序可以在控制台收到类似如下信息：
    ```
    2023-08-02 11:19:49,628 - INFO - Adding 2 and 3
    2023-08-02 11:19:49,629 - INFO - Result: 5
    ```

## 单元测试
Python中有很多单元测试框架可供选择，例如unittest、pytest、nose等。下面以unittest框架为例，说明Python中的单元测试如何进行：
* 导入unittest模块，并创建一个继承自unittest.TestCase的测试类
* 在测试类中定义测试方法，测试方法的名称必须以“test_”开头。在测试方法中编写测试代码，并使用断言来检查代码的输出是否符合预期
* 在测试代码中使用assertEqual、assertTrue等断言方法，检查代码的输出是否符合预期。如果测试通过，则不会输出任何内容，如果测试失败，则会输出错误信息
* 运行测试用例。可以通过在命令行中执行python -m unittest test_module.py来运行测试用例，其中“test_module.py”是包含测试代码的Python模块的文件名
* 查看测试结果。测试完成后，unittest会输出测试结果，包括测试用例的总数、通过的测试用例数、失败的测试用例数等
``` py
import unittest

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('hello'.upper(), 'HELLO')

    def test_isupper(self):
        self.assertTrue('HELLO'.isupper())
        self.assertFalse('Hello'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()
```
运行上面测试代码可以得到如下![测试结果](https://github.com/FreakLee/PythonLearning/blob/main/Screenshot/Day7/1.jpg)

## 文档测试
Python中的文档测试可以帮助开发者测试代码的正确性，并且可以自动生成文档。以下是一个详细的Python中文档测试操作示例：
* 首先，需要在Python代码中添加文档测试。文档测试是在Python代码的docstring中编写的，例如：
``` py
def add(a, b):
    """
    This function adds two numbers.

    >>> add(2, 3)
    5
    >> add(-1, 1)
    0
    """
    return a + b
```
在上面的示例中，docstring中嵌入了文档测试，使用>>>表示需要执行的Python代码，使用期望的输出结果来验证代码的正确性。此处特地在'5'的下一行少写了一个'>'，以便查看测试效果。
* 运行文档测试。可以使用Python自带的doctest模块来运行文档测试。在Python代码中添加以下代码来运行文档测试：
``` py
if __name__ == '__main__':
    import doctest
    doctest.testmod()
```
testmod()函数将自动查找并执行代码中的文档测试，并输出测试结果。
* 查看文档测试结果。运行文档测试后，doctest将输出测试结果，包括测试用例的总数、通过的测试用例数、失败的测试用例数等

例如，运行上面的示例代码，输出的测试结果如下：
```
**********************************************************************
File "test_doc.py", line 6, in __main__.add
Failed example:
    add(2, 3)
Expected:
    5
    >> add(1, -1)
    0
Got:
    1
**********************************************************************
1 items had failures:
   1 of   1 in __main__.add
***Test Failed*** 1 failures.
```
