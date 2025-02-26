import turtle
import time
from Objetos_del_juego import Snake, Food
from Controles import setup_controls, move_snake
from logica_juego import check_food_collision, check_wall_collision, check_self_collision, game_over

def main():
    screen = turtle.Screen()
    screen.title("Juego de la Serpiente")
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.tracer(0)

    snake = Snake()
    food = Food()
    setup_controls(screen, snake)

    score = 0
    score_display = turtle.Turtle()
    score_display.color("white")
    score_display.penup()
    score_display.hideturtle()
    score_display.goto(0, 270)
    score_display.write(f"Puntuación: {score}", align="center", font=("Courier", 16, "normal"))

    while True:
        screen.update()
        move_snake(snake)

        if check_food_collision(snake, food):
            score += 1
            score_display.clear()
            score_display.write(f"Puntuación: {score}", align="center", font=("Courier", 16, "normal"))
            snake.add_segment()
            food.generate()

        velocidad = max(0.1, 0.2 - 0.002 * len(snake.segments)) # Velocidad inicial más lenta
        time.sleep(velocidad)

        if check_wall_collision(snake) or check_self_collision(snake):
            game_over(screen, score)
            break

if __name__ == "__main__":
    main()