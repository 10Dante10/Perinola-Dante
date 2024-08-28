
class Apuesta:
    def __init__(self):
       self.fichas =0
    def __repr__(self):
        return f"Apuesta: {self.fichas} salio" 
    def PonerFichas(self,cuantas=1):
        self.fichas = self.fichas + cuantas
