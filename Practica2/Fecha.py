
class Fecha:
    def __init__(self, dd, mm, aaaa):
        self._dd = dd
        self._mm = mm
        self._aaaa = aaaa
    
    
    def getDD(self):
        return self._dd
    def setDD(self, dd):
        self._dd = dd
    
    def getMM(self):
        return self._mm
    def setMM(self, mm):
        self._mm = mm
    
    def getAA(self):
        return self._aaaa
    def setAA(self, aaaa):
        self._aaaa = aaaa
    
    
    def __str__(self):
        return f"{self._dd}-{self._mm}-{self._aaaa}"