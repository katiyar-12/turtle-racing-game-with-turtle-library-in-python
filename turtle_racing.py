from turtle import Turtle , Screen
from  random import randint , choice

race = False
one = Turtle()
two = Turtle()
three = Turtle()
four = Turtle()
five  = Turtle()
six = Turtle()


turtles = [one,two ,three,four,five,six]
for turtle in turtles :
    turtle.shape("turtle")
    turtle.penup()

rainbow_colors = ["red", "orange", "yellow", "green", "blue", "violet"]


i = 0
for color in rainbow_colors :
    turtles[i].color(color)
    i += 1

screen  = Screen()
screen.setup(width=500,height=400)
user_bet = screen.textinput(title="Make your bet ",prompt="Which turtle do you want to win the race ? (enter your color )").lower()

# making our turtle go staring position
one.goto(x=-230,y=0)
two.goto(x=-230,y= -50)

three.goto(x=-230,y=50)
four.goto(x=-230,y=100)
five.goto(x=-230,y=-100)
six.goto(x=-230,y=-150)


def move_turtles(turtle_object) :
    random_no = randint(1,10)
    turtle_object.forward(random_no)

if user_bet :
    race = True



while race:
    for el in turtles :
        if el.xcor() > 230 :
            winning_color = el.color()[0]
            print(f"{winning_color} turtle won the race ")
            if user_bet == winning_color :
                print("You Win")
            else :
                print("You loose")
            race = False

        move_turtles(el)





screen.exitonclick()
