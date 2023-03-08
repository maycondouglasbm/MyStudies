# Introdução a Algoritmos

**O que é algoritmo?**

Conjuntos de passos finitos e organizados que quando executados, resolvem um determinado problema.

# Algoritmos computacionais

São passos a serem seguidos por um módulo processador e seus respectivos usuários que, quando executados na ordem correta, conseguem realizar determinada tarefa.

VISUALG --> ferramenta utilizada durante o curso

```
algoritmo "nome"
var
   idetificador: tipo
inicio
     nome <- "maycon"
     escreva ('muito prazer', noome)
fimalgoritmo
```

comados de saída:

escreva('msg');

escreva(msg);

escreva('mensagem', msg);


* variáveis: espaço na memória que vão guardar valores

* identificadores:

- deve começar com uma letra;
- os próximos podem ser letras ou números;
- não pode utilizar nenhum símbolo, exceto _
- não pode conter espaços em branco
- não pode conter letras com acentos
- não pode ser uma palavra reservada

nota1 ;                    média [x];
sálario bruto; [x];        9dade [x];
algoritmo[x];              inicio_algoritmo;

* tipos primitivos

interio --> 1, 3, -5, 198;

real --> 0.6, 5.0, -77.3;

caractere --> '123', 'maycon', 'algoritmo';

logico --> verdadeiro ou falso;

* atribuições

msg <- "olá mundo!"

* Comando de entrada

```
algoritmo "meu nome"
var
   nome:caractere
inicio
   escreva('digite seu nome:')
   leia(nome)
   escreva ('muito prazer', nome)
fimalgoritmo
```

```
algoritmo "valores"
var  
   n1, n2, s: inteiro
inicio
   escreva("digite um número:)
   leia (n1)
   escreva('digite outro número:)
   leia(n2)
   s <- n1 + n2
   escreva('a soma é', s)
fimalgoritmo
```


* Operadores aritméticos:

\+ adição;

\- subtração;

\* multiplição;

/ divisão;

\ divisão;

^ exponenciação;

% módulo;

* Ordem de precendência

() parenteses;

^ exponenciação;

\* / multiplicação e divisão;

\+ - adição e subtração;


* funções aritméticas

 abs (valor absoluto);
 
 exp (exponenciação);
 
 int (valor inteiro);
 
 raizQ (raiz quadrada);
 
 pi (retorna pi);
 
 sen (seno(rad));
 
 cos (cosseno(rad));
 
 tan (tangente(rad));
 
 graupad (graus para rad);

 * Operadores lógicos e relacionais

Operadores relacionais
```
 > maior que
 < menor que
 >= maior ou igual a 
 <= menor ou igual a 
 = igual a 
 <> diferende de
```
 Operadores lógicos:     

 P |  q | p e q
:---: |---: | ---:
 v | v | v
 v | v | f
 f | v | f
 f | f | f

 p | q | p ou q
:---: |--: | ---: 
 v | v | v 
 v | f |v
 f | v | v
 f | f | f

 p | não p
:---: | --: 
 f | v

Ordem de preocendência geral

aritméticos :
:---: | :--
() ; ^ ; */ ; +-

relacionais:

todos

Lógicos:

e; ou; não 

