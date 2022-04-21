print("1. Конструкция if ")
if 1: 
 print("hello 1")
print()

a=3
if a==3: 
 print("Здесь а =", a)
print()

if a>1: 
 print(a,">1 hello 3")
print()
 
lst=[1,2,3] 
if lst: 
 print("hello 4")
print()
 
print("2. Конструкция if – else")
a1=3 
if a1>2: 
 print(a,">2 H") 
else: 
 print(a,"не больше 2 L")
print()
 
a2=1 
if a2>2: 
 print(a2,">2 H") 
else: 
 print(a2, "не больше 2 L")
print()

a3=17 
b=True if a3>10 else False 
print(a3,">10",b)
print()

print("3. Конструкция if – elif – else ")
a4 = int(input("введите число:")) 
if a4 < 0: 
 print(a4,"<0 Neg") 
elif a4 == 0: 
 print(a4,"=0 Zero") 
else: 
 print(a4,">0 Pos")
print()
#Если пользователь введет число меньше нуля, то будет напечатано “Neg“,  равное нулю – “Zero“, большее нуля – “Pos“.

print("4. Операторы цикла while и for")
a5 = 0 
while a5 < 7: 
 print("A") 
 a5 += 1
print()
#Буква “А” будет выведена семь раз в столбик.

print("5. Операторы break и continue ")
a6=0
while a6>=0:
 if a6 == 7:
  break
 a6+=1
 print("B")
 #В приведенном выше коде, выход из цикла произойдет при достижении переменной a значения 7.
 print()
 
a7=-1
while a7<10:
  a7+=1
  if a7>=7:
   continue
   print("C")
   #При запуске данного кода символ “А” будет напечатан 7 раз, несмотря на то, что всего будет выполнено 11 проходов цикла. 
print()

print("6. Оператор цикла for")
for i in range(5): 
 print("Hello")
 print()
 
lst = [1, 3, 5, 7, 9] 
for i1 in lst: 
 print(i1**2)
print() 

word_str = "Hello, world!" 
for g in word_str: 
 print(g)
print()
