import os
contpares = 0
contimpares = 0
os.system("cls || clear")
for i in range(5):
    numero = int(input(f"Digite o {i+1}º número:"))
 
    if numero % 2 == 0:
        contpares += 1
        
    else:
        contimpares += 1 

print(f"Numeros pares: {contpares}")
print(f"Numeros impares: {contimpares}")