# # 容器序列的拷贝问题

# old_list = [ i for i in range(1, 11)]
# new_list = old_list
# new_list1 = list(old_list)

# # 切片操作
# new_list2 = old_list[:]

# # 嵌套对象
# old_list.append([11, 12])

# print(new_list)
# print(new_list1)
# print(new_list2)
# print(old_list)

# print(id(new_list))
# print(id(new_list1))
# print(id(new_list2))
# print(id(old_list))

# import copy
# new_list4 = copy.copy(old_list)
# new_list5 = copy.deepcopy(old_list)

# assert new_list4 == new_list5
# assert new_list4 is new_list5

# 命名元组
import collections
Point = collections.namedtuple('Point', ['x', 'y'])
p = Point(11, y=22)
print(p[0] + p[1])
x, y = p
print(p.x + p.y)
print(p)

# 计数器
from collections import Counter
mystring = ['a', 'b', 'c', 'd', 'e', 'f', 'b', 'b', 'f', 'e']
# 取得频率最高的前三个值
cnt = Counter(mystring)
print(cnt.most_common(3))
print(cnt['a'])

# 双向队列
from collections import deque
d = deque('uvw')
d.append('xyz')
d.appendleft('rst')
print(d)
# 容器序列的拷贝问题

old_list = [ i for i in range(1, 11)]
new_list = old_list
new_list1 = list(old_list)

# 切片操作
new_list2 = old_list[:]

# 嵌套对象
old_list.append([11, 12])

print(new_list)
print(new_list1)
print(new_list2)
print(old_list)

print(new_list)
print(new_list1)
print(new_list2)
print(old_list)
