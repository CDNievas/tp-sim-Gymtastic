from lib.Simulacion import Simulacion

simu = Simulacion(3, 8, 1440, False, logging=True)
simu.start()
simu.printResultados()