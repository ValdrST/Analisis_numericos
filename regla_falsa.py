from sympy import Symbol
from sympy.parsing.sympy_parser import parse_expr
import numpy as np

class regla_falsa:
    def __init__(self):
        self.i = 0
        self.acucs = 0
        self.acuraiz = 0
        self.acut = 0
        self.tolerancia = 0
        self.inferior = 0
        self.superior = 0
        self.funcionA = 0
        self.funcionB = 0
        self.funcion = None
        self.x = 0
        self.xa= 0
        self.d = 100
        self.res = 0
    
    def recibir_datos(self):
        self.definir_funcion(input("introduce tu funcion ejemplos:\n x²->x**2\n xcos²(x)->xcos(x)**2: "))
        self.tolerancia = float(input("Escribe la tolerancia en decimales: "))
        self.inferior = float(input("introduce el extremo inferior: "))
        self.superior = float(input("introduce el extremo superior: "))

    def calcular_num_raices(self):
        self.acucs = 0
        self.acuraiz = 0
        for i in np.arange(self.inferior,self.superior,0.1):
            if self.evaluar_funcion(i)*self.evaluar_funcion(i + 0.1) < 0:
                self.acucs = self.acucs + 1
            else:
                if self.evaluar_funcion(i)*self.evaluar_funcion(i + 0.1) > 0:
                    self.acucs = self.acucs
                else:
                    self.acuraiz = self.acuraiz +1
        self.acut = self.acucs + self.acuraiz
        if self.acut != 1:
            print("Tu intervalo tiene mas de una raiz! Selecciona otra intervalo")
            return False
        return True

    def creciente_decreciente(self):
        if self.evaluar_funcion(self.inferior) < self.evaluar_funcion(self.superior):
            return True
        else:
            return False

    def calculo(self):
        for j in np.arange(self.inferior,self.superior,0.5):
            print("x={0}\tf(x)={1}".format(j,self.evaluar_funcion(j)))
        if self.creciente_decreciente == True:
            while self.d>=self.tolerancia:
                self.funcionA = self.evaluar_funcion(self.inferior)
                self.funcionB = self.evaluar_funcion(self.superior)
                self.x = self.inferior + ((self.funcionA*(self.superior-self.inferior))/(self.funcionA-self.funcionB))
                self.res = self.evaluar_funcion(self.x)
                if self.res < 0:
                    self.inferior = self.x
                else:
                    self.superior = self.x
                self.d = self.x - self.xa
                if self.d < 0:
                    self.d = self.d*-1
                print("Iteracion:{0}\tRaiz:{1}\tf(xi):{2}\ttolerancia(Eabs):{3}".format(self.i,self.x,self.evaluar_funcion(self.x),self.d))
                self.xa = self.x
                self.i = self.i + 1
        else:
            while self.d>=self.tolerancia:
                self.funcionA = self.evaluar_funcion(self.inferior)
                self.funcionB = self.evaluar_funcion(self.superior)
                self.x = self.inferior + ((self.funcionA*(self.superior-self.inferior))/(self.funcionA-self.funcionB))
                self.res = self.evaluar_funcion(self.x)
                if self.res < 0:
                    self.superior = self.x
                else:
                    self.inferior = self.x
                self.d = self.x - self.xa
                if self.d < 0:
                    self.d = self.d*-1
                print("Iteracion:{0}\tRaiz:{1}\tf(xi):{2}\ttolerancia(Eabs):{3}".format(self.i,self.x,self.evaluar_funcion(self.x),self.d))
                self.xa = self.x
                self.i = self.i + 1
        print("La raiz es {0}".format(self.x))


                
        

    def definir_funcion(self,funcion_string):
        x = Symbol('x')
        valido = False
        while(valido == False):
            try:
                self.funcion = parse_expr(funcion_string)
                valido = True
            except:
                print("error en tu funcion")
    
    def evaluar_funcion(self,val):
        x = Symbol('x')
        return self.funcion.subs(x,val)
    
if __name__ == "__main__":
    regla_falsa = regla_falsa()
    regla_falsa.recibir_datos()
    if regla_falsa.calcular_num_raices() == True:
        regla_falsa.calculo()
