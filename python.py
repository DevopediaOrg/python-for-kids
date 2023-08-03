  for i in range(1, 11): print(i)


squares = [i**2 for i in range(1, 11)]
print(squares)


length = len("Hello, World!")
print(length)


count = [1, 1, 2, 3, 3, 3].count(3)
print(count)

total_sum = sum([1, 2, 3, 4, 5])
print(total_sum)


reversed_str = "Hello, World!"[::-1]
print(reversed_str)


unique_list = list(set([1, 2, 2, 3, 3, 4]))
print(unique_list)

import math
factorial = math.factorial(5)
print(factorial)


all_positive = all(num > 0 for num in [1, 2, 3, 4, 5, 5, 5, 6)
print(all_positive)
