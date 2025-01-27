import time

def check_food_collision(snake, food):
    if snake.head.distance(food.food) < 20:
        food.generate([(seg.xcor(), seg.ycor()) for seg in snake.segments])
        snake.segments.insert(0, snake.create_segment())
        return True
    return False

def check_wall_collision(snake):
    x, y = snake.head.pos()
    return not (-290 < x < 290 and -290 < y < 290)

def check_self_collision(snake):
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            return True
    return False

def game_over(screen):
    screen.update()
    time.sleep(1)
    screen.bye()