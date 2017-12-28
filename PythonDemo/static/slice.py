#[start: end: step]

class Matrix(object):
    def __init__(self, multi_arr):
        col_s = len(multi_arr[0])
        for row in multi_arr:
            if col_s == len(row):
                col_s = len(row)
            else:
                print("the array is error")
                return                
        self.rowSize = len(multi_arr)
        self.colSize = len(multi_arr[0])

def matrixMul(A, B):
    res = [[0] * len(B[0]) for i in range(len(A))]
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                res[i][j] += A[i][k] * B[k][j]
    return res

def matrixMul2(A, B):
    return [[sum(a * b for a, b in zip(a, b)) for b in zip(*B)] for a in A]

def slice_arr():
    arr = list(range(1,100))
    A = [[0,1,2],[1,2,3]]
    B = [[1,2],[2,3],[3,4]]
    matrix = Matrix(A)
    
    print("矩阵行数：", matrix.rowSize)
    print("矩阵乘法：", matrixMul2(A, B))
    print('数组切片\n', arr[0:200:5])
    print('字符串切片\n','ABCDEFGHIJKLMN'[:10:2])
    print('字符串倒序\n','ABCDEFGHIJKLMN'[::-1])

B = [[1,2],[2,3],[3,4]]
for b in zip(*B):
    print("b:", b)

slice_arr()