import pytest
from Jugador import Jugador
def test_constructor():
  j =Jugador("Andres",6)
  assert(j.nombre == "Andres")
  assert(j.fichas ==6)




def test_constructor_sin_fichas():
  j =Jugador("Andres")
  assert(j.nombre == "Andres")
  assert(j.fichas == 5)




def test_dar_ficha():
  j = Jugador("Andres", 10)
  j.darFicha(5)
  assert(j.fichas ==15)


def test_dar_ficha_sin_fichas():
  j = Jugador("Andres")
  j.darFicha()
  assert(j.fichas == 6)


def test_sacar_ficha():
  j = Jugador("Andres",10)
  j.sacarFicha(5)
  assert(j.fichas == 5)


def test_sacar_ficha_sin_fichas():
  j = Jugador("Andres",10)
  j.sacarFicha()
  assert(j.fichas == 9)


def test_sacar_ficha_de_mas():
  j = Jugador("Andres",10)
  with pytest.raises(ValueError):
   j.sacarFicha(11)


def test_no_tiene_fichas():
   j = Jugador("Andres",10)
   j.sacarFicha(10)
   assert(j.fichas == 0)


def test_tiene_ficha():
  j = Jugador("Andres", 5)
  j.sacarFicha(2)
  assert(j.fichas >= 1)


def test_tiene_ficha_sin_fichas():
  j = Jugador("Andres", 5)
  j.sacarFicha()
  assert(j.fichas >= 1)
