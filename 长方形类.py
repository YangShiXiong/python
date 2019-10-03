class Rect:
    def __init__(self,width,high):
        self.width = width
        self.high = high
    def setRect(self,width,high):
        self.width = width
        self.high = high

    def getRect(self):
        return self.high,self.width

    def gteArea(self):
        return self.high * self.width
if __name__ == '__main__':
    high = int(input('请输入长方形的长：'))
    width = int(input('请输入长方形的宽：'))
    k = Rect(width,high)
    print(k.gteArea())
    print(k.getRect())