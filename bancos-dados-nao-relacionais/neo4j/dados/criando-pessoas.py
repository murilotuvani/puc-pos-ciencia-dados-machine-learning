from faker import Faker
import random
import datetime

# Diferenta em anos entre uma data e outra
def anos_entre_datas(data_inicial, data_final):
  anos = data_final.year - data_inicial.year
  if (data_final.month < data_inicial.month or
      (data_final.month == data_inicial.month and data_final.day < data_inicial.day)):
    anos -= 1
  return anos


# Data de nascimento das pessoas
# Normalmente as pessoas na faculadade tem mais de 17 anos e menos de 50 anos.
# Dias vividos para ter 17 anos 17x365 = 6205
# Dias vividos com 50 anos, 50x365 = 18250.
minimo = 6205
maximo = 18250
    
fake = Faker('pt_BR')

pessoas = []
for _ in range(10):
    nome = fake.name()
    dias_vividos = random.randint(minimo, maximo)
    hoje = datetime.date.today()
    delta = datetime.timedelta(days=dias_vividos)
    data_nascimento = hoje - delta
    idade = anos_entre_datas(data_nascimento, hoje)
    pessoa = {
        'nome': nome,
        'data_nascimento': data_nascimento,
        'idade': idade
    }
    pessoas.append(pessoa)
    
    
for pessoa in pessoas:
    print(pessoa)
    #print(f'{pessoa['nome']}, data de nascimento {pessoa['data_nascimento']}, idade: {pessoa['idade']}')
