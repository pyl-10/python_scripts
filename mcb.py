import mysql.connector

# 打开数据库连接
db = mysql.connector.connect(host="localhost", user="root", passwd="", database="heroDB")
# 获取操作游标
cursor = db.cursor()

# # 执行sql语句
# cursor.execute("SELECT VERSION()")
# # 获取一条语句
# data = cursor.fetchone()
# print(data)
# print("版本为{}".format(data))
# # 关闭游标 和 数据库连接
# cursor.close()
# db.close()

# # 插入 数据
# sql = "INSERT INTO player (team_id, player_name, height) VALUES (%s, %s, %s)"
# val = (1003, "约翰史密斯", 2.08)
# cursor.execute(sql, val)
# db.commit()
# print(cursor.rowcount, "插入成功")

# # 关闭游标 和 数据库连接
# cursor.close()
# db.close()

# 查询身高大于等于2.08的球员
# sql = "SELECT player_id, player_name, height FROM player WHERE height>=2.08"
# cursor.execute(sql)
# data = cursor.fetchall()
# for each_player in data:
#     print(each_player)

sql = "UPDATE player SET height = %s WHERE player_name = %s"
val = (2.09, "约翰史密斯")
cursor.execute(sql, val)
db.commit()
print(cursor.rowcount, "记录被修改")
# 关闭游标 和 数据库连接
cursor.close()
db.close()
