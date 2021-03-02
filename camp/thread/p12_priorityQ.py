# 优先级队列
import queue
q = queue.PriorityQueue()

# 每个元素都是元组
# 数字越小优先级越高
# 同优先级先进先出

q.put((1, "work"))
q.put((2, "eat"))
q.put((-1, "drink"))

print(q.get())
print(q.get())
print(q.get())

# queue.LifoQueue 后进先出队列， 类似堆栈
# q.deque  双向队列