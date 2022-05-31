from faker import Faker
from random import randint
from datetime import date
from unidecode import unidecode

f = Faker(['pt_BR'])
hoje = date.today()
anoatual = int(hoje.strftime('%Y'))

#Nome, idade, e-mail, cidade
def pessoa():
        
    nome = f.first_name() + ' ' + f.last_name()
    idade = randint(18,75)
    anonascimento = str(anoatual - idade)
    usuario = unidecode(nome).lower()
    email = usuario.replace(' ', '') + anonascimento[-2:] + '@' + f.free_email_domain()
    local = f.city() + '/' + f.estado_sigla()

    pessoa = [nome, idade, email, local]

    return pessoa