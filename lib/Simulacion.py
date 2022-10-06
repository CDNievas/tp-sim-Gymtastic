from lib.Profesores import Profesores
from lib.fdp import IA, TA
from lib.log import log

class Simulacion():

    def __init__(self, CP, CAP, TF, FIN_DE_SEMANA, IA=IA, TA=TA, logging=False):
        self.HV = float("inf")
        self.CP = CP
        self.CAP = CAP
        self.TF = TF
        self.FIN_DE_SEMANA = FIN_DE_SEMANA
        self.logging = logging
        
        self.IA = IA
        self.TA = TA

        self.t = 0
        self.tpll = self.IA(FIN_DE_SEMANA)
        self.ns = 0
        self.simu = True

        self.ntp = 0
        self.ntpr = 0
        self.ntpa = 0
        self.pr = 0

        self.profesores = Profesores(self.CP, self.CAP, self.HV)

    def start(self):

        while (self.simu):
            profesorTPS, tps = self.profesores.buscarMenorTPS()
            log("T: %s - TF:%s - TPLL: %s - TPS: %s" % (self.t,self.TF,self.tpll,tps), self.logging)

            if (self.tpll <= tps):
                # Llegada
                log("Evento: Llegada", self.logging)
                self.t = self.tpll
                ia = self.IA(self.FIN_DE_SEMANA)
                log("IA: %s" % ia, self.logging)
                self.tpll = self.t + ia
                self.ntp = self.ntp + 1

                profesorLibre = self.profesores.buscarProfesorLibre()

                if profesorLibre == None:
                    # Rechazo
                    self.ntpr = self.ntpr + 1

                else:
                    # Toma clase
                    self.ns = self.ns + 1
                    self.ntpa = self.ntpa + 1
                    ta = self.TA(self.FIN_DE_SEMANA)
                    tps = self.t + ta
                    profesorLibre.putTPS(tps)
                    profesorLibre.incNTPA()

            else:
                # Salida
                log("Evento: Salida", self.logging)
                self.t = tps
                profesorTPS.removeTPS(tps)
                self.ns = self.ns - 1

            # Vaciamiento
            if (self.t <= self.TF):
                self.simu = True
            else:
                self.simu = False
                if(self.ns > 0):
                    self.simu = True
                    self.tpll = self.HV

            log("-----------------------------------------", self.logging)

        # Calculos
        self.pr = self.ntpr / self.ntp * 100

        for profesor in self.profesores.getList():
            profesor.calcPPAP(self.ntpa)

    def getResultados(self):
        return self.pr, self.profesores.getList()

    def printResultados(self):
        print("RESULTADOS:")
        print("Porcentaje de rechazados: %s/%s - %s%%" % (self.ntpr, self.ntp, self.pr))

        for profesor in self.profesores.getList():
            index = profesor.getIndex()
            ppap = profesor.getPPAP()
            print("Profesor %s - Porcentaje de rentabilidad: %s%%" % (index, ppap))


