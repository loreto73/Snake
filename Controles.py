def setup_controls(screen, snake):
    screen.listen()
    screen.onkeypress(lambda: set_direction(snake, "up"), "Up")
    screen.onkeypress(lambda: set_direction(snake, "down"), "Down")
    screen.onkeypress(lambda: set_direction(snake, "left"), "Left")
    screen.onkeypress(lambda: set_direction(snake, "right"), "Right")

def set_direction(snake, direction):
    opposite_directions = {
        "up": "down",
        "down": "up",
        "left": "right",
        "right": "left"
    }
    if snake.direction != opposite_directions[direction]:
        snake.direction = direction

def move_snake(snake):
    if snake.direction == "up":
        y = snake.head.ycor()
        snake.head.sety(y + 20)
    elif snake.direction == "down":
        y = snake.head.ycor()
        snake.head.sety(y - 20)
    elif snake.direction == "left":
        x = snake.head.xcor()
        snake.head.setx(x - 20)
    elif snake.direction == "right":
        x = snake.head.xcor()
        snake.head.setx(x + 20)

    for index in range(len(snake.segments)-1, 0, -1):
        x = snake.segments[index-1].xcor()
        y = snake.segments[index-1].ycor()
        snake.segments[index].goto(x, y)
        
    if snake.segments:
        snake.segments[0].goto(snake.head.xcor(), snake.head.ycor())