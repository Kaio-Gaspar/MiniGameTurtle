from turtle import *
from tkinter import *
root = Tk()
t = Turtle()
t.speed(1)
while True:
    print('----- Bem-Vindo ao minigame "TURTLE", siga as orientações para joga-lo, considerena direção inicial seno referente a essa seta =>-----')
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
        t.forward(distancia)
    elif orientação == 'b':
        t.backward(distancia)
    else:
        print('[ERRO]reinicie o jogo e insira dados válidos')
        break

    continuar = input('Deseja continuar andando? sim(s) não(n):')
    if continuar == 'n':
        break
    else:
        continue

   
