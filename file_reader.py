import redis
import time

#  直连
# r = redis.Redis(host="localhost", port=6379)

#  连接池 (推荐)
pool = redis.ConnectionPool(host="localhost", port=6379)
# r = redis.Redis(connection_pool=pool)
r = redis.StrictRedis(connection_pool=pool)
# 记录当前时间
time1 = time.time()
# 一万次写
for i in range(10000):
    data = {"username":"zhangfei", "age":28}
    r.hset("users"+str(i), data)
# 统计写时间
delta_time = time.time()-time1
print(delta_time)
# 统计当前时间
time2 = time.time()
# 一万次读
for i in range(10000):
    result = r.hmget("users"+str(i), ["username", "age"])
# 统计读时间
delta_time2 = time.time()-time2
print(delta_time2)



