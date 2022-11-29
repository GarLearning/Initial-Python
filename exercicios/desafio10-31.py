viagem = int(input('dia distancia da viagem em km/h:'))
if viagem > 200:
    print('o custo da viagem foi de R${:.2f}'.format(viagem*0.45))
else:
    print('o custo da viagem foi de R${:.2f}'.format(viagem*0.50))
print('sua viagem foi de {}km/h'.format(viagem))