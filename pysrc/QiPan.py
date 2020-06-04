#写一个棋盘，里面可以放棋子。
#-*-conding:utf-8-*-

#   0 1 2
# 0 N - N 
# 1 I X # 
# 2 R - R 

from QiZi import QiZi
from Path import Path
class QiPan:
    
    def __init__(self):
        self._xPos = (1,1)
        self._nPos = (0,0)
        #self._map = [(0,0), (0,2),(1, 1),(2, 0),(2, 2)]
        self._map = [QiZi((0,0),'N'),QiZi((0,1),'-'), QiZi((0,2),'N'),QiZi((1, 0), '|'),QiZi((1, 1), 'x'), QiZi((1, 2), '#'),QiZi((2, 0), 'R'),QiZi((2,1),'-'),QiZi((2,2),'R')]
        self._pass = [Path((0,0),{(2,0),(1,1),(0,2)},1,3),Path((0,2),{(0,0),(1,1)},2,2),Path((1,1),{(0,0),(0,2),(2,0),(2,2)},3,4),Path((2,0),{(0,0),(1,1),(2,2)},4,3),Path((2,2),{(2,0),(1,1)},5,2)]

    def show(self):
        line = -1
        count = 0
        print('  0 1 2')
        for i in self._map:
            if count%3 == 0:
                line +=1
                print(str(line) + ' ', end ='')
            count += 1
            print(i._value + ' ', end='')            
            if count%3 ==0 and count != 0:
                print()

    def move_test(self):
        print('move key R from 2:0 to 1:1')
        for i in self._map:
            if i._point == (2,0):
                i.setValue('x')
            if i._point ==(1,1):
                i.setValue('R')
    
    def move_pa(self):
        print("D: QiPan::move_pa")
        for pa in self._pass:
            if pa._actPoint == (0,2):
                print("find the path point." + str(pa._actPoint))


    def moveR(self,point_1,point_2):
        print("D: QiPan::moveR(point_1,point_2")
        if self.checkR(point_1) == 0:
            self.getPoint(point_1).setDefault()
            self.getPoint(point_2).setR()
        else:
            print("Please move R key.")

    def moveR(self,points):
        print("D: QiPan::moveR(points)")
        if self.checkR(points[0]) == 0:
            self.getPoint(points[0]).setDefault()
            self.getPoint(points[1]).setR()
        else:
            print("Please move R key2.")

    def getPoint(self,point):
        print("D: QiPan::getPoint(point)")
        for p in self._map:
            if point == p.getPos():
                return p
        print("Got nothing.")
        return None

    def checkR(self,point):
        if self.getPoint(point).getValue() == 'R':
            return 0
        else:
            return -1

    def moveN(self):
        print("D: QiPan::moveN")

        # 需要知道哪里下子。 findX
        # 升级版：需要在friends里找到x才能移动。 20200406
        print("xpos is :" + str(self._xPos))
        self._xPos = self.findX()
        # 哪里有N findN
        self._nPos = self.findN()
        # 将X点置为N
        self.getPoint(self._xPos).setN()
        # 将找到的N置为x
        self.getPoint(self._nPos).setDefault()
        print("after modify xpos is : " + str(self._nPos))
        print("after modify npos is : " + str(self._nPos))
        # checkN  需要checkN
        print("Can't move N key. YOU WIN!!!")
        self.checkPass()
    
    def findX(self):
        print("D: QiPan::findX")
        for p in self._map:
            if p.getValue() == 'x':
                return p.getPos()
        print("Can't find x point.")

    def findN(self):
        print("D: QiPan::findN")
        for p in self._map:
            if p.getValue() == 'N':
                return p.getPos()
        print("Can't find N point.")

    def showPass(self):
        for pa in self._pass:
            pa.show()

    def checkPassFriends(self):
        print("D: QiPan::checkPass")
        for pa in self._pass:
            for friend in pa.getFriends():
                if self.findX() == friend:
                    print("find x in friend.")
                    return friend
        return None
    
    def checkPassPoint(self):
        print("D: QiPan::checkPassPoint")
        for pa in self._pass:
            if self.findN() == pa.getActPoint():
                print("find N in point.")
                return pa.getActPoint()
        return None