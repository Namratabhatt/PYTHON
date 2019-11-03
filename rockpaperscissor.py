# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 00:39:49 2019

@author: Tapas
"""
def rock_paper_scissor(num1,num2,bit1,bit2):
    p1=int(num1[bit1])%3
    p2=int(num2[bit2])%3
    if(player_one[p1]==player_two[p2]):
        print("Draw")
    elif(player_one[p1]=='rock' and player_two[p2]=='paper'):
        print("Player 2 wins")
    elif(player_one[p1]=='paper' and player_two[p2]=='rock'):
        print("Player 1 wins")
    elif(player_one[p1]=='rock' and player_two[p2]=='scissor'):
        print("Player 1 wins")
    elif(player_one[p1]=='scissor' and player_two[p2]=='rock'):
        print("Player 2 wins")
    elif(player_one[p1]=='scissor' and player_two[p2]=='paper'):
        print("Player 1 wins")
    elif(player_one[p1]=='paper' and player_two[p2]=='scissor'):
        print("Player 2 wins")

player_one={1:'rock',2:'paper',3:'scissor'}
player_two={1:'paper',2:'scissor',3:'rock'}
while(1):
    num1=input("Player 1 enter number")
    num2=input("Player 2 enter your number")
    bit1=int(input("p1,Enter secret position"))
    bit2=int(input("p2,Enter secret position"))
    rock_paper_scissor(num1,num2,bit1,bit2)
    ch=input("Do you want to continue")
    if(ch=='n'):
        break