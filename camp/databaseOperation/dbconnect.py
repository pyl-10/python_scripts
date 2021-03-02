import pymysql
from dbconfig import read_db_config

dbserver = read_db_config()
db = pymysql.connect(**dbserver)

try:
    # 使用cursor（）方法创建一个游标对象 cursor
    with db.cursor() as cursor:
        sql = "select version()"
        # 使用 execute() 方法执行sql查询
        cursor.execute(sql)
        res = cursor.fetchone()
    db.commit()
except Exception as e:
    print(f"fetch error {e}")
finally:
    db.close()

print(f"database version : {res}")