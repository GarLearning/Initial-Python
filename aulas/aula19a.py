#dicionarios
#dados = dict()
dados = {"nome": "pedro", "idade": 25}
print(dados["nome"])

#####n aceita depois de trocar o indice, preintar com posição do dado requerido: dados[0]

dados["sexo"] = "M"#a adição de um novo termo é feita altomaticamente com esse comando
del dados["idade"]#deleta a idade, realocando os itens em seus devidos lugares, apaga tanto keys quanto values
dados["nome"] = "gabriel"#subistitui o nome anterior por um novo

filme = {"titulos": "star wars",
         "ano": 1997,
         "diretor": "george lucas"
    }
#elementos que sao meio que inputs sao conecidos como valores
print(filme.values())
#elementos dos quais entraram no lugar dos indices sao as chaves(resultado da tradução)
print(filme.keys())
#quandos se trata dos valores e das chaves sao chamados de item
print(filme.items())
#for k in filme.keys(): printaria so as chaves
#for v in filmes.values(): printaria so os valores
for k, v in filme.items():
    print(f"o {k} é {v}")
#printa tado chaves com o k e valores com , v e k sao designados a items e n o 1 a pessoas e o segundo a items


locadora = list()
locadora.append(filme)
print(locadora)
#da append em uma lista, onde os elementos dsao dicionarios podendo traduzir as posições para "qualquer coisa"
print(locadora[0]["ano"])
#print do ano do elemento na posição 0
print("-"*30)
print(filme)
filme = {"titulo": "avengers",
         "ano": "2012",
         "diretor": "joss whendon"}
print("-" * 20)
estado = {}
brasil = []
for c in range(0, 2):
    estado["uf"] = str(input(" unidade federativa: "))
    estado["sigla"] = str(input("sigla do estado: "))
    brasil.append(estado.copy())#o .copy é o unico jeito de fazer uma copia independente do dicionario
#se fosse só o estado iria prevalecer o ultimo result adcionado, e estado[:], como em listas nao daria certo pois dicionarios n aceitam esse metodo
print(brasil)
for e in brasil:
    for k, v in e.items():#usou-se o "e" porque o e pega o termo 0 da lista e grava enquanto n reseta o laço
        print(f"a {k} é {v}")
    print()
