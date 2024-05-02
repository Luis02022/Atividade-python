import os 

os.system("cls || clear")

desconto = 0.1

print("||Escolha a quantidade em kg||")
quantmaca = int(input("Digite a quantidade de maçãs:"))
quantmorango = int(input("Digite a quantidade de morangos:"))


if quantmaca < 5:
    precomaca = 2.50
else: 
    precomaca = 2.20
if quantmorango < 5:
     precomorango = 1.80

else:
     precomorango = 1.50

     pesoTotal = quantmaca + quantmorango
     subtotal = (quantmaca * quantmorango) + (precomorango * precomaca)   

if subtotal > 8 or subtotal > 25:
 desconto = subtotal - 0.1

else:
    desconto = 0


