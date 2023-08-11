
import numpy as np

# -------------------------创建数组---------------------------
# 创建一维数组
arr1 = np.array([1, 2, 3, 4, 5])

# 创建二维数组
arr2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
arr2_2d = np.arange(12).reshape(4,3)  #将0-11这12个数以4行三列的方式创建二维数组，打印效果如下：
"""
[[ 0  1  2]
 [ 3  4  5]
 [ 6  7  8]
 [ 9 10 11]]
"""

# 创建三维数组
arr3_3d = np.arange(24).reshape(2,3,4)  #将0-23这24个数以shape(2,3,4)的形式创建三维数组。打印效果如下：
"""
[[[ 0  1  2  3]
  [ 4  5  6  7]
  [ 8  9 10 11]]

 [[12 13 14 15]
  [16 17 18 19]
  [20 21 22 23]]]
"""

# 创建全零数组
zeros_arr = np.zeros((3, 4))

# 创建全一数组
ones_arr = np.ones((2, 3))

# 创建指定范围的数组
range_arr = np.arange(0, 10, 2)  # 从0到10，步长为2

# 创建随机数组
random_arr = np.random.rand(3, 2)  # 3行2列的随机数组

# 创建时显示指定数组的类型
com_arr = np.array([[1,2],[3,4]], dtype=complex)  # 2行2列的复数数组


# -------------------------数组操作---------------------------
arr = np.array([1, 2, 3, 4, 5])
arr_other = np.array([2, 3, 4, 5, 6])
arr_2d = np.arange(16).reshape(4,4)
# 访问数组元素
print(arr[0])  # 输出：1
print(arr[2:4])  # 输出：[3, 4]
# 以下两种方式等价
"""
 0  1  2  3
 4  5  6  7
 8  9 10 11
12 13 14 15
"""
# 多维数组索引
print(arr_2d[1][1]) # 输出：5
print(arr_2d[1,1])  # 输出：5

# 条件筛选
filtered_arr = arr[arr > 2]
print(filtered_arr)
# 输出：[3, 4, 5]

# 布尔索引
bool_index = np.array([True, False, True, False, True])
bool_filtered_arr = arr[bool_index]
print(bool_filtered_arr)
# 输出：[1, 3, 5]

# 多维数组切片
print(arr_2d[1:2])  # 输出：[[4 5 6 7]]
print(arr_2d[0:2,1])  # 输出：[1 5]
"""
输出：
[[ 6]
 [10]]
"""
print(arr_2d[1:3,2:3]) 
"""
输出：
[[ 5  6]
 [ 9 10]]
"""
print(arr_2d[1:3,1:3]) 

# 数组运算
print(arr + 2)  # 输出：[3, 4, 5, 6, 7]
print(arr * 3)  # 输出：[3, 6, 9, 12, 15]
print(arr + arr_other)  # 输出：[3, 5, 7, 9, 11]


# ---------------插入矩阵部分操作 以作对比
# 对于大小相同的两个矩阵，我们可以使用算术运算符（+-*/）将其相加或者相乘。NumPy对这类运算采用对应位置（position-wise）操作处理
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
"""
 [1, 2]  [5, 6]    [ 6,  8]
 [3, 4]  [7, 8]    [10, 12]
"""
print(A + B)

"""
 [1, 2]  [5, 6]    [ 5, 12]
 [3, 4]  [7, 8]    [21, 32]
"""
print(A * B)

