from random import *
import time
import os

#sistema de apresentação de opções 

os.system('cls')
print("-----------------JOKENPO!-----------------")
jokenpo = ["Pedra", "Papel", "Tesoura"]
cont = 0
escolha = ""

for x in jokenpo:
    print("[",cont, "] - ", x)
    cont += 1
    
#Tomada de decisões
    
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

#Resultado

match adv: 
    case 0: #Pedra
        match jogada:
            case 0:
                print("Empate")
            case 1:
                print("Jogador venceu")
            case _:    
                print("Computador venceu")
        
    case 1: #Papel
        match jogada:
            case 0:
                print("Computador venceu")
            case 1:
                print("Empate")
            case _:    
                print("Jogador venceu")
    
    case _: #Tesoura
        match jogada:
            case 0:
                print("Jogador venceu")
            case 1:
                print("Computador venceu")
            case _:    
                print("Empate")
    
