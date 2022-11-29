import urllib
import urllib.request

try:
    status = urllib.request.urlopen("http://www.pudim.com.br/")
except urllib.error.URLERROR:
    print("This site wasn't possible to open.")
else:
    print("This site is up and running.")
    print(status.read())#conteudo do site