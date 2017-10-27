import pickle
import json
obj = dict(name='abel', age=24, weight='70kg')
obj_byte = pickle.dumps(obj)
f = open('./dump.txt', 'wb')
#pickle.dump(obj, f)    两种方式序列化到文件
f.write(obj_byte)
f.close()

f_o = open('./dump.txt', 'rb')
new_obj = pickle.load(f_o)
f_o.close()
print(new_obj)

json_str = '{"age": 20, "score": 88, "name": "Bob"}'
json_obj = json.loads(json_str)
print(json.dumps(new_obj), 'is string:', isinstance(json.dumps(new_obj), str))
print(isinstance(json_obj, dict))

class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score
#   不能直接序列化

def student2dict(stu):
    return {
        'name':stu.name,
        'age':stu.age,
        'score':stu.score
    }
def dict2Student(d):
    return Student(d['name'], d['age'], d['score'])

s = Student('aaa', 20, '99')
print(json.dumps(s, default=student2dict))
print(json.loads(json_str, object_hook=dict2Student))
