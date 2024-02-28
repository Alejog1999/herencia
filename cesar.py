class Cesar:
    def __init__(self,clave):
        if isinstance(clave,int):
            self.clave = clave
        else:
            raise AttributeError(f"{clave} debe ser un entero")

    