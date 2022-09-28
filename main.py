from utils.logo import printLogo
from utils.menu import printMenu, printMenuAgain
from lib.Simulacion import Simulacion

if __name__ == "__main__":
    printLogo()

    is_again = True
    while(is_again):
        CP, CAP, FIN_DE_SEMANA, TF = printMenu()

        simu = Simulacion(CP, CAP, TF, FIN_DE_SEMANA, logging=False)
        simu.start()
        simu.printResultados()

        is_again = printMenuAgain()