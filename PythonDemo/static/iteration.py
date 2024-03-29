from collections import Iterable
from collections import Iterator

print('is Iterable:', isinstance('abc', Iterable))
print('is Iterator:', isinstance('abc', Iterator))
obj = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4
}
for k in obj.keys():
    print(k)

for k, v in obj.items():
    print(k, ':', v)

for index, value in enumerate(['A', 'B', 'C']):
    print(index, value)

for x, y in [(1, 1), (2, 4), (3, 9)]:
    print(x, y)
    
# 凡是可作用于for循环的对象都是Iterable类型；
# 凡是可作用于next()函数的对象都是Iterator类型，它们表示一个惰性计算的序列；
# 集合数据类型如list、dict、str等是Iterable但不是Iterator，不过可以通过iter()函数获得一个Iterator对象。