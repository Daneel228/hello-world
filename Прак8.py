print("Создание словаря")
d1 = dict(Ivan="manager", Mark="worker")
print(d1)
print(type(d1))
d2 = {"A1":"123", "A2":"456"}
print(d2)
print(type(d2))
print()
print("Добавление и удаление элемента")
d1 = {"Russia":"Moscow", "USA":"Washington"}
d1["China"]="Beijing"
print(d1)
d2 = {"A1":"123", "A2":"456"}
del d2["A1"]
print(d2)
print()
print("Методы словарей")
#clear() - Удаляет все элементы словаря.
d2 = {"A1":"123", "A2":"456"}
print(d2)
d2.clear()
print(d2)
print()
#copy() -Создается новая копия словаря.
d2 = {"A1":"123", "A2":"456"}
d3 = d2.copy()
print(d3)
d3["A1"]="789"
print(d2)
print(d3)
print()
#get(key) - Возвращает значение из словаря по ключу key.
d = {"A1":"123", "A2":"456"}
print(d.get("A1"))
print()
#items() - Возвращает элементы словаря (ключ, значение) в отформатированном виде.
d = {"A1":"123", "A2":"456"}
print(d.items())
print()
#keys() - Возвращает ключи словаря.
d = {"A1":"123", "A2":"456"}
print(d.keys())
print()
#update([other])- Обновить словарь парами (key/value) из other, если же ключи уже существуют, то обновить их значения.
d = {"A1":"123", "A2":"456"}
print(d)
d.update({"A1":"333", "A3":"789"})
print(d)
print()
#values() - Возвращает значения элементов словаря без ключей.
d = {"A1":"123", "A2":"456"}
print(d.values())