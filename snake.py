"""Snake, classic arcade game.

Exercises

1. How do you make the snake faster or slower?
2. How can you make the snake go around the edges?
3. How would you move the food?
4. Change the snake to respond to mouse clicks.
"""

from random import randrange,choice
from turtle import *
from freegames import square, vector


colors = ['blue', 'green', 'purple', 'orange', 'yellow']

def get_distinct_colors():
    
    color1 = choice(colors)
    color2 = choice(colors)
    while color2 == color1:  # Asegura que los colores sean distintos
        color2 = choice(colors)
    return color1, color2

food = vector(0, 0) # Se crea la comida
snake = [vector(10, 0)] # Se crea la serpiente
aim = vector(0, -10) # Se crea la dirección de la serpiente

# Se cambia la dirección de la serpiente
def change(x, y):
    """Change snake direction."""
    aim.x = x
    aim.y = y
# Se verifica que la serpiente se encuentre dentro de los límites de la pantalla
def inside(head): 
    """Return True if head inside boundaries."""
    return -200 < head.x < 190 and -200 < head.y < 190

# Se define el comportamiento del juego
def move(): 
    """Move snake forward one segment."""
    head = snake[-1].copy() 
    head.move(aim) # La serpiente se mueve en la dirección que se le indica

    if not inside(head) or head in snake: # Se definen los casos en los que la serpiente pierde
        square(head.x, head.y, 9, 'red') # Se dibuja un cuadrado rojo en la posición de la serpiente
        update()
        return

    snake.append(head)

    if head == food: # Se verifica si la serpiente comió
        print('Snake:', len(snake)) # Se imprime el tamaño de la serpiente
        xfood_position = randrange(int((food.x/10)-1),int((food.x/10)+2)) * 10 # Se define la posición de la nueva comida a un paso de
        yfood_position = randrange(int((food.y/10)-1),int((food.y/10)+2)) * 10 # distancia de la comida pasada
        while xfood_position == food.x or yfood_position == food.y or not inside(food): # Se verifica que la comida no se encuentre
            xfood_position = randrange(int((food.x/10)-1),int((food.x/10)+2)) * 10      # en la posición pasada ni fuera de los límites
            yfood_position = randrange(int((food.y/10)-1),int((food.y/10)+2)) * 10
        food.x = xfood_position # Se crea una nueva comida con nueva posición
        food.y = yfood_position 
        print('Food:', food.x, food.y)
        
        # Cambia el color de la comida y la serpiente al azar
        global snake_color,food_color
        snake_color,food_color = get_distinct_colors()

 
    else:
        snake.pop(0) 

    clear()

    

    for body in snake: # Se dibuja la serpiente
        square(body.x, body.y, 9, snake_color) 

    square(food.x, food.y, 9, food_color) # Se dibuja la comida
    update()
    ontimer(move, 100) 


# Define colores iniciales al comenzar el juego
snake_color, food_color = get_distinct_colors()


setup(420, 420, 370, 0) # Se define el tamaño de la pantalla
hideturtle() 
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right') # Se definen las teclas para cambiar la dirección de la serpiente
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()
