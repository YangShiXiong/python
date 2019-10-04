import math
class Point:

    def __init__(self,x1,y1,x2,y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
    def setXY(self,x1,y1,x2,y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
    def getXY(self):
        return self.x1,self.y1,self.x2,self.y2
class Line(Point):
    def __init__(self,x1,y1,x2,y2):
        super(Line, self).__init__(x1,y1,x2,y2)
    def getLine(self):
        self.length = abs((self.x1-self.x2)*2)+abs((self.y1-self.y2)*2)
        return math.sqrt(self.length)

if __name__ == '__main__':
    p = Line(1,1,2,2)
    print(p.getLine())