#O break quebra um loop por determinada condição
#flag é = ao ponto de parada
"""n = s = 0
while True:
    n = int(input("enter number: "))
    if n == 999:
        break
    s += n
print(f"a soma vale {s} ")"""
#print(s)
#testa se o break sai do laço atual ou de todos os laços
#forma f strengs apartir do python 3.6

"""nome = "gabriel"
idade = 20
print(f"o {nome} tem {idade} anos.")#python 3.6
print("o {} tem {} anos.".format(nome, idade))#python 3
print("o %s tem %d anos." % (nome, idade))#python 2"""
#%s == string %d inteiro
# passar a ficar interado sobre novas funcionalidades que as att tazem
nome = "gabriel"
idade = 20
salario = 500000
print(f"o {nome:@^11} tem {idade} e ganha R${salario:.2f}")
