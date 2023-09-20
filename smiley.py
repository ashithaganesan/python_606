import turtle

win = turtle.Screen()
win.title("smiley")
win.bgcolor("light blue")
turta= turtle.Turtle()
turta.pensize(4)
turta.pencolor('black')
turta.speed(1)


#x=int(input("Enter x coordinate : "))
#y=int(input("Enter y coordinate : "))
#rad=int(input("Enter the radius of the circle : " ))
#color=input("Enter the color of the cirlce : ")

def draw_circle(x,y,rad,color):

    turta.up()
    turta.goto(x,y)
    turta.begin_fill()
    turta.fillcolor(color)
    turta.circle(rad)
    turta.end_fill() 
    #turta.left(90)
    #turta.forward(rad)
    turta.up()
    

def eye():
    draw_circle(0,0,100,"white")
    draw_circle(0,50,50,"brown")
    draw_circle(0,75,25,"black")

main()
turtle.done()
win.exitonclick()


    
