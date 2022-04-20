valor = int(input("escreva um valor: "))

i = 0

while valor <= 0 or valor > 125:
  print("valor invalido")
  i = i + 1
  valor = int(input("digite um valor: "))
else:
  print(i)