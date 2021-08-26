from mundo_pc.monitor import Monitor as Mon
from mundo_pc.teclado import Teclado as Tec
from mundo_pc.raton import Raton as Rat

class Computador:
    contador_computadoras = 0

    def __init__(self, nombre, monitor, teclado, raton):
        Computador.contador_computadoras += 1
        self._id_computadora = Computador.contador_computadoras

        self._nombre = nombre
        self._monitor = monitor
        self._teclado = teclado
        self._raton = raton

    def __str__(self):
        return f'''
        {self._nombre}: {self._id_computadora}
        Monitor: {self._monitor}
        Teclado: {self._teclado}
        Raton: {self._raton}
        '''

if __name__ == '__main__':
    monitor1 = Mon('Logitech', 15)
    monitor2 = Mon('Maxell', 24.5)

    teclado1 = Tec('HP', 'USB')
    teclado2 = Tec('Genius', 'ANT+')

    raton1 = Rat('HP', 'USB')
    raton2 = Rat('Acer', 'Bluetooth')

    computador1 = Computador('PC 1', monitor1, teclado1, raton1)
    computador2 = Computador('PC 2', monitor2, teclado2, raton2)

    print(computador1)
    print(computador2)