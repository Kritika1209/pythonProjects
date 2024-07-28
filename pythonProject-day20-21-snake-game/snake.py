from turtle import Turtle, Screen

STARTING_POSITIONS= [(0,0),(-20,0),(-40,0)]
UP= 90
DOWN= 270
LEFT= 180
RIGHT=0
class Snake:
    #making initial snake
    def __init__(self):
        self.snake_list=[]
        self.x_cor = 0
        self.create_snake()
        self.head= self.snake_list[0]



    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        snake = Turtle("square")
        snake.penup()
        snake.color("white")
        snake.goto(position)
        self.snake_list.append(snake)

    def extend(self):
        self.add_segment(self.snake_list[-1].position())

    def reset(self):
        for seg in self.snake_list:
            seg.goto(1000,1000)
        self.snake_list.clear()
        self.create_snake()
        self.head = self.snake_list[0]


    def move(self):

        for seg_no in range(len(self.snake_list) - 1, 0, -1):
            new_x = self.snake_list[seg_no - 1].xcor()
            new_y = self.snake_list[seg_no - 1].ycor()
            self.snake_list[seg_no].goto(new_x, new_y)
        self.snake_list[0].forward(20)

    def up(self):
        if self.snake_list[0].heading() != DOWN:
            self.snake_list[0].seth(UP)


    def down(self):
        if self.snake_list[0].heading() != UP:
            self.snake_list[0].seth(DOWN)


    def left(self):
        if self.snake_list[0].heading() != RIGHT:
            self.snake_list[0].seth(LEFT)


    def right(self):
        if self.snake_list[0].heading() != LEFT:
            self.snake_list[0].seth(RIGHT)
