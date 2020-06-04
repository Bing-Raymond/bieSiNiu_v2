#这个是棋子。怎么把他放到棋盘上呢？
class QiZi(object):

    def __init__(self, point=(0,0), value='-'):
        self._point = point
        self._value = value
        # self._number = 

    def getValue(self):
        return self._value

    def getPos(self):
        return self._point

    def setValue(self, value='-'):
        self._value = value
    
    def setR(self):
        self.setValue('R')

    def setN(self):
        self.setValue("N")

    def setDefault(self):
        self.setValue('x')