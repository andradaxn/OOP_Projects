import math

class Punct(object):
    """reprezinta un punct in spatiul 2D"""
    
    def __init__(self, x=0, y=0):
        self.x=x
        self.y=y

    def __str__(self):
        return '(%.d,%.d)' % (self.x,self.y)

    def __add__(self, other):
        return self.x + other.x
    
class Dreptunghi(object):
    """reprezinta un dreptunghi
    atribute:colt stanga jos, largime si inaltime"""

    def __init__(self, p, largime, inaltime):
        self.colt=p
        self.largime=largime
        self.inaltime=inaltime

    def __str__(self):
        return '(%s,%d,%d)' % (self.colt, self.largime, self.inaltime)   
                 
    def arie(self):
        return self.largime*self.inaltime

    def perimetru(self):
        return 2*(self.largime+self.inaltime)

    def ariacercinsc(self):
        if self.inaltime<self.largime:
            return math.pi*(self.inaltime/2.0)**2
        else:
            return math.pi*(self.largime/2.0)**2

    def ariacerccirc(self):
        return math.pi*((math.sqrt(self.largime**2+self.inaltime**2))/2)**2

    def translatie(self, dx, dy):
        dreptunghi=Dreptunghi(Punct(),self.largime,self.inaltime)
        dreptunghi.colt.x = self.colt.x + dx
        dreptunghi.colt.y = self.colt.y + dy
        return dreptunghi
    

A=Punct()
A.x=float(raw_input('abscisa punctului='))
A.y=float(raw_input('ordonata punctului='))

print A

box=Dreptunghi(Punct(),0,0)
box.colt = A
box.largime = float(raw_input('largime='))
box.inaltime = float(raw_input('inaltime='))

print box
            
print 'aria este', box.arie()

print 'perimetrul este', box.perimetru()

print 'aria cercului inscris', box.ariacercinsc()

print 'aria cercului circumscris', box.ariacerccirc()

print 'dreptunghiul translatat', box.translatie(10,20)
