inicio = int(input("Digite um número inicial para o invervalo: "))
fim = int(input("Digite um número final para o intevalo: "))

somaPares = 0

for numero in range(inicio, fim+1):
    if numero %2 == 0:
        somaPares += numero

if somaPares > 0:
    print("A soma dos números pares no intervalo informado é:", somaPares)
else: 
    print("Não há numeros pares no intervalo informado!")


