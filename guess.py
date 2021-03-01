import random

# 猜三次
for i in range(3):
    guess = ''
    while guess not in ('heads', 'tails'):
        print('Guess the coin toss!Enter heads or tails:')
        guess = input()

    toss = random.randint(0, 1)
    if toss == 0:
        toss = 'tails'
    elif toss == 1:
        toss = 'heads'

    if toss == guess:
        print('恭喜你,只用了' + str(i+1) + '次就猜中了')
        continue
    else:
        print('你还有' + str(2-i) + '次机会')