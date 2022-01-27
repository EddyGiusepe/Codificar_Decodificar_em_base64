'''
Data Scientist Jr.: Dr.Eddy Giusepe Chirinos Isidro

Sempre aprendendo!
'''

import sys
import pybase64 as b64

arquivo_leitura = open("texto.txt", "r")
arquivo_escritura = open("resultado.txt", "w")
texto_sem_codificar = arquivo_leitura.read()


texto_codificado = b64.b64encode(bytes(texto_sem_codificar, "UTF-8"))
print("O texto codificado é: {}".format(texto_codificado))


texto_decodificado = b64.b64decode(texto_codificado)
print("O texto decodificado é: {}".format(texto_decodificado))


arquivo_escritura.write(str(texto_codificado))
arquivo_escritura.write(str(texto_decodificado))
arquivo_escritura.close()
arquivo_leitura.close()
