from turtle import Screen, Turtle
from random import choice, randint


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
            chosen_racer_number = int(display.numinput(title="Racing Menu",
                                                       prompt="How many racers should attend?",
                                                       default=2))

            if 2 <= chosen_racer_number <= 10:
                return chosen_racer_number
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
        new_racer.sety(-100 + i * 50)
        new_racer.setx(-250)
        new_racer.number = i + 1
        new_racer.write(str(i + 1))
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
            track_length = int(turf.numinput(title="Track Building",
                                             prompt="How long is the line?",
                                             default=250))

            if 100 <= track_length <= 800:
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
                print("Sorry, but you need a number between 100 and 800")
        except TypeError:
            print("Sorry, but you need a number between 100 and 800")


def bet_the_winner(number_of_racers, display):
    """Manages the bet of the player, returns an int"""
    betting = True

    while betting:
        try:
            bet_racer_number = int(display.numinput(title="Betting Menu",
                                                    prompt="Who will win?",
                                                    default=randint(1, number_of_racers)))

            if 1 <= bet_racer_number <= number_of_racers:
                return bet_racer_number
            else:
                print("Sorry, but you need a number between 1 and " + str(number_of_racers))
        except TypeError:
            print("Sorry, but you need a number between 1 and " + str(number_of_racers))


def race(participants, track_length, number_bet):
    """The race itself, turtles run, and the winner will be decided"""
    race_in_progress = True

    while race_in_progress:
        for turtle in participants:
            move = randint(1, 10)
            turtle.forward(move)

            if int(turtle.pos()[0]) > int(track_length):
                print("Turtle " + str(turtle.number) + " won the race")
                if turtle.number == number_bet:
                    print("Congratulation, you bet on the right turtle!")
                else:
                    print("What a pity, you bet on the wrong turtle!")
                race_in_progress = False
                break


def reset_turtles(participants):
    """Resets the input list of objects"""
    for turtle in participants:
        turtle.reset()


screen = Screen()
screen.setup(800, 800)

racers = racer_number(screen)
turtles = turtle_racers(racers)
race_length = strecke(turtles, screen)
bet = bet_the_winner(racers, screen)

race(participants=turtles,
     track_length=race_length,
     number_bet=bet)

print("Thank you for playing!")
screen.exitonclick()
