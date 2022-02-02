from asyncio import constants
import datetime
import modulos.constantes as constant

def deco_clase(cls):
    class Env:
        def __init__(self, *args):
            self.instance = cls(*args)

        def __getattr__(self, nombre):
            clase = type(self.instance).__name__ # Instancia de la clase.

            file = f'log_{datetime.datetime.now().strftime("%Y_%m_%d")}.txt'
            cadena = f'{datetime.datetime.now().strftime("%H:%M:%S")}'
            cadena = f'{cadena} --> {clase}.{nombre}'

            log = open(f'{constant.RUTA_LOG}{file}', 'a')
            log.write(f'{cadena}\n')
            log.close()

            return getattr(self.instance, nombre)

    return Env
