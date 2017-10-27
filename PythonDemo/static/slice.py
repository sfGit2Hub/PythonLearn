#[start: end: step]
def slice_arr():
    arr = list(range(1,100))
    print('数组切片\n', arr[0:200:5])
    print('字符串切片\n','ABCDEFGHIJKLMN'[:10:2])
    print('字符串倒序\n','ABCDEFGHIJKLMN'[::-1])


slice_arr()