# 逆矩阵
"""
逆矩阵是一个与原矩阵相乘后得到单位矩阵的矩阵。对于一个 n×n 的方阵 A，如果存在另一个 n×n 的方阵 B，使得 A 与 B 相乘后得到单位矩阵 I（大小为 n×n），则矩阵 B 被称为 A 的逆矩阵，记作 A^(-1)。

形式化表示为：A × A^(-1) = A^(-1) × A = I

逆矩阵的存在条件是，原矩阵 A 必须是可逆的（也称为非奇异的）。如果矩阵 A 不可逆，也就是不存在与之相乘后得到单位矩阵的矩阵 B，那么我们称 A 为奇异矩阵。

逆矩阵的性质包括：

只有方阵（行数等于列数）才有可能存在逆矩阵。
逆矩阵是唯一的，如果 A 有逆矩阵，那么它的逆矩阵是唯一的。
如果 A 与 B 都是可逆矩阵，那么 A × B 也是可逆的，并且它的逆矩阵为 B^(-1) × A^(-1)。

下面输出：
[[-2.   1. ]
 [ 1.5 -0.5]]
"""
matrix = np.array([[1, 2], [3, 4]])
inverse_matrix = np.linalg.inv(matrix)
print(inverse_matrix)


# 转置
"""
[[ 0  4  8 12]
 [ 1  5  9 13]
 [ 2  6 10 14]
 [ 3  7 11 15]]
"""
print(arr_2d.T)

# 对于不同大小的矩阵，只有两个矩阵的维度同为1时（例如矩阵只有一列或一行），我们才能进行这些算术运算，在这种情况下，NumPy使用广播规则（broadcast）进行操作处理
arr_c = np.array([1, 2])
"""
 [1, 2]  [1, 2]    [2, 4]
 [3, 4]  [1, 2]    [4, 6]
"""
print(A + arr_c)

"""
 [1, 2]  [1, 2]    [1, 4]
 [3, 4]  [1, 2]    [3, 8]
"""
print(A * arr_c)


# 点积dot()
"""
 [1, 2]  [5, 6]    [19, 22]
 [3, 4]  [7, 8]    [43, 50]

 1*5 + 2*7 = 19
 3*5 + 4*7 = 43
 1*6 + 2*8 = 22
 3*6 + 4*8 = 50
"""
# 以下三种打印相同
print(np.dot(A,B))
print(A @ B)  # Python 3.5及以上版本
print(np.matmul(A, B))


# 数组形状操作
print(arr.shape)  # 输出：(5,)  
reshaped_arr = arr.reshape((5, 1))
print(reshaped_arr.shape)  # 输出：(5, 1)
"""
输出：
[[1]
 [2]
 [3]
 [4]
 [5]]
"""
print(reshaped_arr)  #注意与print(arr)的区别：[1 2 3 4 5]

orgin_arr = np.array([1, 2, 3, 4, 5,6])
print(orgin_arr.shape)  # 输出：(6,)  
"""
输出：
[[1 2 3]
 [4 5 6]]
"""
print(orgin_arr.reshape(2,3))
"""
输出：
[[1 2]
 [3 4]
 [5 6]]
"""
print(orgin_arr.reshape(3,2))


# 数组聚合操作
print(np.mean(arr)) # 输出：3.0
print(np.max(arr))  # 输出：5
print(np.sum(arr))  # 输出：15
print(np.max(arr_2d))  # 输出：15
print(np.mean(arr_2d))  # 输出：7.5

"""
 0  1  2  3
 4  5  6  7
 8  9 10 11
12 13 14 15
"""
print(np.max(arr_2d[0:3]))  # 输出：11
# 找到每行的最大值（沿列聚合）：
print(np.max(arr_2d, axis=0))  # 输出：[12 13 14 15]
# 找到每列的最小值（沿行聚合）：
print(np.min(arr_2d, axis=1))  # 输出：[ 0  4  8 12]
# 按行求和（沿列聚合）：
print(np.sum(arr_2d, axis=0))  # 输出：[24 28 32 36]
# 按列求和（沿行聚合）：
print(np.sum(arr_2d, axis=1))  # 输出：[ 6 22 38 54]


# 数组拼接
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

concatenated_arr = np.concatenate((arr1, arr2))
print(concatenated_arr)
# 输出：[1 2 3 4 5 6]

# 数组分割
arr = np.array([1, 2, 3, 4, 5, 6])
splitted_arr = np.split(arr, 3)
print(splitted_arr)
# 输出：[array([1, 2]), array([3, 4]), array([5, 6])]
