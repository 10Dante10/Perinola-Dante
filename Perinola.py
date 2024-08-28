from random import choice
class Perinola:
     def __init__(self):
         self.cara_visible = "Pone 1"
     def __repr__(self):
          return f"Salio: {self.cara_visible}" 
     def tirar (self):
      caras = ("Pone 1", "Toma 2", "Todos Ponen",
               "Toma 1", "Pone 2", "Toma Todo")
      self.cara_visible = choice(caras) 
      return self.cara_visible      
