from sympy.parsing.sympy_parser import parse_expr
from sympy import Symbol
import numpy as np

class Biseccion:
    def __init__(self):
        self.iterador = 0
        self.acumulador = 0
        self.izquierda = 0
        self.derecha = 0
        self.tolerancia = 0
        self.error = 0
        self.test = 0
        self.xi = 0
        self.function = None
        self.xi_anterior = 0
    
    def recibir_datos(self):
        print("METODO DE BISECCION")
        self.definir_funcion(input("introduce tu funcion ejemplos:\n x²->x**2\n xcos²(x)->xcos(x)**2: "))
        self.izquierda = float(input("Introduce el intervalo izquierdo: "))
        self.derecha = float(input("Introduce el intervalo derecho: "))
        self.tolerancia = float(input("introduce la tolerancia: "))
    
    def calculo(self):
        for i in np.arange(self.izquierda, self.derecha,.05):
            print("X = {0} f(x) = {1}".format(i,self.funcion(i)))
        for i in np.arange(self.izquierda,self.derecha-0.1,0.1):
            if self.funcion(i)*self.funcion(i+0.1) < 0:
                self.acumulador = self.acumulador + 1
            else:
                if self.funcion(i)*self.funcion(i+0.1) > 0:
                    self.acumulador = self.acumulador
                else:
                    self.error = 0
        if self.acumulador != 1:
            print("No hay raiz en este intervalo o existe mas de una raiz o existe una asintota")
        else:
            self.iteracion()
            while(self.error > self.tolerancia):
                self.iteracion()

    def definir_funcion(self,funcion_string):
        x = Symbol('x')
        valido = False
        while(valido == False):
            try:
                self.function = parse_expr(funcion_string)
                valido = True
            except:
                print("error en tu funcion")

    def funcion(self, val):
        x = Symbol('x')
        return self.function.subs(x,val)

    def iteracion(self):
        self.iterador = self.iterador + 1
        self.xi_anterior = self.xi
        self.xi = ((self.izquierda + self.derecha)/2)
        if self.funcion(self.derecha) < self.funcion(self.izquierda):
            self.test = self.funcion(self.xi)
            if self.test < 0:
                self.derecha = self.xi
            else:
                if self.test > 0:
                    self.izquierda = self.xi
        else:
            if self.funcion(self.izquierda) > self.funcion(self.derecha):
                self.test = self.funcion(self.xi)
                if self.test < 0:
                    self.derecha = self.xi
                else:
                    if self.test > 0:
                        self.izquierda = self.xi
                    else:
                        self.error = 0
            else:
                print("No hay raiz en este intervalo")        
        print("Iteracion: {0}  Raiz: {1}  Error: {2}".format(self.iterador,self.xi,self.error))

if __name__ == "__main__":
    biseccion = Biseccion()
    biseccion.recibir_datos()
    biseccion.calculo()