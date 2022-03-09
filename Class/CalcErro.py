class CalcErro():
    import math as mt
    def __init__(self, x = 0, erro1= 0, z = 0, erro2 = 0, i = 0, erro3 = 0, l = 0, erro4 = 0 ):
        self.x = x
        self.erro1 = erro1
        self.z = z
        self.erro2 = erro2
        self.i = i
        self.erro3 = erro3
        self.l = l
        self.erro4 = erro4
    
    def soma (self):
        s1 = (self.x + self.z)
        e1 = (self.erro1 + self.erro2)
        s2 = (self.i + self.l)
        e2 = (self.erro3 + self.erro4)
        st = s1 + s2
        et = e1+e2
        print (f'Sua soma deu {st} e seu erro deu {et}')
    
    def sub (self):
        s1 = (self.x - self.z)
        e1 = (self.erro1 + self.erro2)
        s2 = (self.i - self.l)
        e2 = (self.erro3 + self.erro4)
        st = s1 - s2
        et = e1+e2
        print (f'Sua subtração deu {st} e seu erro deu {et}')      
    
    def prod (self):
        p1 = (self.x * self.z)
        e1 = ((self.z * self.erro1) + (self.x * self.erro2))
        p2 = (self.i * self.l)
        e2 = ((self.l * self.erro3) + (self.i * self.erro4))
        if p2 != 0:
            pt = (p1 * p2)
            et = (e1 * p2)+ (e2 * p1)
        else:
            pt = p1
            et = e1
        print (f'Seu produto deu {pt} e seu erro deu {et}')     

    def div (self):
        s1 = (self.x / self.z)
        e1 = (((self.z * self.erro1) + (self.x * self.erro2))/(self.z**-2))
        if self.i != 0:
            s2 = (self.i / self.l)
            e2 = (((self.l * self.erro3) + (self.i * self.erro4))/(self.i**-2))
        else:
            s2 = 0
            e2 = 0  
        if s2 == 0:          
            st = s1 + s2
            et = e1 + e2
        else:
            st = s1 / s2
            et = ((e1*s2) + (e2*s1))/(s2**-2)       
        print (f'Sua divisão deu {st} e seu erro deu {et}')
    
    def cos (self):
        if self.x != 0:
            cos1 = CalcErro.mt.cos(self.x)
            e1 = (CalcErro.mt.sin(self.x)) * self.erro1
            print(f'O cos é igual a {cos1} com o erro {e1}')
        

        if self.z != 0:
            cos2 = CalcErro.mt.cos(self.z)
            e2 = (CalcErro.mt.sin(self.z)) * self.erro2
            print(f'O cos é igual a {cos2} com o erro {e2}')        
        if self.i != 0:
            cos3 = CalcErro.mt.cos(self.i)
            e3 = (CalcErro.mt.sin(self.i)) * self.erro3
            print(f'O cos é igual a {cos3} com o erro {e3}')
        
        if self.l != 0:
            cos4 = CalcErro.mt.cos(self.l)
            e4 = (CalcErro.mt.sin(self.l)) * self.erro4
            print(f'O cos é igual a {cos4} com o erro {e4}')
        
    def sen (self):
        if self.x != 0:
            cos1 = CalcErro.mt.sin(self.x)
            e1 = (CalcErro.mt.cos(self.x)) * self.erro1
            print(f'O sen é igual a {cos1} com o erro {e1}')
        

        if self.z != 0:
            cos2 = CalcErro.mt.sin(self.z)
            e2 = (CalcErro.mt.cos(self.z)) * self.erro2
            print(f'O sen é igual a {cos2} com o erro {e2}')        
        if self.i != 0:
            cos3 = CalcErro.mt.sin(self.i)
            e3 = (CalcErro.mt.cos(self.i)) * self.erro3
            print(f'O sen é igual a {cos3} com o erro {e3}')
        
        if self.l != 0:
            cos4 = CalcErro.mt.sin(self.l)
            e4 = (CalcErro.mt.cos(self.l)) * self.erro4
            print(f'O sen é igual a {cos4} com o erro {e4}')
    
    def log (self):


        if self.x != self.z :
            l1 = CalcErro.mt.log(self.x)
            e1 = self.erro1/self.x
            print(f'O log é {l1} e o erro é {e1}')

        if self.z != self.x :
            l2 = CalcErro.mt.log(self.z)
            e2 = self.erro2/self.z
            print(f'O log é {l2} e o erro é {e2}')

        if self.i != self.l:
            l3 = CalcErro.mt.log(self.i)
            e3 = self.erro3/self.i
            print(f'O log é {l3} e o erro é {e3}')

        if self.l != self.i:
            l4 = CalcErro.mt.log(self.l)
            e4 = self.erro4/self.l
            print(f'O log é {l4} e o erro é {e4}')
    
    def raiz (self):

        if self.x != 0:
            sq1 = CalcErro.mt.sqrt(self.x)
            e1 = (self.erro1)/(2*CalcErro.mt.sqrt(self.x))
            print(f'Seu raiz quadrada foi de {sq1}e o erro foi de {e1}')
        
        if self.z != 0:
            sq2 = CalcErro.mt.sqrt(self.z)
            e2 = (self.erro2)/(2*CalcErro.mt.sqrt(self.z))
            print(f'Seu raiz quadrada foi de {sq2}e o erro foi de {e2}')
       
        if self.i != 0:
            sq3 = CalcErro.mt.sqrt(self.i)
            e3 = (self.erro3)/(2*CalcErro.mt.sqrt(self.z))
            print(f'Seu raiz quadrada foi de {sq3}e o erro foi de {e3}')
        
        if self.l != 0:
            sq4 = CalcErro.mt.sqrt(self.l)
            e4 = (self.erro4)/(2*CalcErro.mt.sqrt(self.l))
            print(f'Seu raiz quadrada foi de {sq4}e o erro foi de {e4}')

    






        

        




s = CalcErro(2 , 0.01, 3, 0.002)

s.prod()
s.div()
