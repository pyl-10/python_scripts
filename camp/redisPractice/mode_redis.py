import redis

client = redis.Redis(host='localhost', password='7PqfHu7mLK0Q')
print(client.keys())

for key in client.keys():
    print(key.decode())
