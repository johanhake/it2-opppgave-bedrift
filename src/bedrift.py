class Ansatt:
    def __init__(self, navn:str, lønn:float, ansattnr:int)->None:
        self.navn = navn
        self.lønn = lønn
        self.ansattnr = ansattnr

class Leder(Ansatt):
    def __init__(self, navn:str, lønn:float, ansattnr:int):
        super().__init__(navn, lønn, ansattnr)
        self.ansatte = []

    def legg_til_ansatt(self, ansatt:Ansatt):
        pass

class Bedrift:
    def __init__(self, navn:str)->None:
        self.navn = navn
        self.ansatte = []

    def legg_til_ansatt(self, navn:str, lønn:float, leder_navn:str):
        pass
    
    def legg_til_leder(self, navn:str, lønn:float):
        pass
    
