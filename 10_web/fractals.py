import turtle
import random

window = turtle.Screen()
window.colormode(255)
window.setup(600,600)


turt = turtle.Turtle()
turt1 = turtle.Turtle()
def draw_koch(t, t1, depth, length):
    if depth == 1:
        t.pencolor(random.randrange(255),random.randrange(255),random.randrange(255))
        t.fd(length)
        t1.pencolor(random.randrange(255),random.randrange(255),random.randrange(255))
        t1.fd(length)
        t.lt(60)
        t1.rt(60)
        t.pencolor(random.randrange(255),random.randrange(255),random.randrange(255))
        t.fd(length)
        t1.pencolor(random.randrange(255),random.randrange(255),random.randrange(255))
        t1.fd(length)
        t.rt(120)
        t1.lt(120)
        t.pencolor(random.randrange(255),random.randrange(255),random.randrange(255))
        t.fd(2 * length)
        t1.pencolor(random.randrange(255),random.randrange(255),random.randrange(255))
        t1.fd(2 * length)
        t.lt(120)
        t1.rt(120)
        t.pencolor(random.randrange(255),random.randrange(255),random.randrange(255))
        t.fd(length)
        t1.pencolor(random.randrange(255),random.randrange(255),random.randrange(255))
        t1.fd(length)
        t.rt(60)
        t1.lt(60)
        t.pencolor(random.randrange(255),random.randrange(255),random.randrange(255))
        t.fd(length)
        t1.pencolor(random.randrange(255),random.randrange(255),random.randrange(255))
        t1.fd(length)
    else:
        draw_koch(t, t1, depth -1, length)
        t.lt(60)
        t1.rt(60)
        draw_koch(t, t1, depth -1, length)
        t.rt(120)
        t1.lt(120)
        draw_koch(t, t1, depth -1, length)
        t.lt(60)
        t1.rt(60)
        draw_koch(t,t1, depth -1, length)
draw_koch(turt,turt1,3,10)

def draw_sierpinski(t, depth, length):
    if depth == 1:
        t.lt(60)
        t.fd(length)
        t.rt(120)
        t.pencolor('white')
        t.pensize(1)
        t.fd(length)
        t.rt(120)
        t.pencolor('black')
        t.fd(length)
        t.rt(180)
        t.pencolor('gray')
        t.pensize(4)
    else:
        draw_sierpinski(t, depth - 1, length/2)
        t.fd(length/2)
        draw_sierpinski(t, depth - 1, length/2)
        t.fd(-length/2)
        t.lt(60)
        t.fd(length / 2)
        t.rt(60)
        draw_sierpinski(t, depth - 1, length/2)
        t.rt(120)
        t.fd(length/2)
        t.lt(120)


draw_sierpinski(turt,4,200)

turt.lt(90)
def tree(t, depth, length, angle):
    if depth == 1:
        t.pencolor('green')
        t.fd(length)
        t.rt(90)
        a = random.randrange(10)
        while a == 0:
            a = random.randrange(10)
        t.fd(length/a)
        t.rt(90)
        t.fd(length)
        t.rt(90)
        t.fd(length/a)
        t.rt(90)
    else:
        t.pencolor('brown')
        t.fd(length)
        t.rt(90)
        a = random.randrange(10)
        while a == 0:
            a = random.randrange(10)
        t.fd(length/a)
        t.rt(90)
        t.fd(length)
        t.rt(90)
        t.fd(length/a)
        t.rt(90)
        t.pensize(2)
        t.fd(length)
        t.lt(angle)
        tree(t, depth - 1, length, angle)
        t.rt(4 * angle)
        t.fd(length/a)
        t.lt(angle)
        tree(t,depth -1,length,angle)
        t.rt(angle)
        t.fd(-length/a)
        t.lt(90)
        t.fd(-length)    

tree(turt,4,50,30)

window.exitonclick()
