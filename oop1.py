class Table:
    def __init__(self,l,w,h):
        self.long = l
        self.width = w
        self.height = h

    def outing(self):
        print (self.long,self.width,self.height)


class Kitchen(Table):
    def howplaces(self,n):
        if n < 2:
            print ("It is not kitchen table")
        else:
            self.places = n
    def outplases(self):
        print (self.places)

class Worker(Table):
    def __init__(self, l, w, h, material):
        super().__init__(l, w, h)
        self.material = material

    def howmany(self, num):
        if num < 1:
            print("Invalid number of workers")
        else:
            self.workers = num

    def outworkers(self):
        print("This table can accommodate", self.workers, "workers")

t_room1 = Kitchen(2,1,0.5)
t_room1.outing()
t_room1.howplaces(5)
t_room1.outplases()
t_2 = Table(1,3,0.7)
t_2.outing()
