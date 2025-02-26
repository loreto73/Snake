def setup_controls(screen, snake):
    """Configura los controles del juego"""
    screen.listen()
    screen.onkeypress(lambda: set_direction(snake, "up"), "Up")
    screen.onkeypress(lambda: set_direction(snake, "down"), "Down")
    screen.onkeypress(lambda: set_direction(snake, "left"), "Left")
    screen.onkeypress(lambda: set_direction(snake, "right"), "Right")

def set_direction(snake, direction):
    """Establece la dirección de la serpiente"""
    opposite_directions = {
        "up": "down",
        "down": "up",
        "left": "right",
        "right": "left"
    }
    # No permitir cambiar a la dirección opuesta
    if snake.direction != opposite_directions.get(direction, None):
        snake.direction = direction

def move_snake(snake):
    """Mueve la serpiente"""
    # Mueve primero los segmentos del cuerpo (desde el último al primero)
    for index in range(len(snake.segments)-1, 0, -1):
        x = snake.segments[index-1].xcor()
        y = snake.segments[index-1].ycor()
        snake.segments[index].goto(x, y)
        
    # El primer segmento sigue a la cabeza
    if snake.segments:
        x_head = snake.head.xcor()
        y_head = snake.head.ycor()
        snake.segments[0].goto(x_head, y_head)
    
    # Ahora mueve la cabeza de la serpiente
    if snake.direction == "up":
        snake.head.sety(snake.head.ycor() + 20)
    elif snake.direction == "down":
        snake.head.sety(snake.head.ycor() - 20)
    elif snake.direction == "left":
        snake.head.setx(snake.head.xcor() - 20)
    elif snake.direction == "right":
        snake.head.setx(snake.head.xcor() + 20)
