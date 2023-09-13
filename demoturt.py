#Step 1: import turtle
import turtle 

#Step 2: Create a turtle control
win=turtle.Screen()           #create a graphics window
win.title("My screen")        #giving the title as my first window
win.bgcolor("light blue")     #assign light blue to window
#win.exitonclick()

#Step 3: my window is ready and i need to create a turtle to control 
turta=turtle.Turtle()
turta.color("red")
turta.pensize(4)
turta.pencolor("green")
turta.speed(1)
turta.forward(200)              #turta.fd(200)
turta.right(90)

turta.forward(70)
turta.right(90)
turta.forward(200)
turta.right(90)
turta.forward(70)
turta.penup()
 

turta.goto(10,100)

turta.pendown()
turta.forward(70)

turta.circle(30)
turta.dot(50)
turta.begin_fill()
turtle.done()