valor = float(input('valor do produto? R$'))
print("""====Incira agora o codigo da forma de pagamento====
a vistra no dinheiro (1)
a vista no carão (2)
2x no cartão (3)
3x ou mais no cartão (4)""")
fpaga = int(input("qual sera sua opição de pagamento?"))
if fpaga == 1:
    print("voce tera 10% de desconto, o novo preço do produto é R${:.2f}".format(valor-valor*10/100))
elif fpaga == 2:
    print("voce tera um desconto de 5%, o novo preço do produto é R${:.2f}".format(valor-valor*5/100))
elif fpaga == 3:
    print("seu preço continuara o mesmo, que é R${:.2f}".format(valor))
elif fpaga == 4:
    print("voce tera um acrecimo de 20%, o novo preço é de R${:.2f}".format(valor+valor*20/100))
else:
    print("valor digitado ou opção nao aceitos")