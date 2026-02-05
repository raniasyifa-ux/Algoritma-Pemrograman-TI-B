#metode __iter__() dan __next__().

mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))

#String juga merupakan objek yang dapat diiterasi, yang berisi urutan karakter:
mystr = "banana"
myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

#Melakukan Perulangan Melalui Iterator
mytuple = ("apple", "banana", "cherry")

for x in mytuple:
  print(x)

#Iterasi karakter-karakter dalam sebuah string:
mystr = "banana"

for x in mystr:
  print(x)

