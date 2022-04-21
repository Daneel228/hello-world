import random
from random import randint
from random import randint as rd
import numpy as np
print("Вариант 1")
matrix = [[2],8]
result = [matrix[i][j] for i in range(len(matrix)-1) for j in range(i+1, len(matrix[i])) if matrix[i][j] > 0]
print('Сумма положительных элементов —', sum(result), '\nколичество таких элементов —', len(result))
print()
print("Вариант 3")
a = [[randint(1, 10) for i in range(5)] for j in range(4)]
for row in a:
    print(row)
print()
max_elem = a[0][0]
ie = je = 0
for i in range(len(a)):
    for j in range(len(a[0])):
        if a[i][j] > max_elem:
            max_elem = a[i][j]
            ie = i 
            je = j 
a[0], a[ie] = a[ie], a[0]
a[0][0], a[0][je] = a[0][je], a[0][0]
for row in a:
    print(row)
print()
print("Вариант 4")
matrix = [[random.randint(-10, 10) for _ in range(3)] for _ in range(3)]
for row in matrix:
    print(row)
s=[]
for i in range(len(matrix)):
    s.append(sum(matrix[i]))
print("Строка с наибольшей суммой:",matrix[s.index(max(s))],"Сумма элементов:",max(s),"Строка с наименьшей суммой:",matrix[s.index(min(s))],"Сумма элементов:",min(s))
print()
print("Вариант 5")
arr = [[rd(2, 10) for i in range(3)] for j in range(3)]
for i in arr :
    print(i)
print()
for row in arr :
    rmin = min(row)
    row = [(1 if rmin % 2 else 0) if j == rmin else j for j in row]
    print(row)
print()
print("Вариант 6")
n = 3
b = [[randint(1,10) for i in range(n)] for j in range(n)]
for i in b:
    print(i)
print()
a = sum(b, [])
max1 = max(a[::n+1])
max2 = max(a[n-1::n-1][:n])
if max1 > max2:
    i1 = j1 = a[::n+1].index(max1)
else:
    i1 = a[n-1::n-1][:n].index(max2)
    j1 = n - 1 - i1
b[n//2][n//2], b[i1][j1] = b[i1][j1], b[n//2][n//2]
for i in b:
    print(i)
print()
print("Вариант 8")
N = 3
k = 1
print("k=",k)
a = [[rd(2, 10) for i in range(n)] for j in range(n)]
for row in a:
    print(row)
for n in range(0, len(a)):
    print(a[k, n],'/',a[n,n], '=',  a[k,n] / a[n, n])
print()
print("Вариант 10.1")
matr = [[rd(2, 10) for i in range(3)] for j in range(3)]
for i in matr :
    print(i)
print(*[max(row) for row in matr if row == sorted(row) or row == sorted(row, reverse=True)])
print()
print("Вариант 10.2")
k = 2
d = [[random.randint(-10, 10) for _ in range(4)] for _ in range(4)]
for row in d:
    print(row)
print("Элементы в порядке возростания:")
for i in d:
    print(sorted(i, key = d[k-1].sort()))
print()
print("Вариант 11")
matrix = [[randint(-10, 10) for j in range(3)] for i in range(3)]
for row in matrix:
    print(row)
min_ = [min(row) for row in matrix]
ind_row_with_min = min_.index(min(min_))
print(ind_row_with_min)
print('min: {}'.format(sum(matrix[ind_row_with_min])))
print()
print("Вариант 12")
arr = [[-6, -1, -1, 2], [-1, -8, -1, -5], [-1, -8, -8, -8], [2, -8, -4, 0]]
for i in arr :
    print(i)
print()
n = 4
arr_rev = list(map(list,zip(*arr)))
for i in range(n) :
    for j in range(n) :
        if arr[i] == arr_rev[j] :
            print(i+1, 'строка и ', j+1, 'столбец равны')
