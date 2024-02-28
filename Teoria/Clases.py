from validators import valida_dni
class persona:
    def __init__(self,nombre,apellido,correo_e,dni):
        self.nombre = nombre
        self.apellidos= apellido
        self.correo_e=correo_e
        self.dni=valida_dni(dni)

    def nombre_completo(self):
         return f"{self.nombre} {self.apellidos.capitalize()}"
        
class Estudiante(persona):
    def __init__(self, nombre, apellido, correo_e,dni,curso):
        super().__init__(nombre, apellido, correo_e,dni)
        self.curso=curso
    def info(self):
        return f"{self.nombre_completo()} {self.curso}"

class Profesor(persona):
    pass