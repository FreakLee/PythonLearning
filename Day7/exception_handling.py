
# ---------------异常处理-----------------
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