
with open('exemplo.txt','r') as arquivo:
    for linha in arquivo:
        print(linha, end='')

arquivo = open('exemplo.txt', 'r')
try:
    for linha in arquivo:
        print(linha)
finally:
    arquivo.close()

open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)

# Abrir um arquivo para leitura:
arquivo = open('exemplo.txt', 'r')

# Abrir um arquivo para escrita, sobrescrevendo o conteúdo:
arquivo = open('exemplo.txt', 'w')

# Abrir um arquivo para leitura e escrita:
arquivo = open('exemplo.txt', 'r+')

# Abrir um arquivo em modo binário para leitura:
arquivo = open('imagem.jpg', 'rb')

# read(): Lê todo o conteúdo do arquivo como uma única string.
with open('exemplo.txt', 'r') as arquivo:
    conteudo = arquivo.read()
    print(conteudo)

# readline(): Lê uma linha do arquivo por vez.
with open('exemplo.txt', 'r') as arquivo:
    linha = arquivo.readline()
    print(linha)

# readlines(): Lê todas as linhas do arquivo e retorna uma lista.
with open('exemplo.txt', 'r') as arquivo:
    linhas = arquivo.readlines()
    print(linhas)

# write(): Escreve uma string no arquivo.
with open('exemplo.txt', 'w') as arquivo:
    arquivo.write("Texto exemplo\n")

# writelines(): Escreve uma lista de strings no arquivo.
with open('exemplo.txt', 'w') as arquivo:
    arquivo.writelines(["Linha 1\n", "Linha 2\n", "Linha 3\n"])

# Iterar sobre o arquivo: Você pode iterar linha por linha diretamente:
with open('exemplo.txt', 'r') as arquivo:
    for linha in arquivo:
        print(linha.strip())  # Remove o '\n'


# Fechar o arquivo:
# Quando você usa with, o arquivo é automaticamente fechado no final.
# Se não usar with, feche manualmente com close():
arquivo = open('exemplo.txt', 'r')
conteudo = arquivo.read()
arquivo.close()

# encoding: Ao abrir arquivos de texto, você pode especificar a codificação (importante para evitar erros com caracteres especiais):
with open('exemplo.txt', 'r', encoding='utf-8') as arquivo:
    conteudo = arquivo.read()


with open('teste.txt', 'r') as arquivo:
    for linha in arquivo:
        print(linha.strip())  # Remove o '\n' do final de cada linha


lista = [1, 2, 3]
iterador = iter(lista)  # Cria o iterador

print(next(iterador))  # Saída: 1
print(next(iterador))  # Saída: 2
print(next(iterador))  # Saída: 3
# print(next(iterador))  # Gera StopIteration porque a lista acabou