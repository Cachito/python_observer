from modulos.db_clases import db
from modulos.db_clases import Observacion

class Model:
    """
    Model
    modelo del programa
    """
    def __init__(self):
        try:
            db.connect()
            db.create_tables([Observacion])

            print("base y tabla creadas")

        except Exception as exc:
            print(f"Error al iniciar {str(exc)}")

        finally:
            db.close()

    def save(self, observador, descripcion, valor):
        """
        alta
        crea un registro
        """
        if not db.is_closed():
            db.close()

        try:
            db.connect()

            Observacion.create(Observador = observador, Descripcion = descripcion, Valor = valor)

            return True

        except Exception as exc:
            print(f"Error al crear registro {str(exc)}")

            return False

        finally:
            db.close()
