class Calcul():
    def __init__(self,n):
        self.n=n
    def factorielle(self):
        fact=1
        for i in range(1,abs(self.n)+1):
            fact=fact*i
        return fact
    def somme(self):
        s=0
        for i in range(1,self.n+1):
            s=s+i
            return s
    def testPerim(self):
        for i in range(1,10):
            if (self.n%i==0 and i!=self.n and i!=1):
                return False
            else:
                continue
        return True
    def testPrims(k,m):
     while k%m>0 or m%m>0:
        if k>m:
            k=k%m
        else:
            m=m%k
        








fact=Calcul(6)
print(fact.factorielle())
print(fact.testPerim())
