#funções
#sao rotinas em linguagem de programação. print, input, int
#def é utilizado para declarar uma função personalizada
# todas as funções em python sao indentificadas por parenteses no final do nome
#criando uma funnção(rotina)

#def siguinifica definição
def mostralinha():
    print("=" * 20)#so é printado quando usada a "chave"(mostralinha())


#se n deixar 2 linhas vazias entre o def e o programa principal(cima e baixo) a proxima coisa escrica fica  sublinhada(questao de estetica), no caso o mostralinha depois do comentario
# mostralinha é a palavra usada como frase para mostras o codigo "print("=" * 20)", uma FUNÇÃO(rotina)
mostralinha()
#parametros
def mens(msg):# o "msg" é um PARAMETRO, pode ter qualquer nome, n so msg,
    print("=" * 20)
    print(msg)#o msg dentro do print é onde a mensagem vai ser chamada
    print("=" * 20)

mens("hello world")
mens("hello universe")

mostralinha()
def soma(a, b):
    print(f"a={a} e b={b}")
    s = a + b
    print(f"The sum is= {s}")


soma(3, 4)
soma(5, 6)
soma(a=5, b=6)
soma(b=5, a=6)  # da para explicitar o valor dos parametros desta forma onde foi definido mesmo com a ordem sendo a mesma
# dessa forma so é possivel fazer com a contidade de parametros explicita, se n da erro

# EMPACOTAMENTO DE PARAMETROS
mostralinha()


def cont(*num):  # o asterisco seguinifica DESEMPACOTAR, usado quando se tem uma quantidade n definida de parametros
    print("The values are", end="")
    for c in num:  # num pega o cont, nesse caso, e o trasforma em uma tupula, onde num vai ser a tupula com os valores definidos em cont
        print(f" {c}", end="-")
    print(f" They are in all {len(num)} numbers", end=".")
    print()


cont(1, 0, 3, 5)
cont(1, 6, 4)
cont(2, 3)
mostralinha()


def double(lst):# n precissa do * para desenpacotamento pq a lista ja é uma variavel composta
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1
    print(lst)


valores = [5, 3, 1, 0, 2]
double(valores)
print(valores)
#funções sao definidas com def q quer dizer definição, que quando criadas fazem com que a rotina criada dentro do def seja executada.
#parametros sao usados para se obter mais funcionalidades, os parametros sao traduzidos como variaves(resultados, inputs),
# que serao tratadas pelas funções, por isso listas podem ser definidas como parametros sem a necessidade de haver um desempacotamento.
#o * antes do parametro siguinifica q ira desempacotar oo parametro para ser tratado, o * faz com que os resultados dos parametros sejam colocados em uma tupula, dai o "desempacotar",
#para poder ser usado um numero variado de parametros.00000000000000
