import keyword
print("Phyton keywords:",keyword.kwlist)
print()

print("keyword.iskeyword (try)",keyword.iskeyword("try"))
print("keyword.iskeyword (b)",keyword.iskeyword("b"))
print()

a=4
b=5
c=b
print("a=",a)
print("b=",b)
print("id(a)",id(a))
print("id(b)",id(b))
print("c=b")
print("id(c)",id(c))
print()

a1=10
b1="hello"
c1=(1,2)
print("a=",a1)
print("b=",b1)
print("c=",c1)
print("type(a)",type(a1))
print("type(b)",type(b1))
print("type(c)",type(c1))