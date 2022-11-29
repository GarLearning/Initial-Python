#modularização
#para que um programa n fique tao grande usa-se a modularização, que faz com que as funções fiquem em um arquivo .py separado localmente permitindo o importe do mesmo
#pelo nome do arquivo, e com o from "arquivo" import "nome da função dentro do arquivo".
import aulas
from aulas import aula21a
    #mais ou menos assim, porem para ser considerado um modulo de aulas seriam == a arquivos .py e aula21a, por exemplo, seria uma função(def) dentro desse arquivo.
#obs:. n e recomendado usar o from devido se huver 2 imports com funções iguais o programa respeitara a do ultimo improt, como abaixo que o time usado seria o 2
from datetime import time
from time import time
                #pacotes
#mesmo que bibliotecas em outras linguagens
#são designados a projetos maiores onde existiria muitas funções com funcionalidades diferentes
#passo1- dentro do CV, nesse caso, cria um packeage
#passo2- dentro desse package, que seria o pacote, cria-se outro package, com o nome de uma das funcionalidades expecificas (operações, linhas, quebralinhas).
#passo3- dentro desse package expecifico cria um arquivo "__init__.py", que geralmente ja vem ao se criar um package(criação obrigatoria).
#passo4- dentro dele coloque as funcões
import aulas
from aulas import aula21a
#aulas- seria o 1 package
#aula21a- seria o segundo especifico onde estariam as funções referentes a aula21a
#para fazer uso das funções da aula21a é só usar o comando, aula21a.função que queira usar







#####testar se da para usar import aulas, e colocar aulas.aula21a.função que queira usar
#####testar n criar o __init__.py e colocar funções em uma pasta normal(se n funcionar ver o pq disso)