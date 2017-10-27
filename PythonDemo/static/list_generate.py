import os
from collections import Iterable

list(range(1, 11))
#[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

[x*x for x in range(1, 11)]
#[1x1, 2x2, 3x3, ..., 10x10]

[x*x for x in range(1, 11) if x % 2 == 0]
# [4, 16, 36, 64, 100]

[x+y for x in 'ABC' for y in 'DEF']
# ['AD', 'AE', 'AF', 'BD', 'BE', 'BF', 'CD', 'CE', 'CF']

[d for d in os.listdir('.')]
#列出当前目录下的所有文件

L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [s.lower() if isinstance(s, str) else s for s in L1]
# ['hello', 'world', 18, 'apple', None]

g = (x*x for x in range(0, 100))
# 生成器表达, Python一边循环一边计算的机制
print(isinstance(g, Iterable))

# 如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator
def fib(num):
    n, a, b = 0, 0, 1
    print('n', n, '\ta', a, '\tb', b)
    while n < num:
        yield b
        a, b = b, a + b
        # t = (b, a + b) # t是一个tuple
        # a = t[0]
        # b = t[1]

        n = n + 1
    return 'done'

f = fib(6)
for v in f:
    print(v)