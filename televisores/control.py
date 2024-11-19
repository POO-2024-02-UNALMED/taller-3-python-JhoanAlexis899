class Control:
  def __init__(self):
    self._tv = None

  def turnOn(self):
    if self._tv is not None:
      self._tv.turnOn()
  def turnOff(self):
    if self._tv is not None:
      self._tv.turnOff()
  def canalUp(self):
    if self._tv is not None:
      self._tv.canalUp()
  def canalDown(self):
    if self._tv is not None:
      self._tv.canalDown()
  def volumenUp(self):
    if self._tv is not None:
      self._tv.volumenUp()
  def volumenDown(self):
    if self._tv is not None:
      self._tv.volumenDown()
  def setVolumen(self, i):
    if self._tv is not None:
      self._tv.setVolumen(i)
  def setCanal(self, j):
    if self._tv is not None:
      self._tv.setCanal(j)
  def enlazar(self, tv):
    self._tv = tv
    tv.setControl(self)
  def setTv(self, tv):
    self.enlazar(tv)
  def getTv(self):
    return self._tv