import turtle

alice = turtle.Turtle()
bob = turtle.Turtle()
print(bob)

# def square(t):
#     for i in range(4):
#         t.fd(100)
#         t.lt(90)
# square(bob)
# square(alice)


# def square(t, length):
#     for i in range(4):
#         t.fd(length)
#         t.lt(90)
# square(bob, 100)

def polygon(t, n, length):
    angle = 360 / n
    for i in range(n):
        t.fd(length)
        t.lt(angle)
polygon(bob, 20, 30)

import math

# def circle(t, r):
#     circumference = 2* math.pi * r
#     n = 50
#     length = circumference / n
#     polygon(t, n, length)



# def circle(t, r):
#     circumference = 2 * math.pi * r
#     n = int(circumference / 3) + 1
#     length = circumference / n
#     polygon(t, n, length)




def arc(t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = angle / n

    for i in range(n):
        t.fd(step_length)
        t.lt(step_angle)

def polyline(t, n, length, angle):
    for i in range(n):
        t.fd(length)
        t.lt(angle)

def polygon(t, n, length):
    angle = 360.0 / n
    polyline(t, n, length, angle)

def arc(t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n
    polyline(t, n, step_length, step_angle)

def circle(t, r):
    arc(t, r, 360)

circle(alice, 70)
turtle.mainloop()