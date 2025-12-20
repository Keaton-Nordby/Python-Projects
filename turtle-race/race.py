import turtle
import time

WIDTH, HEIGHT = 500, 500


def get_number_of_racers():
    racers = 0
    while True: 
        racers = input("How many turtles do you want to race (2-10): ")
        if racers.isdigit():
            racers = int(racers)
        else:
            print("Input is not numeric... Try Again!")
            continue

        if 2 <= racers <= 10:
            return racers
        else:
            print("Number of racers must be between (2-10)... Try Again!")

def init_turtle():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title('Turtle Racing Game')


racers = get_number_of_racers()
init_turtle()

racer = turtle.Turtle()
racer.speed(1)
racer.shape('turtle')
racer.forward(100)
racer.left(90)
racer.forward(100)
racer.right(90)
racer.backward(100)
time.sleep(10)


