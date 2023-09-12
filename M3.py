from random import randint
import time
from turtle import *

import numpy as np

PALETTE = {
    "light_blue": "#DBE6E6",
    "medium_blue": "#75AFBF",
    "dark_blue": "#023A80",
    "teal": "#ACCDCC",
    "purple": "#B377AB",
    "dusty_pink": "#EDB394",
    "green": "#1D7D76",
    "taupe": "#F6BF55",
    "orange": "#D27E20",
    "yellow": "#DF9D39"
}

SIZES = {"small": (1,1),
         "medium": (2,1),
         "large": (3,1.5)
        }

class Painter:
    def __init__(self, transition_matrix, size_matrix):
        self.transition_matrix = transition_matrix
        self.size_matrix = size_matrix
        self.colors = list(transition_matrix.keys())
        self.sizes = list(size_matrix.keys())

    def get_next_color(self, current_color):
        return np.random.choice(
            self.colors,
            p=[self.transition_matrix[current_color][next_color] for next_color in self.colors]
        )
    
    def get_next_size(self, current_size):
        return np.random.choice(
            self.sizes,
            p=[self.size_matrix[current_size][next_size] for next_size in self.sizes]
        )

def main():
    painter = Painter(transition_matrix={
        "light_blue": {"light_blue": 0.05, "medium_blue": 0.2, "dark_blue": 0.3, "teal": 0.05, "purple": 0.1, "dusty_pink": 0.025, "green": 0.1, "taupe": 0.025, "orange": 0.05, "yellow": 0.1},
        "medium_blue":  {"light_blue": 0.2, "medium_blue": 0.1, "dark_blue": 0.025, "teal": 0.3, "purple": 0.05, "dusty_pink": 0.05, "green": 0.05, "taupe": 0.1, "orange": 0.1, "yellow": 0.025},
        "dark_blue":  {"light_blue": 0.05, "medium_blue":  0.1, "dark_blue": 0.025, "teal": 0.05, "purple":  0.1, "dusty_pink": 0.025, "green": 0.05, "taupe": 0.2, "orange": 0.1, "yellow": 0.3},
        "teal": {"light_blue": 0.1, "medium_blue": 0.05, "dark_blue": 0.025, "teal": 0.05, "purple": 0.3, "dusty_pink": 0.025, "green": 0.1, "taupe": 0.2, "orange": 0.1, "yellow": 0.05},
        "purple":  {"light_blue": 0.1, "medium_blue":  0.2, "dark_blue": 0.1, "teal": 0.025, "purple": 0.1, "dusty_pink": 0.3, "green": 0.05, "taupe": 0.025, "orange": 0.05, "yellow": 0.05},
        "dusty_pink":  {"light_blue": 0.025, "medium_blue": 0.05, "dark_blue": 0.025, "teal": 0.2, "purple": 0.05, "dusty_pink": 0.05, "green": 0.3, "taupe": 0.1, "orange": 0.1, "yellow": 0.1}, 
        "green": {"light_blue": 0.3, "medium_blue": 0.1, "dark_blue": 0.05, "teal": 0.1, "purple": 0.05, "dusty_pink": 0.1, "green": 0.025, "taupe": 0.2, "orange": 0.025, "yellow": 0.05},
        "taupe": {"light_blue": 0.025, "medium_blue": 0.2, "dark_blue": 0.05, "teal": 0.025, "purple": 0.05, "dusty_pink": 0.05, "green": 0.3, "taupe": 0.1, "orange": 0.1, "yellow": 0.1},
        "orange":  {"light_blue": 0.1, "medium_blue": 0.2, "dark_blue": 0.025, "teal": 0.3, "purple": 0.1, "dusty_pink": 0.05, "green": 0.1, "taupe": 0.05, "orange": 0.05, "yellow": 0.025},
        "yellow":  {"light_blue": 0.025, "medium_blue": 0.05, "dark_blue": 0.3, "teal": 0.1, "purple": 0.05, "dusty_pink": 0.2, "green": 0.025, "taupe": 0.1, "orange":  0.05, "yellow": 0.1},
    }, size_matrix={
        "small": {"small": 0.3, "medium": 0.1, "large": 0.6},
        "medium":  {"small": 0.6, "medium": 0.3, "large": 0.1},
        "large":  {"small": 0.3, "medium": 0.6, "large": 0.1}
    })
    
    current_color="taupe"
    current_size="small"
    for x in range (0,100):
        pos = (randint(-150,150), randint(-150,150))
        direction = 0
        size = painter.get_next_size(current_size)
        current_size = size
        for y in range(0, 9):
            turtle = Turtle()
            turtle.speed(0)
            turtle.penup()
            color = painter.get_next_color(current_color)
            current_color = color
            if size == "small":
                turtle.shapesize(0.5,0.5)
            elif size == "medium":
                turtle.shapesize(1,1)
            else: 
                turtle.shapesize(1.5, 1)
            turtle.color(PALETTE[color])
            # turtle.setheading(turtle.towards(0, 0))
            turtle.setpos(pos)
            direction += 40
            turtle.left(direction)
            turtle.fd(10)
            turtle.pendown()
            turtle.shape("circle")
            turtle.penup()
            pos = turtle.pos()
    time.sleep(15)

if __name__ == "__main__":
    main()