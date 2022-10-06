from typing import List


class Profesor:

    def __init__(self, cap, hv, index):

        self.index = index
        self._hv = hv
        self.ntpa = 0
        self.ppap = 0
        self.index = 0
        self.tps = []

        self.ppcapa = 0
        self.ppcapb = 0

        for i in range(cap):
            self.tps.append(hv)

    def putTPS(self, tps) -> None:
        self.tps.remove(self._hv)
        self.tps.append(tps)

    def removeTPS(self, tps) -> None:
        self.tps.remove(tps)
        self.tps.append(self._hv)

    def getMinTPS(self) -> int:
        self.tps.sort()
        return self.tps[0]

    def getSlotsLibres(self) -> int:
        return len(list(filter(lambda x: x == self._hv, self.tps)))

    def getTPSList(self) -> List[int]:
        return self.tps

    def incNTPA(self) -> None:
        self.ntpa = self.ntpa + 1

    def calcPPAP(self, ntpa) -> None:
        self.ppap = self.ntpa / ntpa * 100

    def getIndex(self) -> int:
        return self.index

    def getPPAP(self) -> float:
        return self.ppap

