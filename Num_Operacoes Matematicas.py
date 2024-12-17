# Números e Operações Matemáticas
# https://docs.python.org/3/library/math.html

a = 20     # <class 'int'>
b = 20.5   # <class 'float'>
print(type(a))  # <class 'int'>
print(type(b))  # <class 'float'>

# Operações Matemáticas
print(10 + 6)
print(10 - 6)
print(10 * 6)

print(10 / 6)   # 1.6666666666666667
print(f"{10 / 6:.2f}")        # método f-string
print("{:.2f}".format(10/6))  # Método format

# Arredondamento round(número, qtd digitos)
print(round(1.6658))  # Sem a qtd de digitos arredondará para o próximo inteiro
print(round(1.666666, 2))  # Com a qtd de digitos

print(10 // 6)  # Divisão de inteiro (só a parte inteira)
print(10 % 6)   # Modulo (resto da divisão)
print(10 ** 6)  # exponencial

c = 10
c = c + 5
c += 5

d = 20
d = d - 2
d -= 2

import math

# Raiz quadrada
raiz_quadrada = math.sqrt(16)  # Resultado: 4.0

# Exponencial
exponencial = math.exp(2)  # Resultado: e^2 ≈ 7.389

# Logaritmo natural (base e)
log_natural = math.log(10)  # Resultado: log_e(10)

# Logaritmo de base 10
log_base10 = math.log10(100)  # Resultado: 2.0

# Seno, cosseno e tangente (em radianos)
seno = math.sin(math.pi / 2)  # Resultado: 1.0
cosseno = math.cos(math.pi)   # Resultado: -1.0
tangente = math.tan(math.pi / 4)  # Resultado: 1.0

# Converter graus para radianos e vice-versa
radianos = math.radians(180)  # Resultado: π
graus = math.degrees(math.pi)  # Resultado: 180

# Módulo de um número (valor absoluto)
modulo = math.fabs(-5)  # Resultado: 5.0

# Fatorial de um numero (n!)
fatorial = math.factorial(5)  # Resultado: 120
print(fatorial)


import random

# Número aleatório entre 0 e 1
aleatorio = random.random()
print(aleatorio)
# Gerando Números Aleatórios em um Intervalo Personalizado
a = 5
b = 10
# Gera número entre 5 e 10
aleatorio_personalizado = a + (b - a) * random.random()
print(aleatorio_personalizado)

# Número inteiro aleatório entre dois valores
inteiro_aleatorio = random.randint(1, 10)

# Gera números (aleatórios) float no intervalo [a, b] (ambos inclusivos).
# Número entre 2.5 e 7.5
aleatorio1 = random.uniform(2.5, 7.5)
print(aleatorio1)

# Número aleatório dentro de um intervalo (com passo)
passo = random.randrange(0, 10, 2)  # Exemplo: 0, 2, 4, 6, 8
print(passo)
# Escolher aleatoriamente de uma lista
escolha = random.choice([1, 2, 3, 4, 5])
print(escolha)


import numpy as np

# Criar um array
arr = np.array([1, 2, 3, 4])
print(arr)

# Soma de elementos do array
soma = np.sum(arr)  # Resultado: 10
print(soma)

# Média
media = np.mean(arr)  # Resultado: 2.5
print(media)

# Desvio padrão
desvio_padrao = np.std(arr)  # Resultado: ≈ 1.118
print(desvio_padrao)

# Operações com matrizes
matriz_a = np.array([[1, 2], [3, 4]])
matriz_b = np.array([[5, 6], [7, 8]])
print(matriz_a)
print(matriz_b)

soma_matrizes = matriz_a + matriz_b  # Soma elemento por elemento
print(soma_matrizes)
produto_matrizes = np.dot(matriz_a, matriz_b)  # Produto matricial
print(produto_matrizes)


from fractions import Fraction

# Criar uma fração
fracao = Fraction(3, 4)  # 3/4
print(fracao)

# Soma de frações
soma_fracoes = Fraction(1, 3) + Fraction(1, 6)  # Resultado: 1/2
print(soma_fracoes)