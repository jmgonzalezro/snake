from turtle import Screen, Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20


class Snake:

    def __init__(self):
        self.initial_segments = []
        self.create_snake()
        self.movement()

    def create_snake(self):
        for position in STARTING_POSITIONS:
            new_segment = Turtle('square')
            new_segment.color('white')
            new_segment.penup()
            new_segment.goto(position)
            self.initial_segments.append(new_segment)
    
    def movement(self):
        for seg_num in range(len(self.initial_segments)-1, 0, -1):
            new_x = self.initial_segments[seg_num-1].xcor()
            new_y = self.initial_segments[seg_num-1].ycor()
            self.initial_segments[seg_num].goto(new_x, new_y)
        
        self.initial_segments[0].forward(MOVE_DISTANCE)