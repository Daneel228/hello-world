a = [1, 2, 3]
print(a)
a[1]=15
print(a)
lst=[10, 20, 30]
tpl=(10, 20, 30)
print("lst.sizeof",lst.__sizeof__())
print("tpl.sizeof",tpl.__sizeof__())
print()
print("Создание кортежей")
a = ()
print(type(a))
print(a)
a = (1,2,3,4,5)
print(type(a))
print(a)
print()
print("Преобразование кортежа в список и обратно")
lst = [5, 4, 3, 2, 1]
print(type(lst))
print(lst)
tpl = tuple(lst)
print(type(tpl))
print(tpl)




