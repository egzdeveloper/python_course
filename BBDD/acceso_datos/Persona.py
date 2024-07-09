from logger_base import log

class Persona:
    def __init__(self, id_persona=None, nombre=None, apellido=None, email=None):
        self._id_persona = id_persona
        self._nombre = nombre
        self._apellido = apellido
        self._email = email

    @property
    def id_persona(self):
        return self._id_persona

    @property
    def nombre(self):
        return self._nombre

    @property
    def apellido(self):
        return self._apellido

    @property
    def email(self):
        return self._email

    @id_persona.setter
    def id_persona(self, id_persona):
        self._id_persona = id_persona

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido

    @email.setter
    def email(self, email):
        self._email = email

    def __str__(self):
        return (f'[{self._id_persona}] '
                f'Nombre: {self._nombre}, '
                f'Apellido: {self._apellido}, '
                f'Email: {self._email}')