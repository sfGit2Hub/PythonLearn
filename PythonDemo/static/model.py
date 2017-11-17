class Field(object):
    def __init__(self, name, column_type):
        self.name = name
        self.column_type = column_type

    def __str__(self):
        return '<%s, %s, %s>' % (self.__class__.__name__, self.name, self.column_type)


class StringField(Field):
    def __init__(self, name):
        # 显示调用父类初始化
        super(StringField, self).__init__(name, 'varchar(255)')


class IntegerField(Field):
    def __init__(self, name):
        super(IntegerField, self).__init__(name, 'bigint')


# __new__()方法接收到的参数依次是：
#     1.当前准备创建的类的对象；
#     2.类的名字；
#     3.类继承的父类集合；
#     4.类的方法集合。
class ModelMetaClass(type):
    def __new__(cls, name, bases, attrs):
        if name == 'Model':
            return type.__new__(cls, name, bases, attrs)
        print('Found model %s' % name)
        mappings = dict()
        for k, v in attrs.items():
            if isinstance(v, Field):
                print('Found mapping: %s ==> %s' % (k, v))
                mappings[k] = v
        for k in mappings.keys():
            attrs.pop(k)
        attrs['__mappings__'] = mappings    # 保存属性和列的映射关系
        attrs['__table__'] = name           # 假设表名和类名一致
        return type.__new__(cls, name, bases, attrs)


class Model(dict, metaclass=ModelMetaClass):
    def __init__(self, **kwargs):
        super(Model, self).__init__(**kwargs)

    def __getattr__(self, item):
        try:
            return self[item]
        except KeyError:
            raise AttributeError(r"'Model' object has no attribute '%s'" % item)

    def __setattr__(self, key, value):
        self[key] = value

    def insert(self):
        fields = []
        params = []
        args = []
        for k, v in self.__mappings__.items():
            fields.append(v.name)
            print(v.column_type)
            params.append('%s')
            args.append(getattr(self, k, None))
        sql = 'insert into %s (%s) VALUES (%s)' % (self.__table__, ','.join(fields), ','.join(params))
        print('SQL: %s' % sql)
        print('ARGS: %s' % str(args))


class User(Model):
    # 定义类的属性到列的映射：
    id = IntegerField('id')
    name = StringField('username')
    email = StringField('email')
    password = StringField('password')
    age = 3


if __name__ == '__main__':
    u = User(id=1, name='1', email='test@gmail.com', passd='Aa123456')
    u.insert()
