import numpy as np
import math
import turtle

def area_circulo(raio):
    return np.pi*(raio**2)
def p_circulo(raio):
    return 2*np.pi*raio
def d_circulo(raio):
    q = turtle.Turtle()
    q.color("blue")
    q.pensize(5)
    q.circle(raio*10)
    turtle.done()

def area_retangulo(base, altura):
    return base*altura
def p_retangulo(n1,n2):
    return (n1*2)+(n2*2)
def d_retangulo(base, altura):
    q = turtle.Turtle()
    q.color("blue")
    q.pensize(5)
    for _ in range(2):
        q.left(90)
        q.forward(base*10)
        q.left(90)
        q.forward(altura*10)
    turtle.done()

def area_triangulo(n1, n2, n3):
    sp=(n1+n2+n3) / 2
    return np.sqrt(sp * (sp - n1) * (sp - n2) * (sp - n3))
def p_triangulo(n1, n2, n3):
    return n1 + n2 + n3
def d_trianguloe(lado):
    q = turtle.Turtle()
    q.color("blue")
    q.pensize(5)
    for _ in range(3):
        q.forward(lado*10)
        q.left(120)
    turtle.done()
def d_trianguloi(lado_igual, lado_base):
    cos_vertice = (2 * lado_igual**2 - lado_base**2) / (2 * lado_igual**2)
    cos_vertice = max(-1, min(1, cos_vertice))
    angulo_vertice_rad = math.acos(cos_vertice)
    angulo_vertice_graus = math.degrees(angulo_vertice_rad)
    angulo_base_graus = (180 - angulo_vertice_graus) / 2

    q = turtle.Turtle()
    q.color("blue")
    q.pensize(5)
    q.forward(lado_base*10)
    q.left(180 - angulo_base_graus)
    q.forward(lado_igual*10)
    q.left(180 - angulo_vertice_graus)
    q.forward(lado_igual*10)
    turtle.done()
def d_trianguloes(lado1, lado2, lado3):
    if lado1 + lado2 <= lado3 or lado1 + lado3 <= lado2 or lado2 + lado3 <= lado1:
        print("Erro: Os lados fornecidos não formam um triângulo válido!")
        return
    cos_angulo_entre_lado1_lado2 = (lado1**2 + lado2**2 - lado3**2) / (2 * lado1 * lado2)
    cos_angulo_entre_lado1_lado2 = max(-1, min(1, cos_angulo_entre_lado1_lado2))
    angulo_entre_lado1_lado2 = math.degrees(math.acos(cos_angulo_entre_lado1_lado2))
    cos_angulo_entre_lado2_lado3 = (lado2**2 + lado3**2 - lado1**2) / (2 * lado2 * lado3)
    cos_angulo_entre_lado2_lado3 = max(-1, min(1, cos_angulo_entre_lado2_lado3))
    angulo_entre_lado2_lado3 = math.degrees(math.acos(cos_angulo_entre_lado2_lado3))

    q = turtle.Turtle()
    q.color("blue")
    q.pensize(5)
    q.forward(lado1 * 10)
    q.left(180 - angulo_entre_lado1_lado2)
    q.forward(lado2 * 10)
    q.left(180 - angulo_entre_lado2_lado3)
    q.forward(lado3 * 10)
    turtle.done()

def area_quadrado(lado):
    return lado*lado
def p_quadrado(lado):
    return lado*4
def d_quadrado(lado):
    q = turtle.Turtle()
    q.color("blue")
    q.pensize(5)
    for _ in range(4):
        q.left(90)
        q.forward(lado*10)
    turtle.done()
    

def creditos():
    print("Programa criado em Python por David Jesus 12ºCTC")