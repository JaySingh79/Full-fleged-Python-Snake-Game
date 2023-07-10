from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as file:
            self.high_score = file.read()
        self.write_this()

    def write_this(self):
        self.setpos(0,290)
        self.hideturtle()
        self.clear()
        self.pencolor("white")
        self.color("white")
        self.write(f"score: {self.score} High score: {self.high_score}", align='center', font=('Courier',18,'bold'))

    def new_score(self):
        self.clear()
        self.high_score = self.score
        with open("data.txt", mode='w') as file:
            file.write(f"{self.high_score}")
        self.write_this()


    def game_over(self):
        self.write("Game Over", align='Right',font=('courier',24, 'bold'))


