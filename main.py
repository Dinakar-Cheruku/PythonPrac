#print("lorem ipsum bismillah abdhullah")

# for c in range(2,30,4):
#     print(c)
# else:
#     print("done")

import time
def fib(n):
    a, b = 0, 1
    for _ in range(n):
        print(a)
        a, b = b, a + b

s = time.time()
fib(1000)
e = time.time()

print(e - s, "seconds")


