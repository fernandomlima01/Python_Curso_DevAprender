# Projeto 1 - Cadastre-me
# Objetivo de projeto

# Estamos criando um módulo de login do nosso aplicativo, e você deve obter as seguintes informações do funcionário.

# Módulo 1 - Gerar registro do funcionário
# Funcionalidades do módulo 1
'''
        1. Obtenha o nome do usuário
        2. Obtenha a idade do usuário
        3. Registre de forma automática a data do cadastro do usuário, usando a data do registro como data de registro
        4. Para cada novo funcionário que é registrado na empresa, ele recebe um dos seguintes cartões, que é sorteado de forma aleatória:
        '''
# cartoes = ['R$50,00','R$250,00','R$120,00']
# 5. Guarde informações sobre a data de aniversário do funcionário(dd/mm/aaaa)

# Módulo 2 - Gerar apresentação do usuário
# Funcionalidades do módulo 2 - Mensagem de boas vindas!
'''
    Usando os dados obtidos no módulo 1, exiba as seguintes informações:
        1.  Olá (nome do usuário), seu registro foi concluído com sucesso no dia(data de cadastro no formato dd/mm/aaaa).
            Parabéns, houve um sorteio e você ganhou um cartão de compras no valor de (valor sorteado).
'''
import random
from datetime import datetime

nome_usuario = input('Digite seu nome: ')
formato = '%d/%m/%Y'
data_nasc_usuario = input("Digite o data do seu nascimento (dd/mm/aaaa): ")
# Transformando em datatime
data_nasc_usuario1 = datetime.strptime(data_nasc_usuario, formato)
#print(data_nasc_usuario1, type(data_nasc_usuario1))

# Pega data e hora do momento
dataHoraAtual = datetime.now()
# Transforma em String no formato dd/mm/aaaa (só pega a Data)
dataAtual = dataHoraAtual.strftime(formato)
#print(dataAtual, type(dataAtual))

# Dia/mês atual == dia aniversário (True = 1),ou seja, dia do aniversário
# Dia/mês atual (antes) < dia aniversário (True = 1), ou seja, não completou aniversário
# Dia/mês atual (depois) > dia aniversário (False = 0), ou seja, já completou aniversário
confimacao_aniversario = ((dataHoraAtual.month, dataHoraAtual.day) < (data_nasc_usuario1.month, data_nasc_usuario1.day))
#print(confimacao_aniversario)
# Diferença em anos, menos a confirmação (se completou ou não aniversário)
idadeUsuario = (dataHoraAtual.year - data_nasc_usuario1.year) - confimacao_aniversario
#print(idadeUsuario)

# Lista dos cartões do sorteio
cartoes = ['R$50,00', 'R$250,00', 'R$120,00']
sorteio = random.choice(cartoes) # Escolhe um item aleatório da lista
# print(sorteio)

print(f"O(A) Sr(a). {nome_usuario} tem {idadeUsuario} anos de idade;\n"
      f"Nascido em {data_nasc_usuario}.\n\n"
      f"Olá {nome_usuario}, seu registro foi concluído com sucesso\n"
      f"no dia {dataAtual}. Parabéns, houve um sorteio e você ganhou\n"
      f"um cartão de compras no valor de {sorteio}.")
