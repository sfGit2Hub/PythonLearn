obj = {'name': 'aaa', 'age': 20, 'id':'KNSUBTIO343'}
name = obj.get('name')
print(name)

if obj.get('id') :
    print(obj.get('id'))
else :
    print('no id')

obj.pop('name')
print(obj)

arr = [1, 2, 3, 4, 5]
s_1 = set([1, 2, 3, 4])
#s_2 = set(arr, arr, arr)
print(s_1)
print(2**3)

help(abs)