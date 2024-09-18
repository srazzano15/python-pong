from turtle import Turtle

USER_CONTROLS = {
    1: {
        'up': 'w',
        'down': 's'
    },
    2: {
        'up': 'Up',
        'down': 'Down'
    },
}

class Player(Turtle):

    def __init__(self, player_num):
        super().__init__()
        self.score = 0
        self.player = player_num
        self.shape('square')
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.color('white')
        self.penup()
        user_x = -350 if player_num == 1 else 350
        self.setx(user_x)
        self.controls = USER_CONTROLS[player_num]

    def move_up(self):
        if self.ycor() < 220:
            new_y = self.ycor() + 20
            self.goto(self.xcor(), new_y)

    def move_down(self):
        if self.ycor() > -220:
            new_y = self.ycor() - 20
            self.goto(self.xcor(), new_y)