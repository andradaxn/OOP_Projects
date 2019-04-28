class Matrice(object):
    """reprezinta o matrice
        atribute: a11, a12, a21, a22"""

    def __init__(self, a11=0, a12=0, a21=0, a22=0):
        self.a11=a11
        self.a12=a12
        self.a21=a21
        self.a22=a22

    def __str__(self):
        return '%s  %s\n%s  %s' % (self.a11, self.a12, self.a21, self.a22)

    def __eq__(self, other):
        return self.a11==other.a11 and self.a12==other.a12 and self.a21==other.a21 and self.a22==other.a22

    def __add__(self, other):
        sum=Matrice()
        sum.a11=self.a11+other.a11
        sum.a12=self.a12+other.a12
        sum.a21=self.a21+other.a21
        sum.a22=self.a22+other.a22
        return sum

    def __mul__(self, other):
        prod=Matrice()
        prod.a11=self.a11*other.a11+self.a12*other.a21
        prod.a12=self.a11*other.a12+self.a12*other.a22
        prod.a21=self.a21*other.a11+self.a22*other.a21
        prod.a22=self.a21*other.a12+self.a22*other.a22
        return prod
        
    def transpusa(self):
        transp=Matrice()
        transp.a11=self.a11
        transp.a12=self.a21
        transp.a21=self.a12
        transp.a22=self.a22
        return transp

    def determinant(self):
        det=self.a11*self.a22-self.a12*self.a21
        return det

    def inm_scalar(self):
        self.a11*=scalar
        self.a12*=scalar
        self.a21*=scalar
        self.a22*=scalar
        return self

matrice=Matrice()
matrice.a11=int(raw_input('Dati valoare elementului de pe pozitia a11 in prima matrice: '))
matrice.a12=int(raw_input('Dati valoare elementului de pe pozitia a12 in prima matrice: '))
matrice.a21=int(raw_input('Dati valoare elementului de pe pozitia a21 in prima matrice: '))
matrice.a22=int(raw_input('Dati valoare elementului de pe pozitia a22 in prima matrice: '))

matrice_=Matrice()
matrice_.a11=int(raw_input('Dati valoare elementului de pe pozitia a11 in a doua matrice: '))
matrice_.a12=int(raw_input('Dati valoare elementului de pe pozitia a12 in a doua matrice: '))
matrice_.a21=int(raw_input('Dati valoare elementului de pe pozitia a21 in a doua matrice: '))
matrice_.a22=int(raw_input('Dati valoare elementului de pe pozitia a22 in a doua matrice: '))

scalar=int(raw_input('Dati valoare pentru scalar: '))

print matrice
print matrice_
print 'matrice=matrice_', matrice==matrice_
print matrice.transpusa(), '(transpusa matricei)'
print matrice+matrice_, '(suma matricelor)'
print matrice*matrice_, '(produdul matricelor)'
print 'determinantul matricei: ', matrice.determinant()
print matrice.inm_scalar(), '(produsul cu scalar)'


