# String
# Toda String tem que estar entre aspas (Simples ou dupla)
print('Aspas simples')
print("Aspas duplas")

# String entre aspas Simples (ou dupla) tripla permite escrever na linha abaixo
print('''Aspas simples
      tripla''')
print("""Aspas triplas
      funciona também""")

# caracteres de escape
print('Olá meu nome é \nFernando')  # \n - quebra de linha
print('Codar todos \'os dias')      # \ - utilizar aspas no texto (barra invertida permite que Python ignore as aspas)
print('Caixa d\'água')

# Aspas simples pode ser colocada dentro de aspas duplas
print("Caixa d'água")

# Sem colocar barra invertida (SEM Escape)
print("C:\Users\ferna\Documents\Rascunho.txt")  # da erro
# Colocando barra invertida (Escape) para ignorar a barra invertida existente
print("C:\\Users\\ferna\\Documents\\Rascunho.txt")

# Contar a quantidade de cracteres
nome = 'Carol'
print(len(nome))

# Desafio
print('Vamos codar!')
print("Vamos 'codar!'")
print("Vamos\n'codar'")