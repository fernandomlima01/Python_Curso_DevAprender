# Split e Join

# Split - Separa as Strings
frase = 'Olá, bem-vindo a este treinamento'
print(frase.split())     # Separa as strings a cada espaço encontrado
print(frase.split(','))  # Separa as string a cada virgula encontrada (virgula some)
print(frase.split('-'))  # Separa as string a cada traço/hifem encontrado (traço/hifem some)

nomes = 'jhonatan, rafael, carol, amanda,jefferson'
print(nomes.split())
print(nomes.split(','))

hashtags = 'music #guitar #gamer #coder #python#azul#terra'
print(hashtags.split())
print(hashtags.split('#'))
print(hashtags.split(' #'))
print(hashtags.split('#', 3))  # '#'-indicando o separador; 3-quantas ocorrências até ele parar
print(hashtags.split('#', 5))  # '#'-indicando o separador; 5-quantas ocorrências até ele parar

# Join - Junta/inseri as Strings
# Como concatenar (combinar) strings
hashtag_separadas_por_espaco = hashtags.split(' ')
print(hashtag_separadas_por_espaco)
print(','.join(hashtag_separadas_por_espaco))
print(', '.join(hashtag_separadas_por_espaco))
print('.'.join(hashtag_separadas_por_espaco))
print('. '.join(hashtag_separadas_por_espaco))
print(' '.join(hashtag_separadas_por_espaco))

# DESAFIO
# ​Desafio 1: Transforme a frase1 em uma lista de palavras e guarde o resultado em uma variável chamada palavras1
# Desafio 2: Transforme a frase2 em uma lista de palavras e guarde o resultado em uma variável chamada palavras2
# Desafio 3: Pegue o palavras1 e transforme elas no seguinte string: "Desafio,manipulação,de,strings". Imprima o resultado no console.
# Desafio 4: Pegue o palavras2 e transforme elas no seguinte string: frase2 = "jhonatan & rafael & carol & camilla". Imprima o resultado no console.

frase1 = 'Desafio manipulação de strings'
frase2 = 'jhonatan,rafael,carol,camilla'

# Desafio 1
palavras1 = frase1.split()
print(palavras1)
# Desafio 2
palavras2 = frase2.split(',')
print(palavras2)
# Desafio 3
print(','.join(palavras1))
# Desafio 4
frase2 = ' & '.join(palavras2)
print(frase2)