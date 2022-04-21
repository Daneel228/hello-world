print("Задание 1")
a=input("Ваши фамилия, имя?")
b=input("Сколько Вам лет?")
c=input("Где вы живете?")
print("Ваши фамилия, имя",a)
print("Ваш возраст",b)
print("Вы живете в",c)
print()
print("Задание 2")
import math
x=int(input("Введите x:"))
t=int(input("Введите t:"))
z=((9*math.pi*t+10*math.cos(x))/(math.sqrt(t)-math.fabs(math.sin(t))))*math.pow(math.e,x)
print("z = {0:.2f}".format(z))
print()
print("Задание 3")
for num in map(float, input("Введите три числа через пробел: ").split()):
    if 1 < num < 3:
        print(f"Число {num} принадлежит интервалу (1, 3)")
print()
print("Задание 4")
n = float(input())
for i in range(1,11):
    i = i*n
    print(i)
print()
print("Задание 5")
print("Вариант 1")
s="Промежуточный еврей Европ евсей Евший Егерь тенденция Вызвать"
print("Kоличество слов, начинающихся с буквы 'е'",s.count("Е"))
print()
print("Вариант 2")
s=";;;;;;;;;;::::;;"
print(s)
print(s.replace(":","!"))
print("Kоличество замен",s.count(":"))
print()
print("Вариант 3")
s = "В строке удалить символ точку (.) и подсчитать количество удаленных символов."
print(s)
s2=s.replace(".","")
print(s2)
print("Количество удаленных символов",len(s) - len(s2))
print()
print("Вариант 4")
a="Таким образом реализация намеченных плановых заданий позволяет оценить значение новых предложений."
print(a.replace("а", "о"))
print("Kоличество замен",a.count("а"))
print("Cимволов в строке",len(a))
print()
print("Вариант 5")
a="FWIJDWDK"
print(a)
print(a.lower())
print()
print("Вариант 6")
s="Таким образом реализация намеченных плановых заданий позволяет оценить значение новых предложений."
print(s)
s2=s.replace("а","")
print(s2)
print("Количество удаленных символов",len(s) - len(s2))
print()
print("Вариант 7")
s="Товарищи! постоянное информационно-пропагандистское обеспечение нашей деятельности позволяет выполнять важные задания по разработке модели развития."
print(s)
n=len(s)
s=s[:n // 2].replace('п', '*') + s[n // 2:]
print(s)
print()
print("Вариант 8")
s="Не следует, однако забывать, что дальнейшее развитие различных форм деятельности способствует подготовки и реализации форм развития."
print("Слов в строке",len(s))
print()
print("Вариант 9")
a="слово за слово он начал рассказывать о себе."
print(a)
print('B тексте встречается "слово"',a.count("слово"),"разa")
print()
print("Вариант 10")
s="Oratio accumsan et mea. Eu eam dolores lobortis percipitur, quo te equidem deleniti disputando."
print(s)
print(s.upper())
print()
print("Вариант 11")
s="чтобы сделаться не абстрагировать"
print(s)
for w in s.split():
    if(w.endswith("я")):
        print(w)
print()
print("Вариант 12")
s="чтобы сделаться не абстрагировать"
print(s)
for w in s.split():
    if(w.startswith("а") or w.endswith("я")):
        print(w)
print()
print("Вариант 13")
s="раз два три четыре пять"
print(s)
print("Kоличество букв «т» в строке",s.count("т"))
print()
print("Задание 6")
print("Вариант 1.1")
a=[5,2,8,6,7,2,0,9,8]
print(a)
print("Обратный порядок",list(reversed(a)))
print("Маx число",max(a))
print()
print("Вариант 1.2")
a=[5, -5, 0, 6, 0, 0]
print(a)
b=sum(a) / len(a)
a=[it if it else b for it in a]
print(a)
print()
print("Вариант 2.1")
a=[5,2,8,6,7,2,0,9,8]
print(a)
print("Мin число",min(a))
print()
print("Вариант 2.2")
numbers=[1,-2,3,-4,5,-6,7,-8,9]
print(numbers)
a=[]
b=[]
for num in numbers:
    if num > 0:
        a.append(num)
    else:
        b.append(num)
print("Положительные элементы",a)
print("Отрицательные элементы",b)
print()
print("Вариант 3.1")
D=[0, 1, 2, 3, 4, 5, 20, 7];
print(D)
print("Cуммa элементов с нечетными индексами",sum(x for i,x in enumerate(D) if i % 2 == 1))
print()
print("Вариант 3.2")
D=[0, 1, 2, 3, 4, 5, 20, 7];
print(D)
print([2*x if x < 15 else x for x in D])
print()
print("Вариант 4.1")
a=[5,2,8,6,7,2,0,9,8]
print(a)
print("Mаx элемент",max(a))
print("Индекс max элемента",a.index(max(a)))
print()
print("Вариант 4.2")
a=[5,2,8,6,7,2,0,9,8]
print(a)
res = []
for el in a:
    if el % 2 != 0:
        res.append(el)
if len(res) == 0:
    print('No numbers')
print(sorted(res, reverse=True))
print()
print("Вариант 5.1")
a=[-5,-2,-8,6,-7,-2,0,9,-8,1,-3]
print(a)
for i in range(len(a)-1):
    print(a[i],a[i+1]) if a[i]<0 and a[i+1]<0 else None
print()
print("Вариант 5.2")
a=[1,3,5,6,4,7,9,4,8,3,4,6]
print(a)
for i in reversed(range(len(a)-1)):
    if a[i] in a[i+1:]:
        a.pop(i)
print(a)
print()
print("Вариант 6.1")
a=[1,2,3,4,5,6,7,8,9,10]
print(a)
Max=max(a)
print('Max:',Max)
b=0
m=0
r=0
for i in a:
    if i>Max:
        print(i,">",Max)
        b+=1
    elif i<Max:
        print(i,"<",Max)
        m+=1
print("меньших максимального",m)
print("больших максимального",b)
print()
print("Вариант 6.2")
a=[1,2,3,4,5,6,7,8,9,10]
print(a)
s=sum(n for n in a if n > 5)
print("Cуммa тех чисел, которые >5:",s)
print()
print("Вариант 7")
a=[1,2,3,4,5]
print(a)
max_index, min_index = a.index(max(a)), a.index(min(a))
a[max_index], a[min_index] = a[min_index], a[max_index]
print(a)
print()
print("Вариант 8.1")
a=[1,2,3,4,5]
print(a)
prod = 1
for i in a:
    prod *= i
print(f'Весь список: {a}')
print(f'Сумма элементов списка равна: {sum(a)}')
print(f'Произведение элементов списка: {prod}')
print()
print("Вариант 8.2")
a=[1.2, -5, 0, 3.4, 0, 0]
print(a)
s=sum(a) / len(a)
a=[it if it else s for it in a]
print(a)
print()
print("Вариант 9")
a=[1, 2, 3, 4, 5]
b=[5, -5, 0, 6, 0, 0]
print("a=",a)
print("b=",b)
a,b = b,a
print("a=",a)
print("b=",b)
print()
print("Вариант 10.1")
a=[1,2,3,4,5,5,6,6,7]
b = [i for i in set(a) if a.count(i) > 1]
if len(b) == 0:
   print("Повторяющихся элементов нет")
else:
   print(b)
print()
print("Вариант 10.2")
a = [1, 2, 3, 10, 20, 23, 43, 5, 6, 7, 12, 45, 25, 76, 0] 
print(a)
print([0 if i < 10 else 1 if i > 20 else i for i in a])
print()
print("Вариант 11.1")
a=[1,2,3,4,5]
print(a)
x=a[0]
for i in a:
    if i > x and i % 2 == 0:
        x=i
print(x)
print()
print("Вариант 11.2")
a=[1,2,3,4,5]
print(a)
b=[]
for i in a:
    if i % 2 == 0 and i < 10:
        b.append(i)
if len(b) == 0:
    print("Чисел по заданному условию нет.")
else:
    print(b)
print()
print("Вариант 12")
a=[3,8,1,3,4,2]
print(a)
b=0
for i in sorted(a):
    if i%2:
        b=i
        break
print("Hаименьший нечетный элемент",b)
print()
print("Вариант 13.1")
m = [0, 1, 1, 10, 2, 4, 2, 10, 0, 2, 2, 6, 8, 9, 9, 9, 0]
print(m)
n = []
k = 0
for i in range(len(m) - 1):
    if m[i] not in n:
        if m.count(m[i]) > 1:
            n.append(m[i])
            k = m.index(m[i])
            print('число =', m[i], 'индексы =', k, end=' ')
            for j in range(m.count(m[i]) - 1):
                k = m.index(m[i], k + 1)
                print(k, end=' ')
print()
print("Вариант 13.2")
a = [10, 1, 11, 12, 30, 14, 20, 15]
print(a)
for i in range(len(a)):
   if a[i] < 15:
       a[i] *= 2
print(a)
print()
print("Вариант 14")
l = [10, 1, 11, 12, 30]
print(l)
ma= max(l)
mi = min(l)
for i in range(len(l)):
    if l[i] == ma:
        l[i] = mi
    elif l[i] == mi:
        l[i] = ma
print(l)
print()

