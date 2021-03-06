from peewee import *
from datetime import datetime
from modulos.deco_clase import deco_clase


db = SqliteDatabase('./db/observer_base.db')

class BaseModel(Model):
    """
    modelo de base de datos
    """
    class Meta:
        """
        metadata
        """
        database = db

class Observacion(BaseModel):
    """
    tabla Observaciones
    """
    class Meta:
        """
        metadata
        """
        Database = db
        table_name = "Observaciones"

    Fecha = DateTimeField(default=datetime.now)
    Observador = CharField()
    Descripcion = CharField()
    Valor = IntegerField()
