import turtle
import random

class Snake:
    def __init__(self):
        self.head = turtle.Turtle()
        self.head.shape("square")
        self.head.color("white")
        self.head.penup()
        self.head.goto(0, 0)
        self.direction = "stop"
        self.segments = []
        self.add_segment()  # Añadir segmento inicial
    
    def add_segment(self):
        """Añade un nuevo segmento a la serpiente"""
        new_segment = turtle.Turtle()
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        
        # Posicionar nuevo segmento fuera de pantalla inicialmente para evitar colisiones falsas
        new_segment.goto(1000, 1000)
        
        self.segments.append(new_segment)

class Food:
    def __init__(self):
        self.food = turtle.Turtle()
        self.food.shape("circle")
        self.food.color("red")
        self.food.penup()
        self.generate()
    
    def generate_position(self, avoid_positions=None):
        """Genera una posición aleatoria evitando posiciones ocupadas y alineada a la cuadrícula"""
        if avoid_positions is None:
            avoid_positions = []
            
        while True:
            # Genera coordenadas en múltiplos de 20 para alinear con el movimiento de la serpiente
            x = random.randint(-14, 14) * 20
            y = random.randint(-14, 14) * 20
            
            # Verifica que la posición no esté ocupada por la serpiente
            if not any(abs(pos[0] - x) < 10 and abs(pos[1] - y) < 10 for pos in avoid_positions):
                return (x, y)
    
    def generate(self, avoid_positions=None):
        """Genera una nueva posición para la comida"""
        x, y = self.generate_position(avoid_positions)
        self.food.goto(x, y)
