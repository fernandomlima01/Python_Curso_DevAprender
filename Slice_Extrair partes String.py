# Slice (extraindo partes de uma String)
objeto = 'Teclado'
#         0123456
print(objeto[2])  # Mostra o 2 indice, letra 'c'
print(objeto[-1])  # Mostra o último indice da string, letra 'o'
print(objeto.index('d'))  # Mostra o número do Indíce do caractere

# Mostrando o que ta dentro do index
print(objeto[objeto.index('d')]) 



# Acessando partes de uma string
link = 'facebook.com/devaprender'
#       012345678901234567890123
#                      -5-4-3-2-1
print(link[0])    # Primeiro item do Indice
print(link[-1])   # Último item do indice

# Mostra o indice inicial e o final (não imprimindo o final)
# ou seja ele imprime os indeces 0-1-2-3-4
print(link[0:5])   # faceb

# Imprime do indice mostrado até o final
print(link[0:])

# começa de tras pra frente
# começando a partir do -5 até o último
print(link[-5:])   # ender

# Começa do indice 5 até o final
print(link[5:])

# Começa do indice 0 até o -5 (o indece -5 não é impresso)
print(link[:-5])


# Caractere Repetido
# Acessando a última ocorrência de um caractere
frase = 'Clean Code'
print(frase.rindex('C'))  # Mostra o valor Index do último 'C'


# DESAFIO
#1- Encontrar o indece 'o' dentro da variavel 'Biblioteca'
biblioteca = 'Biblioteca'
print(biblioteca.index('o'))

#2- Imprima apenas as palavras 'De Aplicações'
frase = 'Desenvolvimento De Aplicações'
print(frase[frase.rindex('D'):])

# Outra forma de resolver
indice_d = frase.rindex('D')
indice_s = frase.rindex('s')
# adicionar o +1 para que o último caractere apareça
print(frase[indice_d:indice_s+1])  # COM +1
print(frase[indice_d:indice_s])  # SEM +1