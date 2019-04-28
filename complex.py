import math

class Complex(object):
    """reprezinta un numar sub forma complexa
    atribute: parte reala, parte imaginara"""

    def __init__(self, real=0, imaginar=0):
        self.real=real
        self.imaginar=imaginar

    def __str__(self):
        if self.imaginar>0:
            return '%s+%si' % (self.real, self.imaginar)
        else:
            return '%s %si' % (self.real, self.imaginar)

    def __add__(self, other):
        sum=Complex()
        sum.real=self.real+other.real
        sum.imaginar=self.imaginar+other.imaginar
        return sum

    def __mul__(self, other):
        prod=Complex()
        prod.real=self.real*other.real-self.imaginar*other.imaginar
        prod.imaginar=self.imaginar*other.real+self.real*other.imaginar
        return prod

    def modul(self):
        mod=math.sqrt(self.real**2+self.imaginar**2)
        return mod

    def conjugat(self): 
        conj=Complex()
        conj.real=self.real
        conj.imaginar=-self.imaginar
        return conj

    def formatrig(self): #de aranjat
        r=math.sqrt(self.real**2+self.imaginar**2)
        fi=math.atan(self.imaginar/self.real)
        return '%s(cos%s+isin%s)' % (r,fi,fi)

    def __eq__(self,other):
        return self.real==other.real and self.imaginar==other.imaginar


z=Complex()
z.real=int(raw_input('Re(z)='))
z.imaginar=int(raw_input('Im(z)='))

w=Complex()
w.real=int(raw_input('Re(w)='))
w.imaginar=int(raw_input('Im(z)='))

print 'z=', z
print 'w=', w
print 'Suma este', z+w
print 'Produsul este', z*w
print 'Modulul lui z este', z.modul()
print 'Conjugatul lui z este', z.conjugat()
print 'Forma trigonometrica a lui z este', z.formatrig()
print 'z=w', z==w
