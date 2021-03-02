import redis

client = redis.Redis(host='localhost', password='7PqfHu7mLK0Q')

# client.hset('vip_user', '1001', 1)
# client.hset('vip_user', '1002', 1)
# client.hdel('vip_user', '1002')

# print(client.hexists('vip_user', '1001'))

#  添加多个键值对
# client.hmset('vip_user', {'1003':1, '1004':1})

# 读取值 hkeys, hget, hmget, hgetall
field = client.hkeys('vip_user')
print(field)
field2 = client.hget('vip_user', '1001')
print(field2)
print(client.hget('vip_user', '1001'))
print(client.hgetall('vip_user'))

