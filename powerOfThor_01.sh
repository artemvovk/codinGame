#!/bin/bash
# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
# ---
# Hint: You can use the debug stream to print initialTX and initialTY, if Thor seems not follow your orders.

# lightX: the X position of the light of power
# lightY: the Y position of the light of power
# initialTX: Thor's starting X position
# initialTY: Thor's starting Y position
read lightX lightY initialTX initialTY
let thorX=initialTX
let thorY=initialTY
# game loop
while true; do
    # remainingTurns: The remaining amount of turns Thor can move. Do not remove this line.
    read remainingTurns

    # Write an action using echo
    # To debug: echo "Debug messages..." >&2
    directionX=""
    directionY=""
    if [ $lightY -gt $thorY ]; then
        directionY="S"
        let thorY=thorY+1
    elif [ $lightY -lt $thorY ]; then
        directionY="N"
        let thorY=thorY-1
    fi
    if [ $lightX -gt $thorX ]; then
        directionX="E"
        let thorX=thorX+1
    elif [ $lightX -lt $thorX ]; then
        directionX="W"
        let thorX=thorX-1
    fi

    echo ${directionY}${directionX}
done
