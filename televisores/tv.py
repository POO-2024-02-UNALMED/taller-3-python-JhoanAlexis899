class TV:
  _numTv = 0
  def __init__(self, marca, estado):
      self._marca = marca
      self._estado = estado
      self._control = None
      self._precio = 500
      self._canal = 1
      self._volumen = 1
      TV._numTv += 1
  def getMarca(self):
      return self._marca
  def setMarca(self, nuevaMarca):
      self._marca = nuevaMarca
  def getCanal(self):
      return self._canal
  def setCanal(self, nuevoCanal):
      if self._estado and (nuevoCanal >= 1 and nuevoCanal <= 120):
        self._canal = nuevoCanal
  def getPrecio(self):
      return self._precio
  def setPrecio(self, nuevoPrecio):
      self._precio = nuevoPrecio
  def getVolumen(self):
      return self._volumen
  def setVolumen(self, nuevoVolumen):
      if self._estado and (nuevoVolumen >= 0 and nuevoVolumen <= 7):
        self._volumen = nuevoVolumen
  def getControl(self):
      return self._control
  def setControl(self, nuevoControl):
      self._control = nuevoControl
  @classmethod
  def getNumTV(cls):
    return cls._numTv
  @classmethod  
  def setNumTV(cls, numero):
    cls._numTv = numero
  def turnOn(self):
    self._estado = True
  def turnOff(self):
    self._estado = False
  def getEstado(self):
    return self._estado
  def canalUp(self):
    if self._estado and self._canal < 120:
      self._canal += 1
  def canalDown(self):
    if self._estado and self._canal > 1:
      self._canal -= 1
  def volumenUp(self):
    if self._estado and self._volumen < 7:
      self._volumen += 1
  def volumenDown(self):
    if self._estado and self._volumen > 0:
      self._volumen -= 1