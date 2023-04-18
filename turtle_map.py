## Imports ##
import turtle
import random
## File ##
st_x, st_y = random.randrange(-300,300,5), random.randrange(-300,300,5) # get random cords for start pos
end_x, end_y = random.randrange(-300,300,5), random.randrange(-300,300,5) # get random cords for end pos
file = open("cords.txt", "w") 
file.write(f"up\n{st_x}\t{st_y}\n{end_x}\t{end_y}\ndown") # writes to a txt document: up, start pos, end pos, down
file.close()
## Turtles ##
w = turtle.Screen() # screen
uber = turtle.Turtle() # turtle
s = turtle.Turtle() # turtle
# Window Settings #
w.setup(800, 800); w.screensize(400, 400)
# "Uber" Settings #
uber.hideturtle()
uber.shape("circle")
uber.color("blue")
uber.pencolor("white")
uber.pensize(5)
# Drawer Settings #
s.hideturtle()
s.speed(0)
s.pencolor("#3B9EBF")
s.pensize(10)
# Drawing #
inst = open("cords.txt", "r")
inst = inst.readlines()
inst = (" ".join(inst)).split() # makes the txt file a list (takes txt file, turns it into a string then splits each word)
exec("s." + inst[0] + "()") # takes the up from the text file and runs it a turtle command
s.goto(int(inst[1]), int(inst[2])) # takes the first 2 numbers from the text file and makes the turtle go to that pos
exec("s." + inst[5] + "()")# takes the down from the text file and runs it a turtle command
s.dot(30, "#3B9EBF")# Draws a dot
x_path, y_path = int(inst[3]) - int(inst[1]), int(inst[4]) - int(inst[2]) #Takes the distance from the second set of cords - the first set of cords
s.fd(x_path) # Moves the turtle by distace (x)
s.lt(90)
s.fd(y_path) # Moves the turtle by distace (x)
s.dot(30, "#3B9EBF") # Draws second dot
eval("uber." + inst[0] + "()") 
uber.goto(int(inst[1]), int(inst[2])) #Goes to starting pos via same instructions as other turtle
eval("uber." + inst[5] + "()")
uber.showturtle()
uber.dot(15, "white") #Draws smaller dot
uber.fd(x_path) # Follows same path
uber.lt(90) # V
uber.fd(y_path) # V
uber.dot(15, "white") #Draws smaller dot
phone = turtle.textinput("Phone Number", "Please enter your phone number") #ask user to input a phone number
if phone == None: phone = "0"; phone = int(phone) if phone.isdigit() else "0" # Checks if the phone number is a number, if yes keep the same otherwise turns it to a zero 
w.exitonclick()
## File Again ##
recipt = open("recipt.txt", "w") # Opens file 
recipt.write(f"up\n{st_x}\t{st_y}\n{end_x}\t{end_y}\ndown\n{phone}") # Writes data from cords + phone number (inputs after drawing)
recipt.close() # Closes file 
