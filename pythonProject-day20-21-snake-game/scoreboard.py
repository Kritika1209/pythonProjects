from turtle import Turtle



class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score= 0
        with open("data.txt", mode="r") as file:
            self.high_score= int(file.read())
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.update_score()

        self.hideturtle()

    def update_score(self):
        self.clear()
        self.write(f"Score {self.score}, High Score: {self.high_score}", align="center", font=("Arial", 24, "normal"))


    def reset_score(self):
        if self.score> self.high_score:
            self.high_score=self.score
        with open("data.txt", mode="w") as file:
            self.high_score=str(self.high_score)
            file.write(self.high_score)


        self.score=0
        self.update_score()

    def increase_score(self):
        self.score+=1
        self.update_score()


