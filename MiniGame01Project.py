from turtle import *
from tkinter import *
root = Tk()
t = Turtle()
t.speed(1)
def orientacao_front():
    distancia = int(input('Quantos pixels a percorrer? '))
    t.forward(distancia)
    return distancia

def orientacao_back():
    distancia = int(input('Quantos pixels a percorrer? '))
    t.backward(distancia)
    return distancia



while True:
    print('----- Bem-Vindo ao minigame "TURTLE", siga as orientações para joga-lo, considere  a direção inicial sendo referente a essa seta =>-----')
    orientação = input('Qual sentido você deseja movimentar a turtle: Direita(d), Esquerda(e), Para frente(f), Para atras(a): ')
    if orientação ==  'd' or orientação == 'e':
        graus = int(input(f'Quantos graus deseja girar no sentido {orientação}: '))
        distancia = int(input('Quantos pixels a percorrer? '))
    if orientação == 'd':
        t.right(graus)
        t.forward(distancia)
    elif orientação == "e":
        t.left(graus)
        t.forward(distancia)
    elif orientação == 'f':
        orientacao_front()
    elif orientação == 'a':
        orientacao_back()
    else:
        print('[ERRO]reinicie o jogo e insira dados válidos')
        break

    continuar = input('Deseja continuar andando? sim(s) não(n):')
    if continuar == 'n':
        break
    else:
        continue

   
