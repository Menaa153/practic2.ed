
class Direccion:
    def __init__(self, calle, noCalle, nomenclatura, barrio, ciudad):
        self._calle = calle
        self._noCalle = noCalle
        self._nomenclatura = nomenclatura
        self._barrio = barrio
        self._ciudad = ciudad
    
    def get_calle(self):
        return self._calle
    
    def get_noCalle(self):
        return self._noCalle
    
    def get_nomenclatura(self):
        return self._nomenclatura
    
    def get_barrio(self):
        return self._barrio
    
    def get_ciudad(self):
        return self._ciudad
    
    def __str__(self):
        return f"{self._calle} {self._noCalle} {self._nomenclatura} {self._barrio} {self._ciudad}"
