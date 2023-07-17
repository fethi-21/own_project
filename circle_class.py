import math
class Cercle():
    def __init__(self,a,b,r):
        self.a=a
        self.b=b
        self.r=r
    def surface(self):
        return(math.pi*self.r**2 )
    def perim(self):
        return (2*math.pi*self.r)
#test function deleted
cer=Cercle(1,2,1)
print(cer.surface())
print(cer.perim())


#branche22

#branche11

