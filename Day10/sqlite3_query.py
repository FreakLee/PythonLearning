import sqlite3

# 连接到数据库（如果不存在则创建）
conn = sqlite3.connect('test.db')

# 创建游标对象
cursor = conn.cursor()

# 执行 SQL 查询
cursor.execute('SELECT * FROM users')

# 提取查询结果
results = cursor.fetchall()

# 处理查询结果
print(results)

# 关闭游标和连接
cursor.close()
conn.close()