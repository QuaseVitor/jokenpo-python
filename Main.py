from random import *
import time
import os

os.system('cls')
print("-----------------JOKENPO!-----------------")
jokenpo = ["Pedra", "Papel", "Tesoura"]
cont = 0
escolha = ""

for x in jokenpo:
    print("[",cont, "] - ", x)
    cont += 1
    
jogada = int(input("Insira sua jogada: "))
escolha = jokenpo[jogada]

adv = randint(0,2)
adv_escolha = jokenpo[adv]

print("JO")
time.sleep(1)
print("KEN")
time.sleep(1)
print("PO!")
time.sleep(1)

print("Jogador: ",escolha)
print("Computador: ",adv_escolha)
time.sleep(1)
if adv==0: #Pedra
    if jogada ==0:
        print("Empate")
    elif jogada==1:
        print("Jogador venceu")
    elif jogada==2:    
        print("Computador venceu")
        
elif adv == 1: #Papel
    if jogada ==0:
        print("Computador venceu")
    elif jogada==1:
        print("Empate")
    elif jogada==2:    
        print("Jogador venceu")
    
else: #Tesoura
    if jogada ==0:
        print("Jogador venceu")
    elif jogada==1:
        print("Computador venceu")
    elif jogada==2:    
        print("Empate")
    

