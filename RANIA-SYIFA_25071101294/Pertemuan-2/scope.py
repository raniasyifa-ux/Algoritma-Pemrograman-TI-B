    #Local Scope
def myfunc():
  x = 300
  print(x)

myfunc()

#Fungsi di Dalam Fungsi
def myfunc():
  x = 300
  def myinnerfunc():
    print(x)
  myinnerfunc()

myfunc()

#Global Scope
x = 300

def myfunc():
  print(x)

myfunc()

print(x) = 300

def myfunc():
  print(x)

myfunc()

print(x)

#Penamaan Variabel
x = 300

def myfunc():
  x = 200
  print(x)

myfunc()

print(x)

#Kata Kunci Global
def myfunc():
  global x
  x = 300

myfunc()

print(x)