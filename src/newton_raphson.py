from sympy import Symbol, diff
from sympy.parsing.sympy_parser import parse_expr
import numpy as np
class Newton_raphson:
    def __init__(self):
        self.izquierda = 0
        self.derecha = 0
        self.aproximacion = 0
        self.funcion = None
        self.i = 0
        self.res = 0
        self.p0 = 0
        self.p1 = 0
        self.p2 = 0
        self.g = 0
        self.tolerancia = 0
        self.x = 0
        self.error = 0

    def recibir_datos(self):
        print("METODO DE NEWTON-RAPHSON \n")
        self.definir_funcion(input("Introduce tu funcion de una variable 'x': "))
        self.izquierda = float(input("introduce el intervalo izquierdo: "))
        self.derecha = float(input("introduce el intervalo derecho: "))


    def calculo_intervalo(self):
        self.i = self.izquierda
        self.res = self.evaluar_funcion(self.i)
        while (self.i <= self.derecha):
            self.res = self.evaluar_funcion(self.i)
            print("x: {0}\t f(x)={1}".format(self.i,self.res))
            self.i = self.i + 1
        opcion = ''
        while opcion != 'S' or opcion != 'N':
            opcion = str.upper(input("Selecciona la opcion\n S) Si el intervalo funciona\nN)Si el intervalo no sirve\n_"))
            if opcion == 'S':
                return True
            elif opcion == 'N':
                return False
    def calculo(self):
        if self.calculo_intervalo() == True:
            try:
                self.aproximacion = float(input("introduce una primera aproximacion: "))
            except:
                print("")
            self.p0 = self.evaluar_funcion(self.aproximacion)
            self.p1 = self.funcion_derivar(self.aproximacion,1)
            self.p2 = self.funcion_derivar(self.aproximacion,2)
            print("{0} {1} {2}".format(self.p0,self.p1,self.p2))
            self.g = abs((self.p0*self.p2)/(self.p1*self.p1))
            if self.g < 1:
                self.tolerancia = float(input("La funcion si converge - Ingresa la tolerancia: "))
                self.i = 0
                while self.error >= self.tolerancia:
                    self.iteracion()
                print("Tu raiz es: {0}\t con un error de {1}",self.x,self.error)
            else:
                print("La funcion no converge en ese valor, elige otro")
                input()
                self.calculo()


    def iteracion(self):
        self.x =self.aproximacion - self.evaluar_funcion(self.aproximacion)/self.funcion_derivar(self.aproximacion,1)
        self.error = abs(self.x - self.aproximacion)
        self.aproximacion = self.x
        self.i = self.i+1
        print("Iteracion numero {0}\tAproximacion {1}\t Error absoluto {2}".format(self.i,self.x,self.error))

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

    def funcion_derivar(self,val,orden):
        x = Symbol('x')
        funcion_diff = diff(self.funcion,x,orden)
        return funcion_diff.subs(x,val)

if __name__ == "__main__":
    newton_raphson = Newton_raphson()
    newton_raphson.recibir_datos()
    newton_raphson.calculo()