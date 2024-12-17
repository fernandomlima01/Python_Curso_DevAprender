# Datetime
from datetime import datetime

# Obtendo a data e hora atuais
agora = datetime.now()
print("Data e hora atuais:", agora)
print(agora.year)
print(agora.month)
print(agora.day)
print(agora.hour)
print(agora.minute)
print(agora.second)

# Criando uma data e hora específicas
data_hora_personalizada = datetime(2024, 6, 17, 14, 30, 45)
print("Data e hora personalizadas:", data_hora_personalizada)

# Acessando componentes de data e hora
print("Ano:", data_hora_personalizada.year)
print("Mês:", data_hora_personalizada.month)
print("Dia:", data_hora_personalizada.day)
print("Hora:", data_hora_personalizada.hour)
print("Minuto:", data_hora_personalizada.minute)
print("Segundo:", data_hora_personalizada.second)

from datetime import date

# Obtendo a data atual
data_atual = date.today()
print("Data atual:", data_atual)

# Criando uma data específica
data_personalizada = date(2024, 6, 17)
print("Data personalizada:", data_personalizada)

# Acessando componentes da data
print("Ano:", data_personalizada.year)
print("Mês:", data_personalizada.month)
print("Dia:", data_personalizada.day)

from datetime import time

# Criando um objeto de hora
hora_personalizada = time(14, 30, 45)  # 14:30:45
print("Hora personalizada:", hora_personalizada)

# Acessando componentes da hora
print("Horas:", hora_personalizada.hour)
print("Minutos:", hora_personalizada.minute)
print("Segundos:", hora_personalizada.second)

from datetime import datetime

# Objeto datetime atual
agora = datetime.now()
print(type(agora))  # <class 'datetime.datetime'>

# Formatando a data em uma String
data_formatada = agora.strftime("%d/%m/%Y %H:%M:%S")
print("Data formatada:", data_formatada)  # Data formatada: 17/12/2024 01:20:59
print(type(data_formatada))  # <class 'str'>

from datetime import datetime

# Convertendo string para datetime
data_string = "17/06/2024 14:30:45"
formato = "%d/%m/%Y %H:%M:%S"
data_objeto = datetime.strptime(data_string, formato)
print("Objeto datetime:", data_objeto) # Objeto datetime: 2024-06-17 14:30:45

# Data de uma Input
data_manual = input("digite a Data: ")  # Dia/Mês/Ano
print(f"Data: {data_manual}, cuja classe é: {type(data_manual)}")
# Data: 15/03/2025, cuja classe é: <class 'str'>

# Formatação de data de uma Input em 'datetime.datetime'
data_manual1 = datetime.strptime(input("Digite a Data: "),'%d/%m/%Y')
print(f"Data: {data_manual1}, cuja classe é: {type(data_manual1)}")
# Data: 2025-01-20 00:00:00, cuja classe é: <class 'datetime.datetime'>

from datetime import datetime, timedelta

# Criando um objeto timedelta
delta = timedelta(days=7, hours=5, minutes=30)

# Soma de tempo
data_hora_atual = datetime.now()
nova_data_hora = data_hora_atual + delta
print("Data e hora atual:", data_hora_atual)
print("Data e hora após o delta:", nova_data_hora)

# Subtração de tempo
data_anterior = data_hora_atual - delta
print("Data e hora antes do delta:", data_anterior)

# Diferença entre datas
data1 = datetime(2024, 6, 10)
data2 = datetime(2024, 6, 17)
diferenca = data2 - data1
print("Diferença entre datas:", diferenca.days, "dias")

# Desafio
# Contagem de dias
data_futura = '06/09/2025'
data_atual = datetime.now() # 17/12/2024
dias_que_faltam = datetime.strptime(data_futura, "%d/%m/%Y") - data_atual
print(dias_que_faltam.days) # 262
