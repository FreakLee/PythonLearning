import sqlite3

# 连接到数据库（如果不存在则创建）
conn = sqlite3.connect('test.db')

# 创建游标对象
cursor = conn.cursor()

# 创建user表
cursor.execute('create table users (id varchar(20) primary key, name varchar(20))')

# 继续执行一条SQL语句，插入一条记录:
cursor.execute('insert into users (id, name) values (\'1\', \'Bob\')')

# 通过rowcount获得插入的行数:
cursor.rowcount

# 提交事务:
conn.commit()
# 关闭Cursor:
cursor.close()
# 关闭Connection:
conn.close()
