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
        self._nPos2 = (0,2)
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
        self._xPos = self.findX()
        print("xpos is :" + str(self._xPos))
        self._nPos = self.findN()
        self.moveNToFriend(self._nPos,self._xPos)
        #self.checkPass()

    def moveNToFriend(self,nPoint,xPoint):
        print("D: QianPan::moveNToFriend")
        if nPoint == None or xPoint == None:
            print("Can't move N key. YOU WIN!!!")

        # checkN  需要checkN
        elif self.getPath4Point(nPoint).isFriend(xPoint):
            print("is friend can move to this point")
                # 将X点置为N
            self.getPoint(self._xPos).setN()
            # 将找到的N置为x
            self.getPoint(self._nPos).setDefault()
            print("after modify xpos is : " + str(self._xPos))
            print("after modify npos is : " + str(self._nPos))
        # checkN  需要checkN

    
    def findX(self):
        print("D: QiPan::findX")
        for p in self._map:
            if p.getValue() == 'x':
                return p.getPos()
        #print("Can't find x point.")

    #需要修改一下这个逻辑。让代码自己找到能走的N。而不是找第一个N。
    def findN(self):
        for p in self._map:
            if p.getValue() == 'N' and self.checkPassFriends(p.getPos()):
                print("get N pos: " + str(p.getPos()))
                return p.getPos()
        print("Can't find N.")
        return None

    def showPass(self):
        for pa in self._pass:
            pa.show()

    def getPassFriends(self):
        print("D: QiPan::getPassFriends")
        for pa in self._pass:
            for friend in pa.getFriends():
                if self._xPos == friend:
                    print("find x in friend.")
                    return friend
        return None
    
    def checkPassFriends(self,point):
        print("D: QiPan::checkPassFriends")
        if self._xPos in self.getPath4Point(point).getFriends():  # maybe wrong.
            print("x pos: " + str(self._xPos) + "friends: " + str(self.getPath4Point(point).getFriends()))
            return True
        else:
            return False

    def checkPassPoint(self,point):
        print("D: QiPan::checkPassPoint")
        for pa in self._pass:
            if self.findN() == pa.getActPoint():
                print("find N in point.")
                return pa.getActPoint()
        return None
    
    def getPath4Point(self,point):
        for pa in self._pass:
            if point == pa.getActPoint():
                print("getPath4Point: npos: " + str(point) +" pa act point: " + str(pa.getActPoint()))
                return pa
