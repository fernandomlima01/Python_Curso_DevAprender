# Métodos Comuns de Uma String
nome_curso = '  Edição de Vídeo  '
#             0123456789012345678     indice
print(nome_curso.upper())   # Caixa Alta
print(nome_curso.lower())   # Letras Minusculas
print(nome_curso.strip())   # Retira os espaços em branco
print(nome_curso.lstrip())  # Retira os espaços em branco Lado Esquerdo
print(nome_curso.rstrip())  # Retira os espaços em branco Lado Direito
# Busca o valor (número) do Indice da primeira letra escrita
print(nome_curso.find('Ví'))
#  Substitui palavras
print(nome_curso.replace('Vídeo', 'Música'))
# Exemplo Substituição de palavras
print('https://sc.olx.com.br/?o=90&q=relogio'.replace('relogio', 'carro'))

# DESAFIO 🥇
""" Através da criação de string dinâmicos e os métodos de um string que acabou de aprender, 
use como base as variáveis a seguir para criar as seguintes frases """

a = 'é'
b = 'MELHOR'
c = 'QUE'
d = 'feito'
e = 'perfeito'

print(f'{a.upper()} {b.lower()} {d.upper()} {c.lower()} {e.upper()}')
