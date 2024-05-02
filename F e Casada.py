import os

os.system("cls || clear")

nome = input("Digite seu nome:")
sexo = input("Digite seu sexo:")
estcivil = str(input("Digite seu estado civil:"))



print(f"Nome: {nome}")
print(f"Sexo: {sexo}")
print(f"Estado Civil: {estcivil}")


if sexo == "F"  and estcivil == "Casada":
    tempoCasada =  input("Digite quanto tempo de casada:")
    print(f"Tempo de casamento: {tempoCasada}")

