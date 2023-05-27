# Day1

## Python简介

Python，是一种广泛使用的解释型、高级和通用的编程语言。Python支持多种编程范型，包括结构化、过程式、反射式、面向对象和函数式编程。它拥有动态类型系统和垃圾回收功能，能够自动管理内存使用，并且其本身拥有一个巨大而广泛的标准库。它的语言结构以及面向对象的方法，旨在帮助程序员为小型的和大型的项目编写逻辑清晰的代码。（via [维基百科](https://zh.wikipedia.org/wiki/Python)）

## 安装Python

Mac电脑内置Python。学习时从[官网](https://www.python.org/)下载的最新版3.11.3 dmg安装包。安装简单，双击安装包一路到底就行。
![Python3.11](https://github.com/FreakLee/PythonLearning/blob/main/Screenshot/Day1/1.jpg)

打开终端，输入命令python -v检查是否安装成功。报错信息为：-bash: pyhon: command not found，则将python改为python3。安装成功则会进入python交互式环境中，如下图所示。
![安装成功提示](https://github.com/FreakLee/PythonLearning/blob/main/Screenshot/Day1/2.jpg)

## 第一个Python程序

Python是一种解释性脚本语言。一般的，这种语言支持两种代码运行方式：
* 交互式编程
* 源文件运行（.py文件）

### 交互式编程

如下图所示，在终端python交互式环境中，打印一下Hello Python。
![Python交互式](https://github.com/FreakLee/PythonLearning/blob/main/Screenshot/Day1/3.jpg)

当然也可以利用工具IDLE，如下图所示：
![IDLE](https://github.com/FreakLee/PythonLearning/blob/main/Screenshot/Day1/4.jpg)

### 运行源文件（.py）

跟其它编程语言类似，如C的源文件.c，Python语言的源文件为.py。可以任意编辑器编写Python文件，然后运行源文件。如下图所示在终端创建一个hello.py文件，然后利用vi编写源文件，保存退出，利用python3命令解释源文件，同样打印出了Hello Python。
![源文件运行](https://github.com/FreakLee/PythonLearning/blob/main/Screenshot/Day1/5.jpg)

当然也可以利用IDLE工具打开.py文件运行。
![IDLE运行.py文件](https://github.com/FreakLee/PythonLearning/blob/main/Screenshot/Day1/6.jpg)

## 开发工具

可以使用专业的IDE [PyCharm](https://www.jetbrains.com/pycharm/)。学习阶段可使用微软的万能开发工具：VS Code的Python套餐，方便运行、调试。
![VS Code](https://github.com/FreakLee/PythonLearning/blob/main/Screenshot/Day1/7.jpg)
