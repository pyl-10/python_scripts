import redis

client = redis.Redis(host='localhost', password='7PqfHu7mLK0Q')

# print(client.sadd('redis_set_demo', 'new_data'))
# client.spop('redis_set_demo')
client.smembers('redis_set_demo')

# 交集
client.sinter('set_a', 'set_b')

# 并集
client.sunion('set_a', 'set_b')

# 差集
client.sdiff('set_a', 'set_b')