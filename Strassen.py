import numpy as np


def brute_force(A, B):
    n, m, p = A.shape[0], A.shape[1], B.shape[1]
    C = np.array([[0]*p for i in range(n)])
    for i in range(n):
        for j in range(p):
            for k in range(m):
                C[i][j] += A[i][k]*B[k][j]
    return C


def split(matrix):
    n = len(matrix)
    return matrix[:n//2, :n//2], matrix[:n//2, n//2:], matrix[n//2:, :n//2], matrix[n//2:, n//2:]


def strassen(A, B):
    if len(A) == 1:
        return A*B
    a, b, c, d = split(A)
    print(a, b, c, d)
    e, f, g, h = split(B)
    p1 = strassen(a+d, e+h)
    p2 = strassen(d, g-e)
    p3 = strassen(a+b, h)
    p4 = strassen(b-d, g+h)
    p5 = strassen(a, f-h)
    p6 = strassen(c+d, e)
    p7 = strassen(a-c, e+f)
    C11 = p1 + p2 - p3 + p4
    C12 = p5 + p3
    C21 = p6 + p2
    C22 = p5 + p1 - p6 - p7
    C = np.vstack((np.hstack((C11, C12)), np.hstack((C21, C22))))
    return C


A = np.array([
    [2]
])
B = np.array([
    [5]
])
A = np.array([
    [1, 2, 5, 4],
    [2, 2, 0, 4],
    [3, 1, 1, 5],
    [2, 2, 2, 4]
])
B = np.array([
    [0, 1, 3, 4],
    [1, 1, 1, 4],
    [4, 2, 3, 5],
    [3, 2, 4, 4]
])
# 1st argument --> numbers ranging from 0 to 99,
# 2nd argument, row = 256, col = 256
# A = np.random.randint(100, size=(256, 256))
# B = np.random.randint(100, size=(256, 256))
print(len(A))
print(strassen(A, B))
print(brute_force(A, B))
n = 6
print(n % 2)
print(n // 2)
