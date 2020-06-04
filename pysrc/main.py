#coding=utf-8
from QiPan import QiPan
class Move(object):
    def move(self, v):
        if len(v) != 4:
            raise Exception("Input must be a xxxx character string.")
        else:
            p_1 = int(v[0]),int(v[1])
            p_2 = int(v[2]),int(v[3])
            return p_1,p_2
m = Move()
qp = QiPan()
while True:
    qp.show()
    print("input 4 number, like 2011 means move R from 20 to 11. @exit.")
    a = input()
    if a != 'exit' and a != 'testMove':
        qp.moveR(m.move(a))
        qp.show()
        print("move N.")
        b = input()
        qp.moveN()
        qp.show()
        #qp.showPass()
    elif a == 'testMove':
        qp.move_pa()
    elif a == 'exit':
        break
#qp.getPoint(a)