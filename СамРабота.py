print("Практическое задание")
print("1.")
print ("Python work!")
print()
print("2.")
num=5
print (num)
print()
print("3.")
# print("Comment me :)")
print()
print("4.")
number = 2
print(number ** 3)
print()
print("5.")
getSix = 1467 // 6
print(getSix)
print()
print("6.")
string = "Data"
mult = string * 4
print(mult)
print()
print("7.")
if number % 2 == 0:
    print("Yes")
print()
print("8.")
i = 4
while i <= 13:
    if i != 7 and i != 11:
        print(i ** 2)
    i += 1
print()
print("Нахождение числа")
a = input("Введите число: ")
n1 = int(a)
n2 = int(a * 2)
print (n1 + n2)
print()
print("Работа с переменными")
num = 46
word = "string"
word *= 5
print(num)
print(word)
print()
print("Простые переменные")
x = 5
symbol = 'F'
word = "Привет"
d = 90.2
CONST = 67
print(word)
print()
print("Разделение числа на символы")
number = int(input("Введите число с 4 цифрами: "))
n1 = round(number // 1000 % 10)
n2 = round(number // 100 % 10)
n3 = round(number // 10 % 10)
n4 = round(number % 10)
print(n1, ",", n2, ",", n3, ",", n4)
print()
print("Получение данных от пользователя")
name = input("Ваше имя: ")
surname = input("Ваша фамилия: ")
age = input("Ваш возраст: ")
print (name + " " + surname + ". Ваш возраст: " + age)
print()
print("Получение данных")
friend_name = input("Как зовут вашего друга? ")
print("Вашего друга зовут - ", friend_name)
print()
print("Простая математика")
print(136 // 7)
print()
print("Математические операции")
num_1 = int (input ("Введите 1 число: "))
num_2 = int (input ("Введите 2 число: "))
num_3 = int (input ("Введите 3 число: "))
res = num_1 + num_2 + num_3
print ("Добавление чисел: ", res)
res = num_1 - num_2 - num_3
print ("Вычитание чисел: ", res)
print ("Умножение чисел: ", num_1 * num_2 * num_3)
print ("Деление чисел: ", num_1 / num_2 / num_3)
print ("Остаток при делении чисел: ", num_1 % num_2 % num_3)
print()
print("Типы переменные")
a = 23
b = 4.12
c = "2.1"
res = float (a) + b + float (c)
print(res)
print()
print("Условные операции")
x = float(input("Введите число: "))
if x < 0:
    print("Это отрицательное число")
elif x == 0:
    print("Число равно нулю")
else:
    print("Это положительное число")
print()
print("Проверка на числа")
a = input ("Введите число: ")
if a.isalpha():
    print ("Введите числа")
elif a.isdigit():
    print ("Вы ввели число")
print()
print("Условные операторы")
age = int(input ("Сколько вам лет?"))
if age > 18:
    print("Вам уже все можно")
elif age == 18:
    print("Ура, вам 18 лет!")
else:
    print("Вы еще слишком молоды")
print()
print("Умный калькулятор")
x = int(input("Первое число: "))
math = input("Операция: ")
y = int(input("Второе число: "))
if math == '+':
    print(x, " + ", y, " = ", (x + y))
elif math == '-':
    print(x, " - ", y, " = ", (x - y))
elif math == '*':
    print(x, " * ", y, " = ", (x * y))
elif math == '/':
    if y != 0:
        print(x, " / ", y, " = ", (x / y))
    else:
        print("Нельзя делить на ноль!")
else:
    print("Неверная операция")
print()
print("Среднее число")
a = int(input())
b = int(input())
c = int(input())
if a < b:
    if b < c:
        print(b)
    else:
        if a < c:
            print(c)
        else:
            print(a)
else:
    if a < c:
        print(a)
    else:
        if b < c:
            print(c)
        else:
            print(b)
print()
print("Проверка переменных")
a = int(input())
b = int(input())
if a % 2 == 0:
    a = "чет"
else:
    a = "нечет"
if b % 2 == 0:
    b = "чет"
if a == b:
    print("True")
else:
    print("False")

































