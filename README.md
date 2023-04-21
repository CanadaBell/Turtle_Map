# Turtle "map"
This is a extra challenge for my comp sci class

## What the program does
1. Makes 2 pairs of random cords and writs to a txt file: (up, (x,y), (x,y), down)
2. Draws a dot on the 2 cords and makes a path between each cord, and again with a new turtle (different colour and different size)
3. asks the user to input a phone number a writes that plus the cord data to a new txt file

## How the program does that
1. using random, makes 2 set of cords (start and end) and writes that to a txt file along with up and down
2. reads the "up", first (x,y) and "down" from txt file
3. runs the "up" as in exce() (exce("s." + "up" + "()")), goes to first cords, runs the "down" the same way as "up"
4. repeats that for the second turtle
5. Takes a phone number (checks if it's a number) and writes that to a new txt file along with the info in step 1

## Changing the txt file
If you want to change the txt file manually, follow these steps
1. make sure the file is linked properly (name your txt file cords.txt or change the code)
2. Comment out / Delete lines 5 - 9
3. Make sure that the file is formatted properly (check desc of update for formatting)=
