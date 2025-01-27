import turtle
import time  # <-- Añadir este import
from Objetos_del_juego import Snake, Food
from Controles import setup_controls, move_snake
from logica_juego import check_food_collision, check_wall_collision, check_self_collision, game_over

def main():
    # Configuración inicial
    screen = turtle.Screen()
    screen.title("Juego de la Serpiente")
    screen.setup(600, 600)
    screen.bgcolor("black")
    screen.tracer(0)
    
    # Inicializar objetos
    snake = Snake()
    food = Food()
    setup_controls(screen, snake)
    
    # Bucle principal
    while True:
        screen.update()
        
        move_snake(snake)
        
        check_food_collision(snake, food)
        
        if check_wall_collision(snake) or check_self_collision(snake):
            game_over(screen)
            break
        
        # Control de velocidad CORREGIDO
        velocidad = max(0.05, 0.1 - 0.001 * len(snake.segments))
        time.sleep(velocidad)  # <-- Usar time.sleep en lugar de turtle.delay

if __name__ == "__main__":
    main()