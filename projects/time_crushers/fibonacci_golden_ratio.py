import turtle

def fibonacci_sequence(n):
    sequence = [0, 1]
    while len(sequence) < n:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence[:n]

def draw_square(t, length):
    for _ in range(4):
        t.forward(length)
        t.right(90)

def draw_arc(t, radius, extent):
    t.circle(radius, extent)

def plot_fibonacci_golden_spiral(n):
    sequence = fibonacci_sequence(n)
    
    screen = turtle.Screen()
    screen.setup(width=800, height=800)
    
    t = turtle.Turtle()
    t.speed(0)
    
    x, y = 0, 0
    width = height = 10
    direction = 0  # 0: right, 1: up, 2: left, 3: down

    for i in range(2, n):
        t.penup()
        t.goto(x, y)
        t.pendown()

        if direction == 0:  # Right
            draw_square(t, width)
            t.penup()
            t.goto(x + width, y)
            t.pendown()
            draw_arc(t, width, 90)
            x += width
            width = sequence[i]
            direction = 1
        elif direction == 1:  # Up
            draw_square(t, height)
            t.penup()
            t.goto(x, y + height)
            t.pendown()
            draw_arc(t, height, 90)
            y += height
            height = sequence[i]
            direction = 2
        elif direction == 2:  # Left
            x -= sequence[i]
            draw_square(t, width)
            t.penup()
            t.goto(x, y)
            t.pendown()
            draw_arc(t, width, 90)
            width = sequence[i]
            direction = 3
        elif direction == 3:  # Down
            y -= sequence[i]
            draw_square(t, height)
            t.penup()
            t.goto(x, y)
            t.pendown()
            draw_arc(t, height, 90)
            height = sequence[i]
            direction = 0

    turtle.done()

# Test with a number
plot_fibonacci_golden_spiral(10000)
