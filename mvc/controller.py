from mvc.model import Model
from modulos.deco_clase import deco_clase
@deco_clase
class Controller:
    def __init__(self):
        self.model = Model()

    def save(self, observador, descripcion, valor):
        try:
            #print("saving")
            self.model.save(observador, descripcion, valor)
            return True

        except Exception as e:
            print(str(e))
            return False
