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
    "light_purple": "#D3B2BB",
    "dusty_pink": "#EDD7D3",
    "green": "#729C77",
    "taupe": "#F0DABD",
    "orange": "#DC8825",
    "yellow": "#EEB34D",
    "dark_green": "#22636F",
    "light_green": "#C1C292",
    "dark_orange": "#DB6322"
}

TREES = {

}
    
SKY = {

}
    
ORANGE_BUSH = {

}
    
GREEN_BUSH = {

}

GROUND = {

}
    
OCEAN = {

}
    


class Painter:
    def __init__(self, size_matrix, object_matrix, object_color_matrix):
       
        self.size_matrix = size_matrix
        self.object_matrix = object_matrix
        self.object_color_matrix = object_color_matrix
        self.object_colors = list(object_color_matrix.keys())
        self.sizes = list(size_matrix.keys())
        self.objects = list(object_matrix.keys())

    def get_next_object(self, current_object):
        return np.random.choice(
            self.objects,
            p=[self.object_matrix[current_object][next_object] for next_object in self.objects]
        )

    def get_next_color(self, current_color, current_object):
        matrix = self.object_color_matrix[current_object]
        keys = list(matrix.keys())
        return np.random.choice(
            keys,
            p=[matrix[current_color][next_color] for next_color in matrix]
        )
    
    def get_next_size(self, current_size):
        return np.random.choice(
            self.sizes,
            p=[self.size_matrix[current_size][next_size] for next_size in self.sizes]
        )

