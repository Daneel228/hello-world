import math
print("Задача 7")
print("Вариант 1.1")
def area(figure, data):
    if figure == 'круг':
        res = 3.14*(data[0]**2)
    if figure == 'квадрат':
        a,b = data
        res = a*b
    if figure == 'треугольник':
        a,b = data
        res = (a*b)/2
    return ' Площадь {} = {}'.format(figure, res)
figure =input('Фигуры (круг, квадрат, треугольник): ')
data = [ float(i) for i in input('Размеры: ').rsplit()]
print(area(figure, data))
print()

print("Вариант 1.2")
from functools import reduce
from operator import mul
print("1 массив")
spisok = [16, 15, 9, 14, 13]
print(spisok)
result = reduce(mul, spisok)
print("произведение: ", result)
result2 = sum(spisok) / len(spisok)
print("ср. арифметическое: ", result2)

print("2 массив")
spisok2 = [34, 2, 31, 13, 0]
print(spisok2)
result2 = reduce(mul, spisok2)
print("произведение: ", result2)
result22 = sum(spisok2) / len(spisok2)
print("ср. арифметическое: ", result22)

print("3 массив")
spisok3 = [104, 25, 7, 17, 2]
print(spisok3)
result3 = reduce(mul, spisok3)
print("произведение: ", result3)
result23 = sum(spisok3) / len(spisok3)
print("ср. арифметическое: ", result23)
print()

print("Вариант 2")
s1 = [float(i) for i in input("Введите две стороны через пробел для 1-го прямоугольника: ").split()]
s2 = [float(i) for i in input("Введите две стороны через пробел для 2-го прямоугольника: ").split()]
s3 = [float(i) for i in input("Введите две стороны через пробел для 3-го прямоугольника: ").split()]
print('S1 =',s1[0]*s1[1])
print('S2 =',s2[0]*s2[1])
print('S3 =',s3[0]*s3[1])
print()

print("Вариант 3")
triangl1_kat1 = 3
triangl1_kat2 = 4
triangl2_kat1 = 5
triangl2_kat2 = 6
print('Катеты первого треугольника',triangl1_kat1, triangl1_kat2)
print('Катеты второго треугольника',triangl2_kat1, triangl2_kat2)
gip1 = math.sqrt(triangl1_kat1 ** 2 + triangl1_kat2 ** 2)
gip2 = math.sqrt(triangl2_kat1 ** 2 + triangl2_kat2 ** 2)
print(f'Гиппотенуза первого треугольника: {gip1}')
print(f'Гиппотенуза второго треугольника: {gip2}')
if gip1 > gip2:
    print('Гиппотенуза первого треугольника больше')
else:
    print('Гиппотенуза второго треугольника больше')
print()

print("Вариант 5.1")
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
a, b, c, d = map(int, input('A, B, C, D = ').split())
x = a * d
y = b * c
t = gcd(x, y)
print(x // t, '/', y // t, sep='')
print()

print("Вариант 5.2")
n = int(input('n = '))
for i in range(1,n+1):
   if n % i == 0:
       print(i,end=" ")
print()

print("Вариант 6")
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a 
a = int(input('a = '))
b = int(input('b = '))
print(gcd(a,b))
print((a * b) // gcd(a,b))
print()

print("Вариант 8.1")
def check(num):
    for d in str(num):
        if d == '0' or num%int(d):
            return False
    return True
for i in range(1, int(input()) + 1):
    if check(i):
        print(i)
print()

print("Вариант 8.2")
def func1(a):
    a[0], a[-1] = a[-1], a[0]
    return a
n = int(input('m = '))
a = list(map(int, input('в одну строку через пробел ').split(maxsplit = n)))
print(a)
print(func1(a))
print()

print("Вариант 9")
def f(n):
    s = 0
    while n > 0:
        s += n % 10
        n = n // 10
    return s
c = int(input("Введите число: "))
k = 0
while c > 0:
    c -= f(c)
    k += 1
print("Через " + str(k) + " действий")
print()

print("Вариант 11.1")
from math import sqrt
def isPrime(x):
    return all(x % i != 0 for i in range(2, int(sqrt(x)+1)))
def isTwin(x):
    return isPrime(x) and (isPrime(x-2) or isPrime(x+2))
n = 10
print(*filter(isTwin, [x for x in range(n, 2*n+1)]))
print()

print("Вариант 11.2")
from random import randint as rd
def arrmax(arr) :
    amax = arr[0][0]
    n = len(arr)
    for i in range(n) :
        if max(arr[i]) > amax :
            amax = max(arr[i])
    return amax
def arrprint(a, b) :
    for i in a :
        print(*i)
    print()
    for i in b :
        print(*i)
    print()
na = 6
ma = 4
nb = 3
mb = 5
a = [[rd(1,50) for i in range(ma)] for j in range(na)]
b = [[rd(51,100) for i in range(mb)] for j in range(nb)]
arrprint(a,b)
amax = arrmax(a)
bmax = arrmax(b)
for i in range(len(a)) :
    for j in range(len(a[i])) :
        a[i][j] = bmax if a[i][j] == amax else a[i][j]
for i in range(len(b)) :
    for j in range(len(b[i])) :
        b[i][j] = amax if b[i][j] == bmax else b[i][j]
arrprint(a,b)
print()

print("Вариант 12")
def divisors(number):
    return sum(x for x in range(1, number // 2 + 1) if number % x == 0)
pairs = {}
for i in range(2, 10001):
    sum_div = divisors(i)
    if sum_div != 1:
        if i in pairs:
            num1, num2 = i, pairs[i]
            if divisors(num1) == num2:
                print(*([num2, num1]))
        else:
            pairs[sum_div] = i
print()

print("Вариант 13.1")
k = 10
for i in range(1,k):
    n = len(str(i))
    res = sum((int(j) ** n for j in str(i)))
    if res - i == 0:
        print(res)
print()

print("Вариант 13.2")
def acos(x, y) :
    return x  / ((x * x + y * y) ** 0.5)
x1, x2 = map(float,input("Введи 1 координату x,y" ).split())
y1, y2 = map(float,input("Введи 2 координату x,y" ).split())
z1, z2 = map(float,input("Введи 3 координату x,y" ).split())
res = [x1, x2]
acosx = acos(x1, x2)
acosy = acos(y1, y2)
if acosy > acosx :
    acosx = acosy
    res = [y1, y2]
acosz = acos(z1, z2)
if acosz > acosx :
    acosz = acosz
    res = [z1, z2]
print(*res)
print()

print("Вариант 15")
n = 100
lst = [True for _ in range(n+1)]
i = 1
while 2*i*(i + 1) < n:
    j = i
    while j <= (n - i) / (2*i + 1):
        lst[2*i*j + i + j] = False
        j = j + 1
    i = i + 1
for i in range(1, n+1):
    elem = lst[i]
    if elem:
        prime = 2*i + 1
        if prime > n: break
        a = bin(prime)[2:]
        b = bin(prime)[2:][::-1]
        if a == b:
            print(prime, end=' ')

































