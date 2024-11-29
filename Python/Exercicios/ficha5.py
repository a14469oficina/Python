from math import sqrt

class Triangulo :
    def __init__(self,lado1,lado2,lado3):
        self.lado1 =lado1
        self.lado2 =lado2
        self.lado3 =lado3

    def isTriangulo(self):
        return self.lado1 < self.lado2 + self.lado3 and self.lado2 < self.lado1 + self.lado3 and self.lado3 < self.lado1 + self.lado2

    def perimetro(self) :
            return self.lado1 + self.lado2 + self.lado3
    
    def area (self) :
         sp = self.perimetro() /2
         return sqrt(sp*(sp-self.lado1)*(sp-self.lado2)*(sp-self.lado3))
    
    def tipoTriangulo(self) :
         if self.lado1 == self.lado2 == self.lado3 :
              return "Equilátero"
         if self.lado1 != self.lado2 and self.lado2 != self.lado3 and self.lado1 != self.lado3:
              return "Escaleno"
         return "Isósceles" 
tr1 = Triangulo (4,3,3)

print(tr1.isTriangulo())
print(tr1.perimetro())
print(tr1.area())
print(tr1.tipoTriangulo())