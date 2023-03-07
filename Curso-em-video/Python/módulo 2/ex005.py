#46º exercicio

from time import sleep

print('-=' * 20)
print('CUIDADO! OS FOGOS IRÃO ESTOURAR EM:')
print('-=' * 20)
i = 1
for i in range(10, 0, -1):
    print(i)
    sleep(1)
print('BOOOOOOOOOMMMMM')

#47º exercício

for i in range(0, 51, 2):
    print(i)

    soma = 0
count = 0
for i in range(1, 501, 2):
    if i % 3 == 0:
      soma += i
      count += 1
print(' A soma dos {} valores é igual a {}'.format(count, soma))

#48º exercício

num = int (input("Digite um número para ver a tabuada:"))
for i in range(0, 11):
    print(num, "x", i, "=", num * i)

soma = 0
count= 0
for i in range(1, 7):
    if i % 2 == 0:
        num = int(input('Digite o {} valor'.format(i)))
        print()
        soma += num
        count += 1
print('voce informou {} pares e a soma foi {}'.format(count, soma))

#49º exercício

primeiro = int(input('Primeiro temo:'))
razão = int(input('razão:'))
décimo = primeiro + (10 - 1) * razão
for i in range(primeiro, décimo + razão, razão):
    print("{}".format(i), end='->')
print('acabou')