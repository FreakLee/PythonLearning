
import numpy as np

#---------------------------掩码（Masking）---------------------------

# 创建掩码数组
arr = np.array([1, 2, 3, 4, 5])
mask = arr > 2
print(mask)  # [False False  True  True  True]

# 使用掩码选择元素
selected_elements = arr[mask]
print(selected_elements)  # [3 4 5]

# 使用掩码修改元素
arr[mask] = 0
print(arr)  # [1 2 0 0 0]

# 多条件掩码操作
mask1 = arr > 1
mask2 = arr % 2 == 0
combined_mask = mask1 & mask2
selected_elements = arr[combined_mask]
print(selected_elements)  # [2]

#------------------------花式索引（fancy indexing）-----------------------

# 一维花式索引
arr = np.array([1, 2, 3, 4, 5])
print(arr[[0, 2, 4]])  # [1 3 5]

# 二维花式索引
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

# 使用花式索引选择特定的列
cols = np.array([0, 2])
result = arr[:, cols]

print(result)
"""
[[1 3]
 [4 6]
 [7 9]]
"""

arr2d = arr[[0, 2], [1, 2]] # 使用花式索引
print(arr2d)  # [2 9]


# 布尔花式索引
# 使用布尔花式索引选择满足条件的元素
arr = np.array([1, 2, 3, 4, 5])

mask = np.array([True, False, True, False, False])
result = arr[mask]
print(result)  # [1 3]


#------------------------将数据导入和导出为csv文件-----------------------

# 导入CSV文件（本地文件）
# data = np.genfromtxt('/完整路径/local_example.csv', delimiter=',',dtype=None)
# print(data)


# 导出数据到CSV文件（本地文件）
# 创建一个示例数组
data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# 将数组保存为本地CSV文件
np.savetxt('output.csv', data, delimiter=',',fmt='%d')


#------------------------连接NumPy数组-----------------------

# 按列连接（水平连接）
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

# 按行连接（垂直连接）
c = np.concatenate((a, b), axis=0)

print(c)
"""
[[1 2]
 [3 4]
 [5 6]]
"""

# np.hstack()
# 按水平方向连接数组
c = np.hstack((a, b.T))

print(c)
"""
[[1 2 5]
 [3 4 6]]
"""

# np.vstack()
# 按垂直方向连接数组
c = np.vstack((a, b))

print(c)
"""
[[1 2]
 [3 4]
 [5 6]]
"""

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