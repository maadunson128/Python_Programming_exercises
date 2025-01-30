###Program: Breakout game simulation
#reference: 

from graphics import *
import time
import random
from die_button import Button

# Constants for bricks and moving bat dimensions
WIN_WIDTH = 500
WIN_HEIGHT = 500
PADDLE_WIDTH = 80
PADDLE_HEIGHT = 10
BALL_RADIUS = 8
BRICK_ROWS = 4
BRICK_COLS = 8
BRICK_WIDTH = WIN_WIDTH / BRICK_COLS
BRICK_HEIGHT = 20
BRICK_GAP = 3

class Breakout:
    def __init__(self):
        '''Creates the elements for the game'''
        self.wantToPlay = self.splashScreen()
        if self.wantToPlay:
            self.win = GraphWin("Breakout", WIN_WIDTH, WIN_HEIGHT)
            self.win.setBackground("black")

            # Paddle for hit the ball
            self.paddle = Rectangle(Point(210, 460), Point(290, 470))
            self.paddle.setFill("white")
            self.paddle.draw(self.win)

            # Ball as shooter
            self.ball = Circle(Point(250, 250), BALL_RADIUS)
            self.ball.setFill("red")
            self.ball.draw(self.win)

            # Bricks
            self.bricks = []
            self.create_bricks()

            # Ball movement
            self.dx = random.choice([-3, 3])
            self.dy = -3


    def splashScreen(self):
        win2 = GraphWin("Splash screen", 500, 500)
        text = Text(Point(250, 150), "BreakOut Game")
        text.draw(win2)

        b1 = Button(win2, Point(100, 350), 80, 35, "Play")
        b1.activate()
        b2 = Button(win2, Point(400, 350), 80, 35, "Quit")
        b2.activate()

        pt = win2.getMouse()
        if b1.clicked(pt):
            win2.close()
            return True
        if b2.clicked(pt):
            return False

    def create_bricks(self):
        """Creates bricks in the play area."""
        for row in range(BRICK_ROWS):
            for col in range(BRICK_COLS):
                x1 = col * BRICK_WIDTH + BRICK_GAP
                y1 = row * BRICK_HEIGHT + BRICK_GAP
                x2 = x1 + BRICK_WIDTH - BRICK_GAP
                y2 = y1 + BRICK_HEIGHT - BRICK_GAP
                brick = Rectangle(Point(x1, y1), Point(x2, y2))
                brick.setFill(random.choice(["blue", "green", "yellow", "red", 'green3', 'orange', 'grey']))
                brick.draw(self.win)
                self.bricks.append(brick)

    def move_paddle(self, direction):
        """Moves the paddle left or right."""
        if direction == "Left" and self.paddle.getP1().getX() > 0:
            self.paddle.move(-30, 0)
        elif direction == "Right" and self.paddle.getP2().getX() < WIN_WIDTH:
            self.paddle.move(30, 0)

    def ball_hits_paddle(self):
        """Checks if the ball hits the paddle."""
        ball_center = self.ball.getCenter()
        paddle_top = self.paddle.getP1().getY()
        paddle_left = self.paddle.getP1().getX()
        paddle_right = self.paddle.getP2().getX()
        return paddle_top - BALL_RADIUS <= ball_center.getY() <= paddle_top and \
               paddle_left <= ball_center.getX() <= paddle_right

    def ball_hits_brick(self):
        """Checks if the ball hits a brick and removes it."""
        ball_center = self.ball.getCenter()
        for brick in self.bricks:
            if brick.getP1().getX() <= ball_center.getX() <= brick.getP2().getX() and \
               brick.getP1().getY() <= ball_center.getY() <= brick.getP2().getY():
                brick.undraw()
                self.bricks.remove(brick)
                return True
        return False

    def play(self):
        """Main game loop."""
        while True:
            # Ball movement
            self.ball.move(self.dx, self.dy)
            ball_center = self.ball.getCenter()

            # Wall collision
            if ball_center.getX() - BALL_RADIUS <= 0 or ball_center.getX() + BALL_RADIUS >= WIN_WIDTH:
                self.dx = -self.dx
            if ball_center.getY() - BALL_RADIUS <= 0:
                self.dy = -self.dy

            # Paddle collision
            if self.ball_hits_paddle():
                self.dy = -self.dy

            # Brick collision
            if self.ball_hits_brick():
                self.dy = -self.dy

            # Lose condition
            if ball_center.getY() + BALL_RADIUS >= WIN_HEIGHT:
                print("Game Over! You Lost.")
                break

            # Win condition
            if not self.bricks:
                print("Congratulations! You Won!")
                break

            # Paddle movement control
            key = self.win.checkKey()
            if key in ["Left", "Right"]:
                self.move_paddle(key)

            time.sleep(0.02) # Decrease it for difficulty increase

        self.win.close()

# Run the game
if __name__ == "__main__":
    game = Breakout()
    if game.wantToPlay:
        game.play()
