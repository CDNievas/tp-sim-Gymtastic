from typing import Tuple, List
from lib.Profesor import Profesor

class Profesores:

    def __init__(self, cp, cap, hv):
        self._hv = hv
        self.profesores = []

        for i in range(cp):
            self.profesores.append(Profesor(cap, hv, i))

    def buscarProfesorLibre(self) -> Profesor:

        profesoresLibres = list(filter(lambda x: any(tps == self._hv for tps in x.getTPSList()), self.profesores))
        profesoresLibres.sort(key=lambda x: x.getSlotsLibres())

        if len(profesoresLibres) > 0:
            return profesoresLibres[0]
        else:
            return None

    def buscarMenorTPS(self) -> Tuple[Profesor, int]:

        sMinTPS = self._hv
        sProfesor = None

        for profesor in self.profesores:
            
            profMinTPS = profesor.getMinTPS()
            
            if(sMinTPS >= profMinTPS):
                sMinTPS = profMinTPS
                sProfesor = profesor

        return sProfesor, sMinTPS

    def getSlotsLibres(self) -> int:
        return len(list(sum(list(map(lambda x: x.getSlotsLibres(), self.profesores), []))))


    def getList(self) -> List[Profesor]:
        return self.profesores