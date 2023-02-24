#1º exercício

print('Olá, mundo!')
print('Hello, world!')
print('-----------')
print('Olá! seja bem vindo!')
print('Hello! Welcome!')

#3º exercício

nome = input('Qual o seu nome?')
print('Prazer em te conhecer,', nome)

# or

print('Prazer em te conhecer, {}!'.format(nome))

print("------------------")

nome = input('Qual o seu nome?')
print('Prazer em te conhecer,', nome, ', eu mim chamo PY')
idade = input('Quantos anos você tem?')
print('Que legal!')
profissão = input('Com o que você trabalha atualmente?')
print('Que bacana, adorei isso!')

#4º exercício

num = int(input('Digite um número:'))
num2 = int(input('Digite outro:'))
s = num + num2
print('A soma de {} e {} é igual a {}'.format(num, num2, s))

print('----------------')

t1 = int(input('Digite qualquer número:'))
t2 = int(input('Digite outro:'))
T = t1 - t2
print('A diferença/subtração entre {} e {} é igual a {}'.format(t1, t2, T))

#5º exercício

num = (input('Digite algo:'))
print('O tipo primitivo dele é', type(num))
print('É um número?', num.isnumeric())
print('É um alfanumérico?', num.isalnum())
print('É alfabetico?', num.isalpha())
print('É um digito?', num.isdigit())
print('É um decimal?', num.isdecimal())
print('É minusculo?', num.islower())
print('É maiusculo?', num.isupper())
print('Só tem espaços?', num.isspace())
print('É capitalizado?', num.istitle())
print('A ', num.isidentifier())
print('A ', num.isprintable())

#6º exercício

num = int(input('Digite um número para ver seu sucessor e antecessor:'))
s = num + 1
a = num - 1
print('O sucessor de {} é {} e o antecessor de {} é {}.' .format(num, s, num, a))

#7º exercício

Y = int(input('Digite um número para ver seu dobro, triplo e raiz:'))
D = Y * 2
T = Y * 3
R = Y ** (1/2)
print('O dobro de {} é igual a {:.2f},\nO triplo de {} é igual a {:.2f}, \nE a raiz quadrada de {} é igual a {:.0f}.'.format(Y, D, Y, T, Y, R))

#8º exercício

nota1 = int(input('Primeira nota:'))
nota2 = int(input('Segunda nota:'))
média = (nota1 + nota2) / 2
print('A média do aluno(a) é: {}' .format(média))

print('Outro método para ver se foi aprovado ou reprovado')

print('1° bimestre:')
nota1 = float(input('Primeira nota:'))
nota2 = float(input('Segunda nota:'))
média1 = (nota1 + nota2) / 2
print("A média do aluno(a) é: {}".format(média1))

print('-----------------------------------------------------------------------')

print('2° bimestre:')
nota1 = float (input('Primeira nota:'))
nota2 = float (input('Segunda nota:'))
média2 = (nota1 + nota2) / 2
print('A média do aluno(a) é: {}' .format(média2))

print('-----------------------------------------------------------------------')

print('3° bimestre:')
nota1 = float(input('Primeira nota:'))
nota2 = float(input('Segunda nota:'))
média3: float = (nota1 + nota2) / 2
print('A média do aluno(a) é: {}' .format(média3))

print('-----------------------------------------------------------------------')

print('4° bimestre:')
nota1 = float (input('Primeira nota:'))
nota2 = float (input('Segunda nota:'))
média4 = (nota1 + nota2) / 2
print('A média do aluno(a) é: {}' .format(média4))

print('-----------------------------------------------------------------------')
print('Olhe se você foi aprovado ou reprovado:')
print('-----------------------------------------------------------------------')

m1 = (média1 + média2 + média3 + média4)
print('A média total do aluno nos 4 bimestres é: {}'.format(m1))
if m1 >= 28:
    print('Parabéns, você foi aprovado!')
else:
    print('Reprovado...')

medida = float(input('Qual a medida em metros?'))
c = medida * 100
m = medida * 1000
print(' A medida {} em centimetros é {:.0f}cm e em milimetros é {:.0f}mm'.format(medida, c, m))

#9º exercício

num = int (input("Digite um número para ver a tabuada:"))
for i in range(0, 11):
    print(num, "x", i, "=", num * i)

# aaaaa

print('------------')

num1 = int(input('Digite um número:'))
print('{} * 1 = {}'.format(num1, num1 * 1)),
print('{} * 2 = {}'.format(num1, num1 * 2)),
print('{} * 3 = {}'.format(num1, num1 * 3)),
print('{} * 4 = {}'.format(num1, num1 * 4)),
print('{} * 5 = {}'.format(num1, num1 * 5)),
print('{} * 6 = {}'.format(num1, num1 * 6)),
print('{} * 7 = {}'.format(num1, num1 * 7)),
print('{} * 8 = {}'.format(num1, num1 * 8)),
print('{} * 9 = {}'.format(num1, num1 * 9)),
print('{} * 10 = {}'.format(num1, num1 * 10)),

#10º exercício

num = float(input('Quanto dinheiro em R$ você tem:'))
s = num / 5.15
print('Com R${} você poderá comprar U${:.2f}'.format(num, s))

# com o dolar valendo R$ 3,21
print('----------------------------------------------------------')

real = float(input('Quantos R$ você poderá compra dolares:'))
t = num / 3.21
print("Com R${} você pode comprar U${:.2f}".format(real, t))

#11º exercício

alt = float(input('Qual a altura?'))
larg = int(input('Qual a largura?'))
área = alt * larg
print('A área total é de {:.0f} metros'.format(área))
tinta = área / 2
print('A quantidade de tinta necessária para tintá-la é de {}l'.format(tinta))