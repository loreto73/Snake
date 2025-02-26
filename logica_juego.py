import turtle
import time

def check_food_collision(snake, food):
    """Comprueba si la serpiente come la comida"""
    if snake.head.distance(food.food) < 20:
        # Genera nueva posición para la comida evitando el cuerpo de la serpiente
        snake_positions = [(snake.head.xcor(), snake.head.ycor())]
        for segment in snake.segments:
            snake_positions.append((segment.xcor(), segment.ycor()))
        food.generate(snake_positions)
        return True
    return False

def check_wall_collision(snake):
    """Comprueba colisión con paredes"""
    x, y = snake.head.pos()
    return not (-290 < x < 290 and -290 < y < 290)

def check_self_collision(snake):
    """Comprueba colisión de la serpiente consigo misma"""
    for segment in snake.segments[1:]:  # Ignora el primer segmento que siempre estará cerca de la cabeza
        if segment.distance(snake.head) < 10:
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
