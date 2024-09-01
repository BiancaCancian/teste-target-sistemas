"""

5) Escreva um programa que inverta os caracteres de um string.

IMPORTANTE:
a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
b) Evite usar funções prontas, como, por exemplo, reverse;


"""
entrada = input("Digite a string que você deseja inverter: ")

invertida = ""

for caractere in entrada:
    invertida = caractere + invertida

print(f"String invertida: {invertida}")
