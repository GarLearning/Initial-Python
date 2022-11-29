from time import sleep


def cont(start, end, step):
    if step == 0:
        step = 1
    if step < 0:
        step *= -1
    print(f"Cont of {start} the {end} of {step} in {step}: ")
    sleep(0.5)
    if start < end:
        cont_f = start
        while cont_f <= end:
            print(f"-> {cont_f}", end=" ")
            cont_f += step
            sleep(1)
        sleep(0.5)#as atuais versoes do python cria um buffer dentro dos laços de repetição (while), caso o sleep fosse colocado dentro de um laço
#teria de usar a função ""flush=True"" (na frente do end="", ) com isso n ligaria o buffer de tela e preintaria os numeros com intervalo (obs: n é o caso
# pois o sleep esta fora do laço) | retratação: testei e funciona normal deve ter sido ajeitado nas versões atuais | no pycharm funciona mais quando
# colocado em ide n e é necessario o fluch
        print("")
    else:
        cont_s = start
        while cont_s >= end:
            print(f"-> {cont_s}", end=" ")
            cont_s -= step
        sleep(0.5)
        print("")
    print("=" * 40)


cont(1, 10, 1)
cont(10, 0, 2)
s = int(input("Start: "))
e = int(input("End: "))
p = int(input("Step: "))
cont(s, e, p)
