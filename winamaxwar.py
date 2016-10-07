import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())  # the number of cards for player 1
cardArr1 = []
cardArr2 = []
for i in range(n):
    cardp_1 = input()  # the n cards of player 1
    cardArr1.append(cardp_1)
m = int(input())  # the number of cards for player 2
for i in range(m):
    cardp_2 = input()  # the m cards of player 2
    cardArr2.append(cardp_2)
# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

print ("of p1 " + str(n) + " " + str(cardArr1) + " for player 1" ,file=sys.stderr)
print ("of p2 " + str(m) + " " + str(cardArr2) + " for player 2" ,file=sys.stderr)

def card_val(card):
    if card[0] == 'J':
        return 11
    elif card[0] == 'Q':
        return 12
    elif card[0] == 'K':
        return 13
    elif card[0] == 'A':
        return 14
    elif card[0] == '1':
        return 10
    else:
        return int(card[0])
        
def cardComp(p1arr, p2arr):
    valp1 = card_val(p1arr[0])
    valp2 = card_val(p2arr[0])
    
    if valp1 == valp2:
        return "war"
    elif valp1 > valp2:
        return "1"
    else:
        return "2"

def war():
    global cardArr1
    global cardArr2
    global stack1
    global stack2
    global eqFirst
    global hadWar 
    hadWar = True
    if len(cardArr1) < 3 or len(cardArr2) < 3:
            eqFirst = True
            return
    for num in range(3):
        stack1.append(cardArr1[0])
        cardArr1 = cardArr1[1:]
    for num in range(3):
        stack2.append(cardArr2[0])
        cardArr2 = cardArr2[1:]

def fight():
    global cardArr1
    global cardArr2
    global stack1
    global stack2
    global stepCounter
    global hadWar
    p1card = cardArr1[0]
    p2card = cardArr2[0]
    stack1.append(p1card)
    stack2.append(p2card)
    cardArr1 = cardArr1[1:]
    cardArr2 = cardArr2[1:]
    print (str(stack1) + " " + str(stack2), file=sys.stderr)
    if cardComp(p1card, p2card) == "war":
        war()
    elif cardComp(p1card, p2card) == "1":
        if hadWar:
            hadWar = False
            cardArr1.extend(stack1)
            stack1.clear()
            cardArr1.extend(stack2)
            stack2.clear()
        else:
            cardArr1.append(stack1[-1])
            stack1.pop()
            cardArr1.append(stack2[-1])
            stack2.pop()
        stepCounter+=1
            
    elif cardComp(p1card, p2card) == "2":
        if hadWar:
            hadWar = False
            cardArr2.extend(stack1)
            stack1.clear()
            cardArr2.extend(stack2)
            stack2.clear()
        else:
            cardArr2.append(stack1[-1])
            stack1.pop()
            cardArr2.append(stack2[-1])
            stack2.pop()
        stepCounter+=1

stack1 = []
stack2 = []
stepCounter = 0
hadWar = False
eqFirst = False
# NOTE THAT LAST CARD IN THE STACK IS BY PLAYER 2

while len(cardArr1) > 0 and len(cardArr2) > 0 and not eqFirst:
    fight()
        
ans = ""
if eqFirst:
    ans = "PAT"
elif len(cardArr1) > 0:
    ans = "1 " + str(stepCounter)
elif len(cardArr2) > 0:
    ans = "2 " + str(stepCounter)

print(ans)
