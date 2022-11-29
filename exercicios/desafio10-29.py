velo = int(input('qual voi a velocidade do veiculo em km/h?'))
preço = (velo-80)*7
if velo > 80:
    print('multa por passar de 80km/h foi de R${:.2f}.'.format(preço))
else:
    print('nao hove necessidade de multa, vecocidade permitida.')
print('a velo do veiculo foi de {} km/h'.format(velo))