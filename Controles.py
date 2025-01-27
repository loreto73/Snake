def setup_controls(screen, snake):
    """Configura los controles del juego.
    Esta función establece la escucha de eventos de teclado y asigna funciones a las teclas de flecha.

    Args:
        screen: La pantalla donde se muestra el juego.
        snake: El objeto que representa a la serpiente.
    """
    screen.listen()
    screen.onkeypress(lambda: set_direction(snake, "up"), "Up")
    screen.onkeypress(lambda: set_direction(snake, "down"), "Down")
    screen.onkeypress(lambda: set_direction(snake, "left"), "Left")
    screen.onkeypress(lambda: set_direction(snake, "right"), "Right")

def set_direction(snake, direction):
    """Establece la dirección de la serpiente.
    Esta función actualiza la dirección de la serpiente, evitando cambios de dirección inmediatos.

    Args:
        snake: El objeto que representa a la serpiente.
        direction: La nueva dirección deseada.
    """
    opposite_directions = {
        "up": "down",
        "down": "up",
        "left": "right",
        "right": "left"
    }
    if snake.direction != opposite_directions[direction]:
        snake.direction = direction

def move_snake(snake):
    """Mueve la serpiente.

    Esta función actualiza las posiciones de todos los segmentos de la serpiente.

    Args:
        snake: El objeto que representa a la serpiente.
    """
    # Mueve la cabeza de la serpiente
    if snake.direction == "up":
        snake.head.sety(snake.head.ycor() + 20)
    elif snake.direction == "down":
        snake.head.sety(snake.head.ycor() - 20)
    elif snake.direction == "left":
        snake.head.setx(snake.head.xcor() - 20)
    elif snake.direction == "right":
        snake.head.setx(snake.head.xcor() + 20)

    # Mueve los segmentos del cuerpo de la serpiente
    for index in range(len(snake.segments)-1, 0, -1):
        x = snake.segments[index-1].xcor()
        y = snake.segments[index-1].ycor()
        snake.segments[index].goto(x, y)
        
    # El primer segmento (cuello) sigue a la cabeza
    if snake.segments:
        snake.segments[0].goto(snake.head.xcor(), snake.head.ycor())