def main():
    # Initialize our painter 
    painter = Painter(
    size_matrix={
        "small": {"small": 0.3, "medium": 0.1, "large": 0.6},
        "medium":  {"small": 0.6, "medium": 0.3, "large": 0.1},
        "large":  {"small": 0.3, "medium": 0.6, "large": 0.1}
    },object_matrix={
        "tree": {"tree": 0.2, "sky": 0.2, "orange_bush": 0.1, "green_bush": 0.05, "ground": 0.05, "ocean": 0.3, "yellow_bush": 0.1},
        "sky": {"tree": 0.05, "sky": 0.3, "orange_bush": 0.05, "green_bush": 0.1, "ground": 0.3, "ocean": 0.1, "yellow_bush": 0.1},
        "orange_bush": {"tree": 0.05, "sky": 0.3, "orange_bush": 0.1, "green_bush": 0.05, "ground": 0.2, "ocean": 0.1, "yellow_bush": 0.2},
        "green_bush": {"tree": 0.05, "sky": 0.3, "orange_bush": 0.05, "green_bush": 0.05, "ground": 0.3, "ocean": 0.2, "yellow_bush": 0.05},
        "yellow_bush": {"tree": 0.05, "sky": 0.2, "orange_bush": 0.05, "green_bush": 0.1, "ground": 0.3, "ocean": 0.2, "yellow_bush": 0.1},
        "ground": {"tree": 0.3, "sky": 0.2, "orange_bush": 0.1, "green_bush": 0.05, "ground": 0.05, "ocean": 0.1, "yellow_bush": 0.2},
        "ocean": {"tree": 0.05, "sky": 0.3, "orange_bush": 0.05, "green_bush": 0.2, "ground": 0.05, "ocean": 0.3, "yellow_bush": 0.05}        
    },object_color_matrix={
    "tree": {
        "green": {"green": 0.2, "yellow": 0.2, "teal": 0.1, "light_green": 0.5},
        "yellow": {"green": 0.1, "yellow": 0.2, "teal": 0.5, "light_green": 0.2},
        "teal": {"green": 0.5, "yellow": 0.2, "teal": 0.2, "light_green": 0.1},
        "light_green": {"green": 0.5, "yellow": 0.1, "teal": 0.2, "light_green": 0.2},
        },
    "sky": {
        "light_blue": {"light_blue": 0.5, "medium_blue": 0.2, "dusty_pink": 0.1, "light_purple": 0.2},
        "medium_blue": {"light_blue": 0.1, "medium_blue": 0.2, "dusty_pink": 0.5, "light_purple": 0.2},
        "dusty_pink": {"light_blue": 0.5, "medium_blue": 0.2, "dusty_pink": 0.2, "light_purple": 0.1},
        "light_purple": {"light_blue": 0.5, "medium_blue": 0.1, "dusty_pink": 0.2, "light_purple": 0.2}
        },
    "orange_bush": {
        "orange": {"orange": 0.5, "yellow": 0.2, "purple": 0.1, "dark_orange": 0.2},
        "yellow": {"orange": 0.1, "yellow": 0.2, "purple": 0.5, "dark_orange": 0.2},
        "purple": {"orange": 0.5, "yellow": 0.2, "purple": 0.2, "dark_orange": 0.1},
        "dark_orange": {"orange": 0.5, "yellow": 0.1, "purple": 0.2, "dark_orange": 0.2},
        },
    "green_bush": {
        "green": {"green": 0.2, "dark_green": 0.1, "teal": 0.5, "light_green": 0.2},
        "dark_green": {"green": 0.1, "dark_green": 0.2, "teal": 0.2, "light_green": 0.5},
        "teal": {"green": 0.5, "dark_green": 0.2, "teal": 0.2, "light_green": 0.1},
        "light_green": {"green": 0.2, "dark_green": 0.1, "teal": 0.5, "light_green": 0.2},
        },
    "yellow_bush": {
        "green": {"green": 0.2, "yellow": 0.1, "orange": 0.5, "light_green": 0.2},
        "yellow": {"green": 0.1, "yellow": 0.2, "orange": 0.2, "light_green": 0.5},
        "orange": {"green": 0.5, "yellow": 0.2, "orange": 0.2, "light_green": 0.1},
        "light_green": {"green": 0.2, "yellow": 0.1, "orange": 0.5, "light_green": 0.2},
        },
    "ground": {
        "dark_blue": {"dark_blue": 0.5, "purple": 0.2, "medium_blue": 0.1, "dark_green": 0.2},
        "purple": {"dark_blue": 0.1, "purple": 0.2, "medium_blue": 0.5, "dark_green": 0.2},
        "medium_blue": {"dark_blue": 0.5, "purple": 0.2, "medium_blue": 0.2, "dark_green": 0.1},
        "dark_green": {"dark_blue": 0.5, "purple": 0.1, "medium_blue": 0.2, "dark_green": 0.2},
        },
    "ocean": {
        "teal": {"teal": 0.5, "light_blue": 0.2, "medium_blue": 0.1, "dark_green": 0.2},
        "light_blue": {"teal": 0.1, "light_blue": 0.2, "medium_blue": 0.5, "dark_green": 0.2},
        "medium_blue": {"teal": 0.5, "light_blue": 0.2, "medium_blue": 0.2, "dark_green": 0.1},
        "dark_green": {"teal": 0.5, "light_blue": 0.1, "medium_blue": 0.2, "dark_green": 0.2},
        }
})
    
    # Start with paint color taupe and paintbrush size small 
    current_color="taupe"
    current_size="small"
    current_object="sky"

    # For 100 Flowers
    for _ in range (0,500):
        # Pick a paintbrush size
        size = painter.get_next_size(current_size)
        current_size = size

        # Pick type of object (tree, bush, ocean, ...)
        object = painter.get_next_object(current_object)
        current_object = object
        current_color = list(painter.object_color_matrix[current_object].keys())[0]

        # Choose a random position on the canvas
        if current_object == "sky": 
            pos = (randint(-100,150), randint(50,150)) 
        elif current_object == "ocean": 
            pos = (randint(-150,150), randint(-50,50)) 
        elif current_object == "tree": 
            pos = (randint(-150,-50), randint(-50,150)) 
        elif current_object == "ground": 
            pos = (randint(-150,150), randint(-150,-50))
        elif current_object == "orange_bush": 
            pos = (randint(-150,150), randint(-100,-50))  
        elif current_object == "green_bush": 
            pos = (randint(-150,150), randint(-150,-50))  
        elif current_object == "yellow_bush": 
            pos = (randint(-150,0), randint(-150,0))  
        direction = 0
        
        # For 9 paintstrokes
        for _ in range(0, 10):
            # Initialize the turtle 
            turtle = Turtle()
            turtle.penup()
            turtle.speed(0)
            turtle.setpos(pos)
            direction += 40
            turtle.left(direction)
            turtle.fd(8)

            # Choose a new paint color
            color = painter.get_next_color(current_color, current_object)
            current_color = color
            turtle.color(PALETTE[color])

            # Change the paintbrush size to what was selected before
            if size == "small":
                turtle.shapesize(0.5,0.25)
            elif size == "medium":
                turtle.shapesize(0.5,0.25)
            else: 
                turtle.shapesize(0.5, 0.25)
            
            # Paint the circles 
            turtle.pendown()
            turtle.shape("circle")
            turtle.penup()

            pos = turtle.pos()
    time.sleep(15)

if __name__ == "__main__":
    main()



"""
transition_matrix={
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
"""