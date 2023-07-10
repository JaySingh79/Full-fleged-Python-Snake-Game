from turtle import Turtle
MOVE_DISTANCE = 20
pos = [(-i,0) for i in range(0,41,20)]

class Snake:

    def __init__(self,snakes_color):
        self.snake_color = snakes_color
        self.tim_instances = []
        self.create_snake()

    def create_snake(self):
        for i in pos:
            self.add_segment(i)

    def add_segment(self,posi):
        tim = Turtle(shape="square")
        tim.penup()
        tim.color(self.snake_color)
        tim.setpos(posi)
        self.tim_instances.append(tim)

    def extend(self):
        self.add_segment(self.tim_instances[-1].position())

    def move(self):

        for i in range(len(self.tim_instances)-1, 0, -1):

            new_x = self.tim_instances[i - 1].xcor()
            new_y = self.tim_instances[i - 1].ycor()
            self.tim_instances[i].goto(new_x, new_y)

        self.tim_instances[0].forward(MOVE_DISTANCE)


    def go_up(self):
        if self.tim_instances[0].heading() != 270:
            self.tim_instances[0].seth(90)

    def go_down(self):
        if self.tim_instances[0].heading()!= 90:
            self.tim_instances[0].seth(270)

    def go_left(self):
        if self.tim_instances[0].heading()!= 0:
            self.tim_instances[0].seth(180)

    def go_right(self):
        if self.tim_instances[0].heading() != 180:
            self.tim_instances[0].seth(0)

    def reset(self):
        self.tim_instances[0].goto(0,0)







