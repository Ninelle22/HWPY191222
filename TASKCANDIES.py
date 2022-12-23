#Создайте программу для игры с конфетами человек против человека.

#Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход 
# друг после друга. Первый ход определяется жеребьёвкой. 
# За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять 
# первому игроку, чтобы забрать все конфеты у своего конкурента?

#a) Добавьте игру против бота

#b) Подумайте как наделить бота ""интеллектом""

from random import randint as r

def takecandy(name):
    taken_candy = int(input(f"{name} How many candies will you take from 1 to 28? "))
    while taken_candy < 1 or taken_candy > 28: 
        taken_candy = int(input(f"{name} How many candies will you take from 1 to 28? "))
    return taken_candy

player1 = input("1st player: ")
player2 = input("2nd player: ")   
candy = int(input("Сколько конфет на столе?"))
step = r(0, 2)
print(f"{player1 if step == 1 else player2} START GAME")

while candy > 28:
    taken = takecandy(player1)  if step == 1 else takecandy(player2)
    candy -= taken
    step += 1 if step < 1 else - 1
    print(f"{player2 if step == 1 else player1} взял {taken} конфет. осталось {candy}.")
print(f'Победил: {player1 if step == 1 else player2}, забрав {candy}')
