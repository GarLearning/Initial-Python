#variaveis compostas parte 2 de listas
dados = list()
dados.append("joao")
dados.append(24)
print(dados)
pessoas = list()
pessoas.append(dados[:])
# assim se coloca listas dentro de listas, dando para fazer uma estrutura de repetição
#onde coloca-se inputs de dados dentro de uma listas coloca esse resultado dentro de outra,
#e zera os resultados da 1 lista para colocar mais daados
print(pessoas)
pessoas = [["joao", 24], ["pedro", 15], ["maria", 35]]
#logo tem 3 listas("dados") dentro da lista pessoas
print(pessoas[0][0])
#esse comando printaria o termo de numero 0 dentro da lista pessoas, (que seria a lista joao, 24) e o termo 0 que seria joao
print(pessoas[2])
#da para fazer listas dentro de listas onde os inputs sao feitos dentro de if fazendo o append
#numa lista que ja esta dentro de outra lista, ex:. na posição 0 uma pesquisa com respostas masculinas
# na posição 1 uma lista com respostas femininas e isso tudo dentro de outra lista
print('-'*30)
for p in pessoas:
    print(f"nome: {p[0]} idade: {p[1]}")