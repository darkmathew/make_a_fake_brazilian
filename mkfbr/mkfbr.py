from generators import (
    generate_cnpj,
    generate_cpf,
    generate_rg,
    generate_name,
    generate_person_address,
    generate_birthday_date
)


class Make_A_Fake_Brazilian:

    def __init__(self, 
        cpf_mode='', 
        cnpj_mode='', 
        gen_cnpj=False, 
        rg_mode='',
        gender_name='R',
        
    ) -> None:        
        self.gender_name = gender_name
        self.cpf_mode = cpf_mode
        self.cnpj_mode = cnpj_mode
        self.rg_mode = rg_mode

        self.rg = generate_rg(
            output_mode=self.rg_mode
        )

        self.cpf = generate_cpf(
            output_mode=self.cpf_mode
        )

        self.gen_cnpj = gen_cnpj

        if self.gen_cnpj:
            self.cnpj = generate_cnpj(
                output_mode=self.cnpj_mode)
        else:
            self.cnpj = ""

        
        self.birthday, self.age  = generate_birthday_date()        
        self.name = generate_name()
        self.location_data = generate_person_address()
        
        self.address = self.location_data['address']
        self.logradouro = self.location_data['logradouro']
        self.state = self.location_data['state']
        self.state_abbreviation = self.location_data['state_abbreviation']
        self.city = self.location_data['city']
        self.bairro = self.location_data['bairro']
        


    def get_brazilian(self):

        person_data = {
            "name": self.name,
            "age": self.age,
            "birthday": self.birthday,
            "cpf": self.cpf,
            "rg": self.rg,
            "cnpj": self.cnpj,
            "address": self.address,
            "state": self.state,
            "state_abbreviation": self.state_abbreviation,
            "city": self.city,
            "bairro": self.bairro,
            "logradouro": self.logradouro
        }
        return person_data









