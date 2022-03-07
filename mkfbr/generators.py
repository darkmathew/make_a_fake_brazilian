from random import (
    randrange,
    randint,
    choice
)
from mkfbr.models import (
    Cities,
    States,
    CEPS,
    session
)
from json import loads
from datetime import datetime
from os.path import ( 
    abspath, 
    dirname, 
    join as path_join
)


def generate_rg(output_mode=''):
    rg = [randrange(9) for _ in range(7)]

    for _ in range(2):
        value = sum([(len(rg) + 1 - i) * v for i, v in enumerate(rg)]) % 11
        rg.append(11 - value if value > 1 else 0)


    rg = "".join(str(x) for x in rg)

    if output_mode == 'points':
        rg = f'{rg[:2]}.{rg[2:5]}.{rg[5:8]}-{rg[8:]}'

    return rg


def generate_cpf(output_mode=''):
    cpf = [randrange(10) for _ in range(9)]

    for _ in range(2):
        value = sum([(len(cpf) + 1 - i) * v for i, v in enumerate(cpf)]) % 11
        cpf.append(11 - value if value > 1 else 0)

 
    cpf = "".join(str(x) for x in cpf)

    if output_mode == 'points':
        cpf = f'{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}'

    return cpf


def generate_cnpj(output_mode=''):
    cnpj = [randrange(10) for _ in range(8)] + [0, 0, 0, 1]

    for _ in range(2):
        value = sum(v * (i % 8 + 2) for i, v in enumerate(reversed(cnpj)))
        digit = 11 - value % 11
        cnpj.append(digit if digit < 10 else 0)

    cnpj = "".join(str(x) for x in cnpj)

    if output_mode == 'points':
        cnpj = f'{cnpj[:2]}.{cnpj[2:5]}.{cnpj[5:8]}/{cnpj[8:12]}-{cnpj[12:14]}'

    return cnpj
    

def generate_name(gender_name='R'):

    
    basedir = abspath(dirname(__file__))
    content_file = path_join(basedir, 'json', 'content.json')

    with open(content_file, encoding='utf-8', mode='r') as r:
        file_data = loads(r.read())
    
    if gender_name == 'R':
        gender_name =  choice(['F', 'M'])

    if gender_name == 'F':
        female_names_list = file_data['content']['female_names']
        name = choice(female_names_list)
    else:
        male_names_list = file_data['content']['male_names']        
        name = choice(male_names_list)

    surname_list = file_data['content']['surnames']  
    surname = choice(surname_list)
    last_name = choice(surname_list)

    full_name = f'{name} {surname} {last_name}'
    return full_name


def generate_birthday_date():
    day = randint(1, 27)
    if day < 10:
        day = f'0{day}'

    month = randint(1, 12)
    if month < 10:
        month = f'0{month}'

    year = randint(1922, 2004)

    birthday = f'{day}/{month}/{year}'

    person_age = datetime.today().year - year

    return birthday, person_age


def generate_person_address():

    states_list = session.query(States).all()

    for i in range(10):
        state = choice(
            states_list
        )

        state_name = state.name
        
        state_short_name = state.short_name

        cities = session.query(Cities).filter_by(state_id=state.id).all()

        cities = choice(cities)
    
        
        address = session.query(CEPS).filter(
            CEPS.city_id==int(cities.id)
        ).all()
      
        if address == []:
            continue
    
        address = choice(address)
        break

    location = {
        "state_abbreviation": state_short_name,
        "logradouro": address.logradouro if address.logradouro else "",
        "address": address.cep if address.cep else "",
        "bairro": address.nome_do_bairro if address.nome_do_bairro else "",
        "city": cities.name if cities.name else "",
        "state": state_name
    }
    return location

