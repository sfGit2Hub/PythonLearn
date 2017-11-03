import time

start_time = time.clock()

'''
#   空循环1000万次 300+毫秒
#   Java空循环1000万次 2、3毫秒，性能差别大
for i in range(10000*1000):
    pass
'''

#   while 循环100万次  80+毫秒
#   java 同样情况  1--3毫秒
i=0
while i<1000*1000:
    i = i + 1
end_time = time.clock()
print(end_time - start_time)