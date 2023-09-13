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

class Painter:
    def __init__(self, object_matrix, object_color_matrix):
        """Initializes the Painter with an object_matrix, object_color_matrix, and objects"""
        # object_matrix: probability that the painter will choose another object based on the current object
        self.object_matrix = object_matrix
       
        # object_color_matrix: probability that the painter will chose a particular color for the next paintstroke 
        self.object_color_matrix = object_color_matrix
        
        self.objects = list(object_matrix.keys())

    
    def get_next_object(self, current_object):
        """Selects the next object to paint based on the current object using the transition matrix, object_matrix"""
        return np.random.choice(
            self.objects,
            p=[self.object_matrix[current_object][next_object] for next_object in self.objects]
        )
    
    def get_next_color(self, current_color, current_object):
        """Selects the next color to paint based on the current color and the current object using the transition matrix, object_color_matrix"""
        matrix = self.object_color_matrix[current_object]
        keys = list(matrix.keys())
        return np.random.choice(
            keys,
            p=[matrix[current_color][next_color] for next_color in matrix]
        )
    
    def paint(self, current_object):
        # Start with the object as sky
        current_object="sky"

        # For 500 object circles
        for _ in range (0,500):
            # Pick type of object (tree, bush, ocean, ...)
            object = self.get_next_object(current_object)
            current_object = object

            # Pick a current color as the first color in the object's color palette 
            current_color = list(self.object_color_matrix[current_object].keys())[0]

            # Choose a random position on the canvas 
            # Each object is restricted to the same area that they appear in the original painting (sky in the top right of the canvas)
            # All of these positions build a larger canvas of 300 x 300 pixels
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
            
            # Paint 10 paintstrokes in the Object Circle chosen above 
            for _ in range(0, 10):
                # Initialize the turtle 
                turtle = Turtle()
                turtle.penup()
                turtle.speed(0)

                # Choose a paint color 
                color = self.get_next_color(current_color, current_object)
                current_color = color
                turtle.color(PALETTE[color])

                # Set paintbrush size and shape
                turtle.shapesize(0.5,0.25)
                turtle.shape("circle")

                # Move the paintbrush to the next spot in the circle
                turtle.setpos(pos)
                direction += 40
                turtle.left(direction)
                turtle.fd(8)

                # Paint a paintstroke  
                turtle.pendown()

                pos = turtle.pos()
        time.sleep(15)


def main():
    """Paint image with a Painter"""
    # Initialize our painter 
    painter = Painter(
    object_matrix={
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
    
    # Start Painting 
    painter.paint("sky")

    
if __name__ == "__main__":
    main()