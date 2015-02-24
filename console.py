import sys
import os 

c = 1

plataforma = sys.platform

if plataforma == 'win32':
          os.system('cls')
elif plataforma == 'linux2':
          os.system('clear')
elif plataforma == 'linux':
          os.system('clear')
elif plataforma == 'darwin':
          os.system('clear')

print 'PARA SALIR DE LA CONSOLA PRESIONE "CTRL+D"'
print '------------------------------------------\n'

while c == 1:
         os.system(raw_input('@python:~$ '))
