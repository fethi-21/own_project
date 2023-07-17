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
    def test(self,x,y):
        if math.sqrt((x-self.a)**2+(y-self.b)**2)==self.r:
            return True
        else:
            return False
cer=Cercle(1,2,1)
print(cer.surface())
print(cer.perim())
print(cer.test(1,1))
#branche3

