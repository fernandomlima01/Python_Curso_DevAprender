# Random_Valores Aleatórios
import random

# Número aleatório entre 0.0 <= valor < 1.0
aleatorio = random.random()
# Utilizando round() para arredondar e determinar a quant casas decimais
print(round(aleatorio, 4))  # ex.: 0.5377

# random.random() - Gerando Números Aleatórios em um Intervalo Personalizado
a = 5
b = 10
# Gera número entre 5.0 <= valor < 10.0
aleatorio_personalizado = a + (b - a) * random.random()
# Utilizando round() para arredondar e determinar a quant casas decimais
print(round(aleatorio_personalizado, 4))  # ex.: 8.0397


# Gera números (aleatórios) float no intervalo [a, b] (ambos inclusivos).
# Número entre 2.5 <= valor <= 7.5
aleatorio1 = random.uniform(2.5, 7.5)
# Utilizando round() para arredondar e determinar a quant casas decimais
print(round(aleatorio1, 6))  # Ex.: 2.652557


# Gera Número inteiro aleatório no intervalo [a, b] (ambos inclusivos).
# Número entre 1 <= valor <= 20
inteiro_aleatorio = random.randint(1, 20)
print(inteiro_aleatorio)  # Ex.: 4


# Gera Número aleatório Inteiro dentro de um intervalo (com step)
# gera um número aleatório entre 1 <= valor <= 25
# O step 2 significa que só sera gerado os números 1,3,5,7,9...25
step = random.randrange(1, 25, 2)  # Ex.: 1,3,5,7,9,11,13,15,17,19,21,23 e 25.
print(step)  # Ex.: 23


# Escolher aleatoriamente de uma lista
escolha = random.choice([1, 2, 3, 4, 5])
print(escolha)  # Ex.: 4

lista = ['maçã', 'banana', 'uva']
print(random.choice(lista))  # Ex.: 'banana'


# Retorna uma lista com k elementos escolhidos aleatoriamente com repetição.
# Pode usar pesos (weights) para influenciar a probabilidade de escolha
cores = ['verde', 'vermelho', 'azul', 'amarelo',
         'cyan', 'magenta', 'preto', 'branco']
# Sem considerar os pesos (weights)
print(random.choices(cores, k=2))  # Ex.: ['magenta', 'verde']

# A quant em weights (quando colocado) tem que ser igual a lista
# Caso não coloque dará o erro: : The number of weights does not match the population
# O número de pesos não corresponde à população
print(random.choices([1, 2, 3, 4, 5, 6], weights=[1, 1, 5, 1, 1, 5], k=5))
# Ex.: [6, 3, 3, 3, 6]

# Retorna k elementos sem repetição de uma sequência.
print(random.sample(range(1, 33), 3))  # Ex.: [18, 14, 13]


# Embaralha os elementos de uma lista in-place (altera a lista original).
lista = [1, 2, 3, 4, 5]
# None (não há retorno, embaralha direto na lista)
print(random.shuffle(lista))
print(lista)  # Ex.: [3, 4, 2, 5, 1]

# ​​# DESAFIO 🥇
# # Desafios Random
# 1. Você quer simular a opção de jogar uma moeda e resultar em cara ou coroa
#     jogue as opções dentro de uma variável e depois crie um programa que imprimir 'cara' ou 'coroa' na tela
# 2. Você quer fazer um sorteio entre 5 nomes em uma lista de nomes
#     Crie uma lista de 5 nomes e sorteie um nome de dentro dessa lista e exiba na tela
# 3. você quer escolher aleatóriamente um número de 10-100
#     Imprima na tela um valor aleatório entre 10 e 100
# Desafio 1
cara_coroa = random.choice(['Cara', 'Coroa'])
print(cara_coroa)

# Desafio 2
sorteio = random.choice(
    ['Fernando', 'Lidja', 'Eduardo', 'Gustavo', 'Cicleide'])
print(sorteio)

# Desafio 3
num_aleatorio = random.randint(10, 100)
print(num_aleatorio)
