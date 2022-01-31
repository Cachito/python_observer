import datetime

def deco_clase(cls):
    class Env:
        def __init__(self, *args):
            self.instance = cls(*args)

        def __getattr__(self, nombre):
            file = f'log_{datetime.datetime.now().strftime("%Y_%m_%d")}.txt'
            cadena = f'{datetime.datetime.now().strftime("%H:%M:%S")}'
            cadena = f'{cadena}-{self.instance}-{nombre}: '

            log = open(f'./log/{file}', 'a')
            log.write(f'{cadena}\n')
            log.close()

    return Env
