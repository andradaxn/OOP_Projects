class Bani(object):
    """reprezinta suma de bani in euro;
    atribute: euro(valoare intreaga) si centi(valoare fractionara)"""

    def __init__(self, euro=0, centi=0):
        self.euro=euro
        self.centi=centi

    def __str__(self):
        if self.centi>=100:
            self.centi-=100
            self.euro+=1
        return '%s EUR & %s centi' % (self.euro, self.centi)

    def transformare(self):
        self.centi=self.euro*100+self.centi
        return self.centi

    def transformare_(self):
        self.euro=self.centi/100.0
        return self.euro
    
    def dobanda(self):
        self=self.euro+24*(2.5/100*self.euro)
        return self

    def __add__(self, other):
        sum=Bani()
        sum.euro=self.euro+other.euro
        sum.centi=self.centi+other.centi
        if sum.centi>=100:
            sum.centi-=100
            sum.euro+=1
        return sum

    def __sub__(self,other):
        dif=Bani()
        dif.euro=self.euro-other.euro
        dif.centi=self.centi-other.centi
        if dif.euro<0:
            return 'Nu sunt suficienti bani'
        elif dif.centi<0:
            dif.euro-=1
            dif.centi+=100
            return dif
        else:
            return dif

    def __cmp__(self,other):
        if self.euro>other.euro: return 1
        if self.euro<other.euro: return -1
        if self.centi>other.centi: return 1
        if self.centi<other.centi: return -1
        return 0


    
bani=Bani()
bani.euro=int(raw_input('euro1='))
bani.centi=int(raw_input('centi1='))

bani_=Bani()
bani_.euro=int(raw_input('euro2='))
bani_.centi=int(raw_input('centi2='))


print bani
"""print 'Suma in centi este', bani.transformare()
print 'Suma in euro este', bani.transformare_()
print 'Valoarea cu dobanda este', bani.dobanda()"""
print 'Suma totala este', bani+bani_
print 'Diferenta este', bani-bani_
print bani>bani_
