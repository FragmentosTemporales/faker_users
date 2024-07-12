from faker import Faker
import random

fake = Faker('es_ES')

class FakeUser:
    def __init__(self):
        self.nombre = fake.first_name()
        self.apellido = fake.last_name()
        self.año = random.randint(1950, 2004)
        self.mes = self.seleccionar_mes()
        self.dia = self.seleccionar_dia()

    def seleccionar_mes(self):
        meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']
        return random.choice(meses)

    def seleccionar_dia(self):
        if self.mes == 'Febrero':
            return random.randint(1, 28)
        elif self.mes in ['Abril', 'Junio', 'Septiembre', 'Noviembre']:
            return random.randint(1, 30)
        else:
            return random.randint(1, 31)

    def mostrar_usuario(self):
        return {
            "nombre": self.nombre,
            "apellido": self.apellido,
            "año": self.año,
            "mes": self.mes,
            "dia": self.dia
        }

if __name__=="__main__":
    usuario = FakeUser()
    print(usuario.mostrar_usuario())
