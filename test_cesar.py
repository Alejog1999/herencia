from cesar import Cesar

def test_create_cesar():
    cesar = Cesar(3)
    assert cesar.clave == 3

def test_clave_must_be_integer():
    try:
        Cesar("algo que no es un entero")
        variable_de_comprobacion=0
    except AttributeError:
        variable_de_comprobacion = 1
    assert variable_de_comprobacion == 1


    