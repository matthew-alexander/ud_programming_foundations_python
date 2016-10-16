import turtle 



def draw_square(some_turtle): 
    for i in range(1,5):
        some_turtle.forward(100)
        some_turtle.right(90)

def draw_art():
    window = turtle.Screen()
    window.bgcolor("tan")

    brad = turtle.Turtle()  
    draw_square(brad)

    angie = turtle.Turtle()
    angie.shape("arrow")
    angie.color("blue")
    
    angie.circle(100)

    window.exitonclick()

draw_art()


