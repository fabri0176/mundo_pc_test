from mundo_pc.monitor import Monitor
from mundo_pc.teclado import Teclado
from mundo_pc.raton import Raton
from mundo_pc.computadora import Computador
from orden import Orden

monitor1 = Monitor('Logitech', 15)
monitor2 = Monitor('Maxell', 24.5)

teclado1 = Teclado('HP', 'USB')
teclado2 = Teclado('Genius', 'ANT+')

raton1 = Raton('HP', 'USB')
raton2 = Raton('Acer', 'Bluetooth')

computador1 = Computador('PC 1', monitor1, teclado1, raton1)
computador2 = Computador('PC 2', monitor2, teclado2, raton2)

computadoras1 = [computador1, computador2]

orden = Orden(computadoras1)

print(orden)