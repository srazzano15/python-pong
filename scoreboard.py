from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Courier', 80, 'normal')

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color('white')
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def paint_dotted(self):
        y_anchor = -330
        #self.pendown()
        while y_anchor <= 330:
            self.forward(10)
            self.penup()
            self.forward(20)
            self.pendown()
            y_anchor += 30

    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(f'{self.l_score}', align=ALIGNMENT, font=FONT)
        self.goto(100, 200)
        self.write(f'{self.r_score}', align=ALIGNMENT, font=FONT)
