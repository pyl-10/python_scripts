import pymysql

# 打开数据库连接
db = pymysql.connect('localhost', 'root', '', 'testdb')

try:
    # 使用 cursor（） 方法创建一个游标对象cursor
    with db.cursor() as cursor:
        sql = 'select version()'
        # 使用 execute（） 方法执行 sql 查询
        cursor.execute(sql)
        res = cursor.fetchone()
    db.commit()
except Exception as e:
    print(f'fetch error {e}')
finally:
    # 关闭数据库
    db.close()

print(f'database version:{res}')