import time

def check_food_collision(snake, food):
    """Comprueba si la cabeza de la serpiente choca con el alimento.

    Args:
        snake: El objeto serpiente.
        food: El objeto alimento.

    Returns:
        True si hay una colisión, False en caso contrario.
    """

    if snake.head.distance(food) < 20:
        # Genera nuevas posiciones para el alimento (ajusta según la implementación de food.generate)
        new_food_positions = [(seg.xcor(), seg.ycor()) for seg in snake.segments]
        food.generate(new_food_positions)  # Llama a food.generate con las nuevas posiciones
        snake.segments.insert(0, snake.create_segment())
        return True
    return False

def check_wall_collision(snake, screen):
    """Comprueba si la cabeza de la serpiente choca con las paredes.

    Args:
        snake: El objeto serpiente.
        screen: El objeto pantalla de Turtle.

    Returns:
        True si hay una colisión, False en caso contrario.
    """

    x, y = snake.head.pos()
    screen_width, screen_height = screen.window_width() // 2, screen.window_height() // 2
    return not (-screen_width < x < screen_width and -screen_height < y < screen_height)

# Corrige la función check_wall_collision
def check_wall_collision(snake):
    """Comprueba colisión con paredes (versión simplificada)"""
    x, y = snake.head.pos()
    return not (-290 < x < 290 and -290 < y < 290)

def game_over(screen):
    """Muestra un mensaje de juego terminado y cierra la pantalla.

    Args:
        screen: El objeto pantalla de Turtle.
    """

    screen.update()
    time.sleep(1)
    screen.bye()