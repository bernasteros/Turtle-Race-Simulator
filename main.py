from turtle import Screen, Turtle
from random import choice
from random import randint


def random_hexer():
    """Returns a random color based on the hex-code"""

    hexcolor = "#"
    hexlist = list("0 1 2 3 4 5 6 7 8 9 a b c d e f".split(" "))

    for char in range(6):
        hexcolor += choice(hexlist)

    return hexcolor


def racer_number(display):
    """Asks the user for a number of players that should attend (2-10).
    Returns a Number between 2 and 10."""
    enroll = True

    while enroll:
        try:
            racers = int(display.numinput(title="Racing Menu",prompt="How many racers should attend?"))

            if 2 <= racers <= 10:
                return racers
            else:
                print("Sorry, but you need a number between 2 and 10")
        except TypeError:
            print("Sorry, but you need a number between 2 and 10")


def turtle_racers(number_of_racers):
    """Creates Turtle-Racers as wished"""
    racer_list = []

    for i in range(number_of_racers):
        new_racer = Turtle()
        new_racer.hideturtle()
        new_racer.shape("turtle")
        new_racer.color(random_hexer())
        new_racer.penup()
        new_racer.sety(-100+i*50)
        new_racer.setx(-200)
        new_racer.showturtle()
        racer_list.append(new_racer)

    return racer_list


def strecke(participants, turf):
    """Creates two side lines and the goal for the Racers"""
    track_building = True
    first_player = participants[0].pos()
    last_player = participants[-1].pos()

    while track_building:
        try:
            track_length = int(turf.numinput(title="Track Building", prompt="How long is the line?"))

            if 100 <= track_length <= 500:
                upper = Turtle()
                upper.hideturtle()
                upper.penup()
                upper.setx(-220)
                upper.pendown()
                upper.sety(last_player[1] + 30)
                upper.forward(track_length)

                lower = Turtle()
                lower.hideturtle()
                lower.penup()
                lower.setx(-220)
                lower.pendown()
                lower.sety(first_player[1] - 30)
                lower.forward(track_length)

                goal = Turtle()
                goal.hideturtle()
                goal.penup()
                goal.setx(track_length - 220)
                goal.sety(last_player[1] + 30)
                goal.pensize(10)
                goal.setheading(270)
                i = 0
                while i <= last_player[1] - first_player[1] + 60:
                    goal.pendown()
                    goal.forward(10)
                    goal.penup()
                    goal.forward(20)
                    i += 30
                return track_length - 220

            else:
                print("Sorry, but you need a number between 100 and 500")
        except TypeError:
            print("Sorry, but you need a number between 100 and 500")


screen = Screen()
screen.setup(800, 500)

racers = racer_number(screen)
turtles = turtle_racers(racers)
race_length = strecke(turtles, screen)

# TODO Make a bet on the winning turtle.
# TODO Random steps between 5 and 10
# TODO First Turtle reaches x = track length == GameOver, we have a winner.

screen.exitonclick()