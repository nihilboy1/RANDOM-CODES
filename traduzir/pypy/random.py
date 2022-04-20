from random import randint

aleatorio = randint(1,10)
while True:
  usuario = int(input("Em qual numero, de 1 a 10 a máquina pensou?"))
  if aleatorio == usuario:
    print(f"Você acertou! O valor da máquina foi {aleatorio}")
    break
  elif usuario > aleatorio:
    print("Chutou muito alto!")
  else:
    print("Chutou muito baixo!")