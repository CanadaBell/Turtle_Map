import turtle
import random
st_x = random.randrange(-400,400,5)
st_y = random.randrange(-400,400,5)
end_x = random.randrange(-400,400,5)
end_y = random.randrange(-400,400,5)
file = open("cords.txt", "w")
file.write(f"up\n{st_x}\t{st_y}\n{end_x}\t{end_y}\ndown")
file.close()

w = turtle.Screen()
uber = turtle.Turtle()
s = turtle.Turtle()
s.hideturtle()
uber.shape("circle")
uber.pencolor("white")
uber.hideturtle()
s.speed(0)
w.setup(800, 800)
w.screensize(400, 400)
s.pencolor("#3B9EBF")
s.pensize(10)
inst = open("cords.txt", "r")
inst = inst.readlines()
inst = ("".join(inst)).split()
eval("s." + inst[0] + "()")
s.goto(int(inst[1]), int(inst[2]))
eval("s." + inst[5] + "()")
s.dot(30, "#3B9EBF")
x_path = int(inst[3]) - int(inst[1])
y_path = int(inst[4]) - int(inst[2])
s.fd(x_path)
s.lt(90)
s.fd(y_path)
s.dot(30, "#3B9EBF")
uber.pensize(5)
eval("uber." + inst[0] + "()")
uber.goto(int(inst[1]), int(inst[2]))
eval("uber." + inst[5] + "()")
uber.dot(15, "white")
uber.fd(x_path)
uber.lt(90)
uber.fd(y_path)
uber.dot(15, "white")
w.exitonclick()
