
# What is make_a_fake_brazilian A.K.A mkfbr? Where is he going? Where does he come from? What does it feed on?

  
Well, this simple project was born out of a particular need in personal projects. Specifically I needed some information from Brazilians, such as: Name, Address, CPF, CPNJ, Age, among other things. Since then, I decided to make my job easier with a quick and simple to use module.

**Note:** This project only serves as an object of study and/or software testing, do not use it for fraudulent activities.

## Quick note about missing states in the database

The database for this project was built based on data provided by [CEP ABERTO](https://www.cepaberto.com/), which in turn did not include (when >darkmathew< performed the scraping) the following states: **Maranhão, Rio de Janeiro, Rio Grande do Norte, Roraima and Tocantins**. I apologize to you if you need data generated from any of these regions of Brazil. If you get this information and want to share it with the project, please submit a properly tested and verified PR that includes cities and zip codes for those states.


## Good news, now mkfbr has a free API and a front end version available!
**API repository URL** [click here](https://github.com/darkmathew/mkfbr-api)

**API URL** [click here](http://mkfbr-api.herokuapp.com/api/)

**MKFBR Website** [click here](http://mkfbr-api.herokuapp.com/site/)
 

## Install from PyPi

`pip install mkfbr`

  
## Simple Usage

```python

from mkfbr import Make_A_Fake_Brazilian

mkfbr = Make_A_Fake_Brazilian()

brazilian = mkfbr.get_brazilian()

print(brazilian)

```

Output example:

```

{
    'name': 'Egídia Angelles',
    'age': 47,
    'birthday': '26/11/1975',
    'cpf': '80051493608',
    'rg': '136076262',
    'cnpj': '',
    'address': 'Rua Expedito Pereira de Souza 971',
    'state': 'Acre',
    'state_abbreviation': 'AC',
    'city': 'Bujari',
    'bairro': 'Centro',
    'logradouro': ''
}

```

## Generate Female Person

```python

from mkfbr import Make_A_Fake_Brazilian

  
mkfbr = Make_A_Fake_Brazilian(

    gender_name='F',

)

brazilian = mkfbr.get_brazilian()

  
print(brazilian)

```


## Generate Male Person

```python

from mkfbr import Make_A_Fake_Brazilian


mkfbr = Make_A_Fake_Brazilian(

    gender_name='M',

)

brazilian = mkfbr.get_brazilian()

  
print(brazilian)

```

  
## Generate CPNJ / RG / CPF with pontuation


**Note:** To generate CNPJ the `gen_cnpj` argument needs to be true.


```python

from mkfbr import Make_A_Fake_Brazilian

  

mkfbr = Make_A_Fake_Brazilian(

    cpf_mode='points',

    rg_mode='points',

    gen_cnpj=True,

    cnpj_mode='points',

)

brazilian = mkfbr.get_brazilian()

print(brazilian)

```

  

Output example:

```

{
    'name': 'Eros de Assuncao',

    'age': 66,

    'birthday': '15/01/1956',

    'cpf': '058.592.229-20',

    'rg': '57.137.420-4',

    'cnpj': '60.294.437/0001-07',

    'address': 'Avenida André Pereira Lobato, s/n',

    'state': 'Piauí',

    'state_abbreviation': 'PI',

    'city': 'Sebastião Barros',

    'bairro': 'Centro',

    'logradouro': ''

}

```
