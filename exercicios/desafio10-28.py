import random
n = int(input('adivinhe em qual numero 1 a 100 estou pensando:'))
sorte = random.randrange(100)
if n == sorte:
    print('good vc acertou :)')
if n > 100:
    print('acabou de jogar suas chances fora digitando {}, é maior q 100'.format(n))
else:
    print('vc errou o numero, o q era bem rpovavel')
print('o numero sorteado foi {}'.format(sorte))