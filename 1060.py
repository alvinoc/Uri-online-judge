lista = []
soma = 0
lista.append(float(input()))
lista.append(float(input()))
lista.append(float(input()))
lista.append(float(input()))
lista.append(float(input()))
lista.append(float(input()))

for n in lista:
    if (float(n) > 0):
        soma = soma + 1

print(soma, "valores positivos")