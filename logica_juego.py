import turtle
import time

def check_food_collision(snake, food):
    """Comprueba si la serpiente come la comida"""
    if snake.head.distance(food.food) < 20:
        # Genera nueva posición para la comida
        new_food_positions = [(seg.xcor(), seg.ycor()) for seg in snake.segments]
        food.generate(new_food_positions)
        snake.add_segment()
        return True
    return False

def check_wall_collision(snake):
    """Comprueba colisión con paredes"""
    x, y = snake.head.pos()
    return not (-290 < x < 290 and -290 < y < 290)

def check_self_collision(snake):
    """Comprueba colisión de la serpiente consigo misma"""
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            return True
    return False

def show_score(score):
    """Muestra la puntuación final"""
    score_display = turtle.Turtle()
    score_display.color("white")
    score_display.penup()
    score_display.hideturtle()
    score_display.goto(0, 0)
    score_display.write(f"Juego Terminado\nPuntuación Final: {score}", 
                        align="center", 
                        font=("Courier", 24, "normal"))

def game_over(screen, score):
    """Gestiona el fin del juego"""
    screen.tracer(1)
    show_score(score)
    time.sleep(2)
    screen.bye()
