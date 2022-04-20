

from turtle import st


produtoevalor = {}
precos = []
maioresdemil = 0
pos = 0

while True:
  produto =  str(input("Informe o nome do produto: "))
  valor = int(input("Informe o preço do produto: "))
  fim = str(input("Finalizar compra? (S ou N) ")).upper()
  produtoevalor.update({
    produto: valor
  })
  if fim == "S":
    for produto, valor in produtoevalor.items():
      if pos == 0:
        menorprod = produto
        menorvalor = valor
      if valor < menorvalor:
        menorvalor = valor
        menorprod = produto
      precos.append(valor)
      pos += 1
    else:
      total = sum(precos)
      for item in precos:
        if item > 1000:
          maioresdemil += 1
    break
  else:
    continue
print(f"O produto mais barato foi {menorprod}, com preço de {menorvalor:.2f}R$")
print(f"Houve um total de {maioresdemil} produto com peço acima de 1000,00R$")
print(f"O valor total da compra foi de: {total:.2f}R$")
