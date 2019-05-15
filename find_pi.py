import random
import math


def in_circle(x, y):
    return x**2 + y**2 < 1


def get_pi(inside, total):
    return (inside / total) * 4


# Initialize
random.seed(12345)
total = 10**7
inside_count = 0

# Generate random points within the square
for i in range(total):
    # x and y are in range [-1, 1]
    x = 2 * random.random() - 1
    y = 2 * random.random() - 1

    if in_circle(x, y):
        inside_count += 1

    # Print progress
    if i % (total//10) == 0:
        print(get_pi(inside_count, i+1))

# Print final value
print("Calculated value of Pi:", get_pi(inside_count, total))
print("    Actual value of Pi:", math.pi)