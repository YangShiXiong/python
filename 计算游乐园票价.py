class Ticket:
    nomally = 100
    week = 100*1.2
    child = 100//2
    def getValue(self):
        return 2*self.nomally+self.child

if __name__ == '__main__':

    p = Ticket()
    print(p.getValue())