"""Erro sintático(na sintaxe) > são os que acontecem devido erros de digitação(que seria correta para a execução do comando)
Erros que não são semântico são chamados de EXEÇÃO, exemplos: um print em uma variável que  não exista,
uma digitação alfanumérica quando se declara o input como int, divisões por 0 etc.
"""
# print(x)
# n = int(input("enter a value: hi biiii")

# obs> Digitando python exseption list no google, aparece listas de erros e suas definições.

"""Para o tratamento de erros e exceções a estrutura usada é a seguinte:
try:
	Comando que ira ser executado(dando erro ou n).
excpt:
	Mensagem(código) caso a execução do programa acima der erro.
else:
	Mais caso n de erro, aqui seria a mensagem(código) dada caso desse certo.
finally:
	Isso erá acontecer independente do try ou else ou finally.

Obs:. Else e finally são apenas opcionais.

except Exception as erro:
	Com esse comando, e printando (print(f"o erro foi {erro.__class__}")), diria a classe do erro, além  da classe tem outros comandos que diria porque esse erro estaria acontecendo.
	Obs:. as erro, essa palavra erro pode ser substituída por qualquer outra
	    COM ESSE TRATAMENTO DE ERRO N APARECERIA AS MENSAGENS PADROES DO PYTHON
"""

try:
    a = int(input("Enter a value: "))
    b = int(input("Enter the second value: "))
    c = a / b
#except:
#    print(f"Operation not accept!")
#except (ValueError, TypeError):
#    print("problems with type of data.")
except ZeroDivisionError:
    print("is not possible the division for 0.")
except Exception as error:
    print(f"The error of class is {error.__class__}")
except Exception as error:
    print(f"{error.__cause__}")
else:
    print(f"The result is {c}")
finally:
    print(f">>END<<")
# pode ter varios excepts logo sendo possivel otimizar mensagens para diferentes tipos de erros (quando encontrar uma das exeções ele para):
#except(exeções) e except Exception(tratamento de tipo de erro) e except ValueError(tratando diretamente o erro).