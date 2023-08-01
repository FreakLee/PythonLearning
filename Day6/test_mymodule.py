
import pkg_resources

#import mymodule
from mymodule import work

from SubModules import my_sub_module
# import sys
# sys.path.append('/路径/SubModules')
# import my_sub_module
# 以上两种方式都行

#mymodule.greet('Alice')
work()

my_sub_module.subWork()


# __name__属性：每个模块都有一个__name__属性，当其值是'__main__'时，表明该模块自身在运行，否则是被引入
if __name__ == '__main__':
   print('程序自身在运行')
else:
   print('我来自另一模块')


# 检查是否安装了某个第三方模块
try:
    import requests
except ModuleNotFoundError:
    print('requests module not found')
else:
    print('requests module is installed')

try:
    pkg_resources.get_distribution('requests')
except pkg_resources.DistributionNotFound:
    print('requests module not found')
else:
    print('requests module is installed')