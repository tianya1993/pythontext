#!/usr/bin/env python
#-*-coding:utf8-*-
number = 59
number_chances = 3
print("you have only 3 chances to guess")
for  i  in range(1,number_chances+1):
    print("chance "+str(i))
    guess = int(input("Enter an  interger:"))
    if guess == number:
        print("Bingo! you guessed  it ringht")
        print("(but you do not win any prizes)")
        break


