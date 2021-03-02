import redis

client = redis.Redis(host='localhost', password='7PqfHu7mLK0Q')

# client.set('key', 'value3', nx=True)
# client.append('key', 'value4')
# res = client.get('key')
# print(res)
# print(res.decode())

client.set('key2', '100')
res2 = client.incr('key2')  # +1
print(res2)
res3 = client.decr('key2')  # -1
print(res3)
