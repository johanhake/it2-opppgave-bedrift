class Ansatt:
    def __init__(self, navn:str, lønn:float, ansattnr:int)->None:
        if not isinstance(navn, str):
            raise TypeError(f"Forventet {type('')} for navn, fikk {type(navn)}")
    
        if not isinstance(lønn, float):
            raise TypeError(f"Forventet {type(0.1)} for lønn, fikk {type(lønn)}")

        if not isinstance(ansattnr, int):
            raise TypeError(f"Forventet {type(1)} for ansattnr, fikk {type(ansattnr)}")

        self.navn = navn
        self.lønn = lønn
        self.ansattnr = ansattnr

class Leder(Ansatt):
    def __init__(self, navn:str, lønn:float, ansattnr:int):
        super().__init__(navn, lønn, ansattnr)
        self.ansatte = []

    def legg_til_ansatt(self, ny_ansatt:Ansatt):
        if not isinstance(ny_ansatt, Ansatt):
            raise TypeError(f"Forventet Ansatt for ansatt, fikk {type(ny_ansatt)}")

        # Må vi endre lønnen?
        if self.lønn < ny_ansatt.lønn*1.5:
            self.lønn = ny_ansatt.lønn*1.5
        
        self.ansatte.append(ny_ansatt)

class Bedrift:
    def __init__(self, navn:str)->None:
        self.navn = navn
        self.ansatte = []

    def legg_til_ansatt(self, navn:str, lønn:float, leder_navn:str):
    
        if not isinstance(leder_navn, str):
            raise TypeError(f"Forventet {type('')} for leder_navn, fikk {type(leder_navn)}")
    
        # Oppretter Ansatt
        ny_ansatt = Ansatt(navn, lønn, len(self.ansatte)+1)
        
        # Finner lederen
        leder_ikke_funnet = True
        for leder in self.ansatte:
            if isinstance(leder, Leder) and leder.navn == leder_navn:
                leder_ikke_funnet = False
                leder.legg_til_ansatt(ny_ansatt)
        if leder_ikke_funnet:
            raise ValueError(f"Leder med navn {leder_navn} er ikke registrert.")

        # Legger til den nye ansatte
        self.ansatte.append(ny_ansatt)

        return ny_ansatt
        
    def legg_til_leder(self, navn:str, lønn:float):

        # Oppretter Leder
        ny_leder = Leder(navn, lønn, len(self.ansatte)+1)
        
        # Legger til den nye ansatte
        self.ansatte.append(ny_leder)    

        return ny_leder    
    
