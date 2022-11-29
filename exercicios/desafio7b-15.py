hora = float(input('Ha quantas horas esta com o carro:'))
km = float(input('quantos quilometros foi rodado:'))
pd = hora*2.5
pk = km*0.15
print('o preço a ser pago é: R${:.2f}'.format(pd+pk))