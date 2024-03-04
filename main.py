from turtle import Screen, Turtle, mainloop, listen, onkeypress, tracer, Vec2D, bgcolor
from random import choice

class Target(Turtle):
    colors = ['green', 'orange', 'yellow', 'pink', 'purple', 'gold', 'gray', 'brown', 'white']

    def __init__(self, x, y):
        super().__init__()
        self.white = False
        self.shapesize(1, 2.5)
        self.color(choice(self.colors))
        self.shape('square')
        self.penup()
        self.goto(x, y)


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shapesize(1, 5)
        self.color('blue')
        self.shape('square')
        self.penup()
        self.goto(0, -300)

    def goleft(self):
        if self.xcor() >= -240:
            self.setx(self.xcor() - 10)

    def goright(self):
        if self.xcor() <= 240:
            self.setx(self.xcor() + 10)


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shapesize(1)
        self.color('red')
        self.shape('circle')
        self.penup()
        self.goto(0, -200)  # Adjusted initial position above the bottom
        self.dy = 2  # Set the initial direction to move upward

class Game:
    tx, ty = -250, 300
    dy = 1
    dx = choice([-.5, .5])
    targets = []

    def __init__(self):
        tracer(0)
        self.pl = Player()
        self.ball = Ball()
        self.game_running = True  # Flag to indicate whether the game should continue
        for _ in range(5):
            for _ in range(10):
                target = Target(self.tx, self.ty)
                self.targets.append(target)
                self.tx += 55
            self.ty -= 25
            self.tx = -250
        tracer(1)

    def update(self):
        if self.ball.ycor() < -300:
            self.game_running = False  # Stop the game

        if not self.game_running:
            return  # Exit the update function if the game is not running

        if self.ball.ycor() > 300:
            self.dy *= -1

        if self.ball.ycor() >= 175:
            for target in self.targets:
                if not target.white:
                    if self.ball.ycor() >= target.ycor() - 25:
                        if self.ball.xcor() >= target.xcor() - 25:
                            if self.ball.xcor() <= target.xcor() + 25:
                                self.dy *= -1
                                target.color('black')
                                target.white = True
                                break

        if self.ball.xcor() <= -270 or self.ball.xcor() >= 260:
            self.dx *= -1
        if self.ball.ycor() <= self.pl.ycor() + 25:
            if self.ball.xcor() >= self.pl.xcor() - 50:
                if self.ball.xcor() <= self.pl.xcor() + 50:
                    self.dy *= -1
        self.ball.setpos(self.ball.xcor() + self.dx * 3, self.ball.ycor() - self.dy * 3)


def enable_keys(pl):
    onkeypress(pl.goleft, "Left")
    onkeypress(pl.goright, "Right")


def start():
    screen = Screen()
    screen.bgcolor(0, 0, 0)
    screen.setup(width=screen.window_width(), height=screen.window_height())
    game = Game()
    enable_keys(game.pl)
    listen()

    while 1:
        game.update()
        if not game.game_running:
            break  # Break out of the main loop when the game is not running


if __name__ == '__main__':
    start()
    mainloop()
