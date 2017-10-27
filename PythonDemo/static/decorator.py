import functools
import datetime
def log(fun):
    def wapper(*args, **kw):
        print('1-call function %s()' % fun.__name__)
        return fun(*args, **kw)
    return wapper

def log2(fun):
    @functools.wraps(fun)
    def wapper(*args, **kw):
        print('2-call function %s()' % fun.__name__)
        return fun(*args, **kw)
    return wapper


def log3(text):
    def decorator(fun):
        @functools.wraps(fun)
        def wapper(*args, **kw):
            print('%s-call function %s()' % (text, fun.__name__))
            return fun(*args, **kw)
        return wapper
    return decorator


@log
@log2
@log3('log3')
def now():
    print('2017-10-25')

now()


#偏移函数，基于functools.partial

#参数带关键字
int2 = functools.partial(int, base=2)
print('二进制数字转化:', int2('1000'))

#参数带默认值
max2 = functools.partial(max, 10)
arr = [0, 5, 9]
arr2 = [11, 12, 16]
print('max2 funtion:', max2(*arr))