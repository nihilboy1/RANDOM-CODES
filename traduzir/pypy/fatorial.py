import xdrlib
from xml.dom import xmlbuilder


a = int(input("Informe um numero"))


x = a - 1
while x > 0:
  a = a * x
  x -= 1
else:
  print(a)
