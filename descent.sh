#!/bin/bash

# The while loop represents the game.
# Each iteration represents a turn of the game
# where you are given inputs (the heights of the mountains)
# and where you have to print an output (the index of the moutain to fire on)
# The inputs you are given are automatically updated according to your last actions.


# game loop
while true; do
    max=0
    tar=0
    for (( i=0; i<8; i++ )); do
        # mountainH: represents the height of one mountain.
        read mountainH
        if (( $mountainH > $max )); then
            max=$mountainH
            tar=$i
        fi
    done
    
    echo $tar
    # Write an action using echo
    # To debug: echo "Debug messages..." >&2
    # The index of the mountain to fire on.
done
