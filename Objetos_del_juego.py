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
        
        # Posicionar nuevo segmento
        if not self.segments:
            new_segment.goto(self.head.xcor(), self.head.ycor())
        else:
            last_segment = self.segments[-1]
            new_segment.goto(last_segment.xcor(), last_segment.ycor())
        
        self.segments.append(new_segment)

class Food:
    def __init__(self):
        self.food = turtle.Turtle()
        self.food.shape("circle")
        self.food.color("red")
        self.food.penup()
        self.generate()
    
    def generate_position(self, avoid_positions=None):
        """Genera una posición aleatoria evitando posiciones ocupadas"""
        if avoid_positions is None:
            avoid_positions = []
            
        while True:
            x = random.randint(-280, 280)
            y = random.randint(-280, 280)
            if (x, y) not in avoid_positions:
                return (x, y)
    
    def generate(self, avoid_positions=None):
        """Genera una nueva posición para la comida"""
        x, y = self.generate_position(avoid_positions)
        self.food.goto(x, y)
