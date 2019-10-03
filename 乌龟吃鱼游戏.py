import random  as r
class Fish:
    def prd_fish(self):
        self.x = r.randint(0,10)
        self.y = r.randint(0, 10)
    def Fish_move(self):
        q = True
        while q:
            x1 = self.x + r.randint(-1, 1) - self.x
            y1 = self.y + r.randint(-1, 1) - self.y
            if abs(x1)+abs(y1) == 1:
                self.x = self.x + x1
                self.y = self.y + y1
                if  (0 <= self.x <= 10) and (0 <= self.y<= 10):
                    q = False
                    print("鱼的位置：",self.x, self.y)
                else:
                    self.x = self.x - x1
                    self.y = self.y - y1
    def getXY(self):
        return self.x,self.y
class Turtle:
    active = 100
    def prd_turtle(self):
        self.x = r.randint(0, 10)
        self.y = r.randint(0, 10)
    def Turtle_move(self):
        q = True
        while q:
            x1 = self.x + r.randint(-2, 2) - self.x
            y1 = self.y + r.randint(-2, 2) - self.y
            if abs(x1)+abs(y1) == 2:
                self.x = self.x + x1
                self.y = self.y + y1
                if  (0 <= self.x <= 10) and (0 <= self.y<= 10):
                    q = False
                    print("乌龟的位置：",self.x, self.y)
                    print("乌龟血量：",self.active)
                    print("\n")
                    self.active -= 1
                else:
                    self.x = self.x - x1
                    self.y = self.y - y1
    def getturtleXY(self):
        return self.x,self.y

if __name__ == '__main__':
    print("游戏开始了：")
    p1 = Fish()
    p2 = Fish()
    p3 = Fish()

    q = Turtle()
    q.prd_turtle()
    p1.prd_fish()
    p2.prd_fish()
    p3.prd_fish()
    count = 3
    k1 = True
    k2 = True
    k3 = True
    while count:
        if k1 and p1.getXY() == q.getturtleXY():
            print("吃掉了一条鱼")
            k1 = False
            del p1
            print(q.getturtleXY())
            print(count)
            count -= 1
            q.active += 20
            if q.active >= 100:
                q.active =100
        if k2 and p2.getXY() == q.getturtleXY():
            print("吃掉了一条鱼")
            k2 = False
            del p2
            print(q.getturtleXY())
            count -= 1
            q.active += 20
            if q.active >= 100:
                q.active =100
        if k3 and p3.getXY() == q.getturtleXY():
            print("吃掉了一条鱼")
            k3 = False
            del p3
            print(q.getturtleXY())
            print(count)
            count -= 1
            q.active += 20
            if q.active >= 100:
                q.active =100
        else:
            if q.active < 0:
                print("乌龟饿死了")
                break
            if k1:
                p1.Fish_move()
            if k2:
                p2.Fish_move()
            if k3:
                p3.Fish_move()
            q.Turtle_move()

