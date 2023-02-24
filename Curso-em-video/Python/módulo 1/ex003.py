#22º exercício
nome = str (input('Digite seu nome completo:'))
print('Analisando seu nome...')
print('Seu nome em letras maiusculas é: {}' .format(nome.upper()))
print('Seu nome em letras minusculas é: {}' .format(nome.lower()))
print("O seu nome completo possui o total de: {} letras" .format(len(nome) - nome.find(' ')))
print('O primeiro nome tem no total de letras de: {}'.format(nome.find(' ')))

#23º exercício

num = int(input('Digite um número com mais de 4 algarismos:'))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Unidade desse número: {}'.format(u))
print('Dezena desse número: {}'.format(d))
print('Centena desse número: {}'.format(c))
print('Milhar desse número: {}'.format(m))

#24º exercício

city = str(input('Digite um nome de uma cidade:')).strip()
print(city[:6].upper() == 'SANTOS')

#25º exercício

nom = str(input('Digite seu nome completo:')).strip()
print('Seu nome tem silva? {}'.format('silva' in nom.lower()))

#26º exercício

frase = (input("digite uma frase:")).upper().strip()
print('A letra (a) aparece {} vezes nesta frase'.format(frase.count('A')))
print('A posição que aparece o (a) pela primeira vez é: {}'.format(frase.find('A')+1))
print('A posição que a letra (A) aparece pela ultima vez é: {}'.format(frase.rfind('A')+1))

#27º exercício

nome = str(input("Digite seu nome completo:")).strip()
n = nome.split()
print('O primeiro nome é:{}'.format(n[0]))
print('O último nome é:{}.'.format(n[len(n)-1]))

#28º exercício

from random import randint
from time import sleep
computador = randint(0,5)
print('-=-' * 20)
print('Vamos ver se você irá acerta o número que estou pensando...')
print('-=-' * 20)
print('Vou pensar em um número de 0 a 5, tente adivinhar')
num = int(input('Em que número eu pensei?'))
print('PROCESSANDO...')
sleep(2)
if num == computador:
    print('Parabéns, você acertou! Eu pensei no número: {} e você disse: {}'.format(computador, num))
else:
    print('Você erro...')

#29º exercício

velocidade = float(input("A velocidade do carro:"))
if velocidade > 80:
    print("MULTADO! Você ultrapassou a velocidade máxima permitida de 80km/h")
    multa = (velocidade - 80) * 7
    print('Você terá que pagar uma multa de R${:.2f} '.format(multa))
else:
    print('Você não foi multado')

#30º exercício

num = int(input('Digite um número para saber se ele é impar ou par:'))
resultado = num % 2
if num == 0:
    print('Esse número é par')
else:
    print('Esse número é impar')

#31º exercício

distância = float(input('Qual a distância em km?'))
preço = distância * 0.50
if distância <= 200:
    print('O preço da passagem será {]' .format(preço))
else:
    preço = distância * 0.45
    print('O preço da passagem será {}'.format(preço))

#32º exercício

from datetime import date
ano = int(input('Qual ano quer analisar? Digite 0 para ver o ano atual'))
if ano ==0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('Esse ano {} é bissexto'.format(ano))
else:
    print('esse ano não é bissexto')

#33º exercício

a = int(input('Primeiro valor:'))
b = int(input('Segundo valor:'))
c = int(input('Terceiro valor:'))
menor = a
if b < a and b < c:
    menor = b
if b > a and b > c:
    menor = c

maior = a
if c > a and c > b:
    maior = b
if c < a and c < b:
    maior = c
print('O menor valor é {}'.format(menor))
print('O maior valor é {}'.format(maior))

#34º exercício

sal = float(input('Salário:'))
if sal <= 1250:
    novo = sal + (sal * 15 / 100)
else:
    novo = sal + (sal * 10 / 100)
print('Quem ganha {:.2f} passa a ganhar {:.2f} agora'.format(sal, novo))

#35º exercício

print('-=-' * 20)
print("analisador de triangulos")
print('-=-' * 20)
r1 = float(input('Primeiro segmento:'))
r2 = float(input('Segundo segmento:'))
r3 = float(input('Terceiro segmento:'))
r4 = float(input('Quarto segmento:'))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Podem formar triangulos')
else:
    print('Nao podem formar triangulos')