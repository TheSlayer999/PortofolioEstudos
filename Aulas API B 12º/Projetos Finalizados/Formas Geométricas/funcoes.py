import numpy as np

def area_circulo(raio):
    return np.pi*(raio**2)
def p_circulo(raio):
    return 2*np.pi*raio

def area_retangulo(base, altura):
    return base*altura
def p_retangulo(n1,n2):
    return (n1*2)+(n2*2)

def area_triangulo(n1, n2, n3):
    sp=(n1+n2+n3) / 2
    return np.sqrt(sp * (sp - n1) * (sp - n2) * (sp - n3))
def p_triangulo(n1, n2, n3):
    return n1 + n2 + n3


""" def area_triangulo(base, altura):
    return (base*altura)/2
def p_triangulo_equilatero(n):
    return n*3
def p_triangulo_isosceles(igual,diferente):
    return (igual*2)+diferente
def p_triangulo_escaleno(n1,n2,n3):
    return n1+n2+n3 """

def area_quadrado(lado):
    return lado*lado
def p_quadrado(lado):
    return lado*4

def creditos():
    print("Programa criado em Python por David Jesus 12ºCTC")