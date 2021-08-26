class Monitor:

    contador_monitores = 0

    def __init__(self, marca, tamano):
        Monitor.contador_monitores += 1
        self._id_monitor = Monitor.contador_monitores
        self._marca = marca
        self._tamano = tamano

    def __str__(self):
        return f'Id:{self._id_monitor}, Tamaño: {self._tamano}, Marca: {self._marca}'

if __name__ == '__main__':
    monitor1 = Monitor('Logitech',15)
    monitor2 = Monitor('Maxell', 24.5)

    print(monitor1)
    print(monitor2)