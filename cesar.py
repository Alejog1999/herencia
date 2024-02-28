class Cesar:
    alfabeto = list("ABCDEFGHIJKLMNÑOPQRSTUVWXYZ")
    def __init__(self,clave):
        if isinstance(clave,int):
            self.clave = clave
        else:
            raise AttributeError(f"{clave} debe ser un entero")

    def encriptar(self,mensaje):
        '''
        Para cada caracter del mensaje
        1. Obtener su posiicon en el alfabeto
        2. Sumar clave a posicion
        3. Obtener caracter en nueva posicion
        Devolver la concatenacion de todos los nuevos caracteres
        '''
        mensaje_encriptado=""
        for caracter in mensaje:
            if caracter not in self.alfabeto:
                new_caracter = caracter
            else:
                pos = self.alfabeto.index(caracter)
                new_pos = pos + self.clave
                new_caracter = self.alfabeto[new_pos]
            mensaje_encriptado += new_caracter
        return mensaje_encriptado