# 问题1 a,b,c 三个id 是否相同
a = 123
b = 123
c = a
print(id(a))
print(id(b))
print(id(c))

# 问题2 a,b,c 的值分别是多少
a = 456
print(id(a))
c = 789
c = b = a

# 问题3 x,y的值分别是什么
x = [1, 2, 3]
y = x
x.append(4)
print(x)
print(y)

# 问题4 a,b的值分别是多少
a = [1, 2, 3]
b = a
a = [4, 5, 6]

# 问题5 a,b的值分别是多少
a = [1, 2, 3]
b = a
a[0], a[1], a[2] = 4, 5, 6