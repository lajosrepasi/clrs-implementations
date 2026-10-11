"""
Exercise 1.2-3
"""

n: int = 2

while True:
    alg1_time: int = 100 * n * n
    alg2_time: int = 2**n

    if alg2_time > alg1_time:
        break

    n += 1

print(n)
