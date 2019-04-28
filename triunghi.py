# -*- coding: cp1252 -*-
import math

class Punct(object):
    """reprezinta un punct in spatiul 2D
    atribute: coordonatele sale"""

    def __init__(self, x=0, y=0):
        self.x=x
        self.y=y

    def __str__(self):
        return '(%.d,%.d)' % (self.x,self.y)

class Triunghi(object):
    """reprezinta un triunghi
    atribute: cele 3 colturi"""

    def __init__(self, a, b, c):
        self.A=a
        self.B=b
        self.C=c

    def __str__(self):
        return '(%s,%s,%s)' % (self.A, self.B, self.C)

    def arie(self):
        det=self.A.x*self.B.y+self.B.x*self.C.y+self.C.x*self.A.y-self.C.x*self.B.y-self.B.x*self.A.y-self.A.x*self.C.y
        arie=(math.fabs(det))/2
        return arie

    def perimetru(self):
        per=a+b+c
        return per

    def rt_pitagora(self):
        if a>b and a>c:
            return a**2==b**2+c**2

        elif b>a and b>c:
            return b**2==a**2+c**2

        else:
            return c**2==a**2+b**2

    def echilat(self):
        return a==b and a==c and b==c

    def isoscel(self):
        return a==b or a==c or b==c


    def inaltime(self,other):
        h=(2*self.arie())/other
        return h



A=Punct()
A.x=float(raw_input('abscisa punctului A='))
A.y=float(raw_input('ordonata punctului A='))

B=Punct()
B.x=float(raw_input('abscisa punctului B='))
B.y=float(raw_input('ordonata punctului B='))

C=Punct()
C.x=float(raw_input('abscisa punctului C='))
C.y=float(raw_input('ordonata punctului C='))

triunghi=Triunghi(Punct(), Punct(), Punct())
triunghi.A=A
triunghi.B=B
triunghi.C=C

c=math.sqrt((triunghi.B.x-triunghi.A.x)**2+(triunghi.B.y-triunghi.A.y)**2)
b=math.sqrt((triunghi.C.x-triunghi.A.x)**2+(triunghi.C.y-triunghi.A.y)**2)
a=math.sqrt((triunghi.C.x-triunghi.B.x)**2+(triunghi.C.y-triunghi.B.y)**2)

sinA=(2*triunghi.arie())/(b*c)
sinB=(2*triunghi.arie())/(a*c)
sinC=(2*triunghi.arie())/(a*b)

print
if triunghi.arie()==0:
    
    print 'Cele trei puncte date sunt coliniare'
    exit

else:
    print 'Aria triungiului este', triunghi.arie()
    print 'Perimetrul triunghiului este', triunghi.perimetru()
    print
    print 'Triunghiul ABC este dreptunghic', triunghi.rt_pitagora()
    print 'Triunghiul este echilateral', triunghi.echilat()
    print 'Triunghiul este isoscel', triunghi.isoscel()
    print
    print 'Inaltimea din A este', triunghi.inaltime(a)
    print 'Inaltimea din B este', triunghi.inaltime(b)
    print 'Inaltimea din C este', triunghi.inaltime(c)
    print
    print 'Masura unghiului A este', round(math.degrees(math.asin(sinA))), '°'
    print 'Masura unghiului B este', round(math.degrees(math.asin(sinB))), '°'
    print 'Masura unghiului C este', round(math.degrees(math.asin(sinC))), '°'



