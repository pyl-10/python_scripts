def generator(k):
    i = 1
    while True:
        yield i ** k
        i += 1
# yield 返回了 一个生成器

gen_1 = generator(1)
gen_3 = generator(3)
print(gen_1)
print(gen_3)


def get_sum(n):
    sum_1, sum_3 = 0, 0
    for _ in range(n):
        next_1 = next(gen_1)
        next_3 = next(gen_3)
        print('next_1 = {}, next_3 = {}'.format(next_1, next_3))
        sum_1 += next_1
        sum_3 += next_3
    print(sum_1 * sum_1, sum_3)

# (1+2+3..+n)^2 == 1^3 + 2^3 + 3^3 .. + n^3

get_sum(8)

def index_normal(l, target):
    result = []
    for i, num in enumerate(l):
        if num == target:
            result.append(i)
    return result

print(index_normal([2, 4, 6, 3, 4], 4))
