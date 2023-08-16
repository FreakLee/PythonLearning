# Day12-NumPy（进阶篇）

## 掩码（Masking）
在NumPy中，掩码（Masking）是一种基于条件筛选数据的机制，它允许我们根据某些条件对数组中的元素进行选择、过滤或操作。通过创建一个布尔数组（即掩码数组），我们可以根据这个数组的值来指示哪些元素应该被选中或操作。

1. 创建掩码数组：
我们可以使用比较运算符（如>、<、==等）和逻辑运算符（如&、|、~等）创建掩码数组。
``` py
import numpy as np

arr = np.array([1, 2, 3, 4, 5])
mask = arr > 2
print(mask)  # [False False  True  True  True]
```
在上面的示例中，我们创建了一个布尔数组mask，其中元素大于2的位置为True，否则为False。

2. 使用掩码选择元素：
我们可以使用掩码数组来选择满足特定条件的元素。
``` py
import numpy as np

arr = np.array([1, 2, 3, 4, 5])
mask = arr > 2
selected_elements = arr[mask]
print(selected_elements)  # [3 4 5]
```
在上面的示例中，我们使用掩码数组mask来选择数组arr中大于2的元素，并将它们存储在selected_elements中。

3. 使用掩码修改元素：
我们可以使用掩码数组来修改满足特定条件的元素。
``` py
import numpy as np

arr = np.array([1, 2, 3, 4, 5])
mask = arr > 2
arr[mask] = 0
print(arr)  # [1 2 0 0 0]
```
在上面的示例中，我们使用掩码数组mask来将数组arr中大于2的元素替换为0。

4. 多条件掩码操作：
我们可以使用逻辑运算符（如&、|、~）结合多个掩码数组进行复杂的条件筛选操作。
``` py
import numpy as np

arr = np.array([1, 2, 3, 4, 5])
mask1 = arr > 2
mask2 = arr % 2 == 0
combined_mask = mask1 & mask2
selected_elements = arr[combined_mask]
print(selected_elements)  # [4]
```
在上面的示例中，我们使用两个掩码数组mask1和mask2来筛选数组arr中大于2且为偶数的元素，并将满足条件的元素存储在selected_elements中。

掩码操作在NumPy中非常有用，它提供了一种灵活的方式来处理和操作数组数据。无论是选择、过滤还是修改元素，掩码机制都能帮助我们轻松实现这些操作。

## 花式索引（fancy indexing）
NumPy中的花式索引（fancy indexing）是一种通过整数数组或布尔数组来访问和操作数组元素的机制。它提供了一种灵活且强大的方式来选择和修改数组中的特定元素或子集。花式索引可以用于一维、二维甚至多维数组。在NumPy中，有两种常见的花式索引方式：整数花式索引和布尔花式索引。

1、一维花式索引

在一维数组中，花式索引允许我们使用整数数组来选择和操作特定的元素。
``` py
import numpy as np

# 创建一个一维数组
arr = np.array([1, 2, 3, 4, 5])

# 使用花式索引选择特定的元素
result = arr[[0, 2, 4]]

print(result)
# 输出： [1 3 5]
```

2、二维花式索引

在二维数组中，花式索引可以用于选择行、列或特定的元素。
``` py
import numpy as np

# 创建一个二维数组
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# 使用花式索引选择特定的行
rows = np.array([0, 2])
result = arr[rows, :]

print(result)
"""
[[1 2 3]
 [7 8 9]]
"""
```
在这个例子中，使用整数数组[0, 2]作为行索引，通过花式索引选择了数组arr中的第一行和第三行。

``` py
import numpy as np

# 创建一个二维数组
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# 使用花式索引选择特定的列
cols = np.array([0, 2])
result = arr[:, cols]

print(result)
"""
[[1 3]
 [4 6]
 [7 9]]
"""
```
在这个例子中，使用整数数组[0, 2]作为列索引，通过花式索引选择了数组arr中的第一列和第三列。

3、布尔花式索引

除了整数数组之外，布尔数组也可以用作花式索引，用于根据某些条件选择和操作数组元素。

```py
import numpy as np

# 创建一个一维数组
arr = np.array([1, 2, 3, 4, 5])

# 使用布尔花式索引选择满足条件的元素
mask = np.array([True, False, True, False, False])
result = arr[mask]

print(result) # [1 3]
```
在这个例子中，使用布尔数组[True, False, True, False, False]作为索引，通过布尔花式索引选择了数组arr中满足条件的元素。

## 处理CSV文件

1、导入CSV文件（本地文件）
``` py
import numpy as np

data = np.genfromtxt('file_path', delimiter=',',dtype=None)
print(data)
```

2、导入CSV文件（远程文件）
``` py
import numpy as np

# 从远程CSV文件加载数据
url = 'https://example.com/data.csv'
data = np.genfromtxt(url, delimiter=',', skip_header=1)
```

3、导出数据到CSV文件（本地文件）
``` py
import numpy as np

# 创建一个示例数组
data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# 将数组保存为本地CSV文件
np.savetxt('output.csv', data, delimiter=',',fmt='%d')
```

4、导出数据到CSV文件（远程文件）：
要将NumPy数组保存为远程的CSV文件，可以使用numpy.savetxt()函数，并使用适当的库（如urllib）将数据发送到远程服务器。以下是一个示例：

``` py
import numpy as np
import urllib

# 创建一个示例数组
data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# 将数组保存为远程CSV文件
url = 'https://example.com/save_data.php'
np.savetxt(url, data, delimiter=',', fmt='%d', header='Col1,Col2,Col3')
```
在上述示例中，创建了一个示例数组data，然后使用np.savetxt()函数将其以逗号分隔的格式保存到远程服务器的URL。还指定了格式字符串fmt='%d'用于保存整数数据，并通过header参数指定了列标题。

## 连接NumPy数组
1、np.concatenate()

* 按列连接（水平连接）
``` py
import numpy as np

# 创建两个示例数组
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6]])

# 按列连接数组
c = np.concatenate((a, b.T), axis=1)

print(c)
"""
[[1 2 5]
 [3 4 6]]
"""
```

* 按行连接（垂直连接）
``` py
import numpy as np

# 创建两个示例数组
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6]])

# 按列连接数组
c = np.concatenate((a, b), axis=0)

print(c)
"""
[[1 2]
 [3 4]
 [5 6]]
"""
```
请注意，要连接的数组在连接方向上的维度应该是相同的，除了连接维度之外，其他维度的形状应该保持一致。

2、np.vstack()和np.hstack()

``` py
import numpy as np

# 创建两个示例数组
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6]])

# 按水平方向连接数组
c = np.hstack((a, b.T))

print(c)
"""
[[1 2 5]
 [3 4 6]]
"""

# 按垂直方向连接数组
c = np.vstack((a, b))

print(c)
"""
[[1 2]
 [3 4]
 [5 6]]
"""
```

3、np.r_和np.c_
``` py
import numpy as np

# 创建两个示例数组
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6]])

# 按列连接数组
c = np.c_[a, b.T]

print(c)
"""
[[1 2 5]
 [3 4 6]]
"""

# 按行连接数组
c = np.r_[a, b]

print(c)
"""
[[1 2]
 [3 4]
 [5 6]]
"""
```