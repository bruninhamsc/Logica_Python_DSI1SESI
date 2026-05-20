print("===== EXERCÍCIOS =====")

# EX1
# Um aluno tem 10 anos. Armazene essa idade em uma variável
# e exiba seu tipo.
idade = 10
print(type(idade))

print("===================================")

# EX2
# A temperatura medida é 23.5°C.
# Armazene esse valor e mostre seu tipo.
temp = 23.5
print(type(temp))

print("===================================")


# EX3
# Crie um número complexo representando uma impedância elétrica
# de 5 + 8j e mostre sua parte real.
numero_complexo = 5 +8j
print("Parte Real:", numero_complexo.real)

print("===================================")


# EX4
# Mostre a parte imaginária do número complexo
# criado no exercício anterior.
print("Parte Imaginario:", numero_complexo.imag)

print("===================================")


# EX5
# Declare uma variável chamada "populacao"
# com o valor 8_000_000_000 (8 bilhões)
# e mostre seu tipo.
populacao = 8_000_000_000
print (populacao)
print (type(populacao))

print("===================================")


# EX6
# Verifique se o número 7 é do tipo int
# usando a função type().
valor = 7
print ("int(7)", valor)
print ("Tipo:", type(valor))

print("===================================")


# EX7
# Crie uma variável chamada "aprovado"
# com o valor booleano True e mostre seu tipo.
aprovado = True
print (aprovado)
print (type(aprovado))

print("===================================")


# EX8
# Some True e False e mostre o resultado
# e também o tipo do resultado.
resultado = True + False
print (resultado)
print (type(resultado))

print("===================================")


# EX9
# Pesquise e mostre qual é o valor máximo
# que um número inteiro pode ter em Python.
import sys
print(sys.maxsize)

print("===================================")


# EX10
# Mostre a representação em binário
# do número 10 usando uma função do Python.
print(bin(10))