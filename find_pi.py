import random


def in_circle(x, y):
    return x**2 + y**2 < 1

random.seed(12345)
total = 10**7
inside_count = 0
for i in range(total):
    x = 2 * random.random() - 1
    y = 2 * random.random() - 1
    if in_circle(x, y):
        inside_count += 1
    if i % 1000000 == 0:
        print((inside_count / (i+1)) * 4)

pi = (inside_count / total) * 4

print(pi)
