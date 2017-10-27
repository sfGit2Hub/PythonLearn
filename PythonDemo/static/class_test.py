from enum import Enum, unique


class Person(object):

    # 定义一个特殊的__slots__变量，来限制该class实例能添加的属性
    #__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的
    #__slots__ = ('name', 'age', 'weight', 'hight') # 用tuple定义允许绑定的属性名称

    # 前后都是双下划线
    # 有了__init__方法，在创建实例的时候，就不能传入空的参数了，必须传入与__init__方法匹配的参数，但self不需要传，Python解释器自己会把实例变量传进去
    # 变量名类似__xxx__的，也就是以双下划线开头，并且以双下划线结尾的，是特殊变量，特殊变量是可以直接访问的，不是private变量，所以，不能用__name__、__score__这样的变量名
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def toStr(self):
        return 'name:' + self.__name + '\tage:' + str(self.__age)

    def __str__(self):
        return 'name:' + self.__name + '\tage:' + str(self.__age)

    # 利用@property 装饰器可以实现 setter getter方法
    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__age = age


class Runable(object):
    def run(self):
        print('I can run')


class Studen(Person, Runable):
    pass


class Month(Enum):
    Sun = 0
    Mon = 1
    Tue = 2
    Wed = 3


def set_name(self, name):
    self._Person__name = name

# 利用 type 创建类对象


def fn(self):
    # 至少要有一个参数 self
    print('hello world!')


Hello = type('Hello', (object,), dict(
    sayHello=lambda self: print('hello world!')))

if __name__ == '__main__':
    Person.set_name = set_name
    p = Person('abel', 24)
    print(p.toStr())
    # print(dir(Person))
    # print(p.__name)
    # 访问内部变量
    print(p._Person__name)
    p.set_name('AAA')
    p.age = 18
    print(p)

    stu = Studen('Jack', 20)
    stu.run()
    print(stu)

    print(Month.Mon)

    h = Hello()
    h.sayHello()
