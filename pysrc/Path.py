# 建立点与点之间的连接。
# 走棋子的时候扫描friends，有空位x则可以走。friends上面都有N或者R，那么就说明没地方可走了。憋死了。
class Path:
    
    def __init__(self,pos = (0,0), friends= {(0,0)}, num=0, way=1):
        self._number = num
        self._way = way
        self._actPoint = pos
        self._friends = friends

    def getNumber(self):
        return self._number

    def getWay(self):
        return self._way

    def getFriends(self):
        return self._friends

    def getActPoint(self):
        return self._actPoint

    def show(self):
        print("friends: " + str(self.getFriends()))
        print("Number: " + str(self.getNumber()))
        print("Way: " +str(self.getWay()))

# pa = Path((0,0),{(0,2),(2,0)},1,2)
# pa.show()


    # def checkWay(self, p):
        