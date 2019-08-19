import turtle
t=turtle.Turtle()
wn=turtle.Screen()
#turtle.tracer(3)
t.shape('circle')
t.shapesize(0.8)
t.color('blue')
t.penup()
t.goto(-100,-100)
#_________________________________
t1=turtle.Turtle('square')
t1.color('red')
t1.shapesize(0.8)
t1.penup()
t1.goto(-40,-40)
b1=t1.position()

t3=turtle.Turtle('square')
t3.color('red')
t3.shapesize(0.8)
t3.penup()
t3.goto(0,-40)
b3=t3.position()

t4=turtle.Turtle('square')
t4.color('red')
t4.shapesize(0.8)
t4.penup()
t4.goto(20,-40)
b4=t4.position()

t5=turtle.Turtle('square')
t5.color('red')
t5.shapesize(0.8)
t5.penup()
t5.goto(40,-40)
b5=t5.position()
#__________________________________

t6=turtle.Turtle('square')
t6.color('red')
t6.shapesize(0.8)
t6.penup()
t6.goto(-40,-20)
b6=t6.position()

t10=turtle.Turtle('square')
t10.color('red')
t10.shapesize(0.8)
t10.penup()
t10.goto(40,-20)
b10=t10.position()
#___________________________________

t11=turtle.Turtle('square')
t11.color('red')
t11.shapesize(0.8)
t11.penup()
t11.goto(-40,0)
b11=t11.position()

t12=turtle.Turtle('square')
t12.color('red')
t12.shapesize(0.8)
t12.penup()
t12.goto(-20,0)
b12=t12.position()

t13=turtle.Turtle('square')
t13.color('red')
t13.shapesize(0.8)
t13.penup()
t13.goto(0,0)
b13=t13.position()

t15=turtle.Turtle('square')
t15.color('red')
t15.shapesize(0.8)
t15.penup()
t15.goto(40,0)
b15=t15.position()
#___________________________________________

t16=turtle.Turtle('square')
t16.color('red')
t16.shapesize(0.8)
t16.penup()
t16.goto(-40,20)
b16=t16.position()

t17=turtle.Turtle('square')
t17.color('red')
t17.shapesize(0.8)
t17.penup()
t17.goto(-20,20)
b17=t17.position()

t20=turtle.Turtle('square')
t20.color('red')
t20.shapesize(0.8)
t20.penup()
t20.goto(40,20)
b20=t20.position()
#____________________________________


t21=turtle.Turtle('square')
t21.color('red')
t21.shapesize(0.8)
t21.penup()
t21.goto(-40,40)
b21=t21.position()

t22=turtle.Turtle('square')
t22.color('red')
t22.shapesize(0.8)
t22.penup()
t22.goto(-20,40)
b22=t22.position()

t24=turtle.Turtle('square')
t24.color('red')
t24.shapesize(0.8)
t24.penup()
t24.goto(20,40)
b24=t24.position()

t25=turtle.Turtle('square')
t25.color('red')
t25.shapesize(0.8)
t25.penup()
t25.goto(40,40)
b25=t25.position()


def condition(dir):
    t.setheading(dir)
    t.fd(20)
    a=t.position()
    delta1=abs(b1-a)
    delta3=abs(b3-a)
    delta4=abs(b4-a)
    delta5=abs(b5-a)
    delta6=abs(b6-a)
    delta10=abs(b10-a)
    delta11=abs(b11-a)
    delta12=abs(b12-a)
    delta13=abs(b13-a)
    delta15=abs(b15-a)
    delta16=abs(b16-a)
    delta17=abs(b17-a)
    delta20=abs(b20-a)

    delta21=abs(b21-a)
    delta22=abs(b22-a)
    delta24=abs(b24-a)
    delta25=abs(b25-a)
    #________________________________
    
    if delta1<19:
        t.goto(-100,-100)
    if delta3<19:
        t.goto(-100,-100)
    if delta4<19:
        t.goto(-100,-100)
    if delta5<19:
        t.goto(-100,-100)
    if delta6<19:
        t.goto(-100,-100)
    if delta10<19:
        t.goto(-100,-100)
    if delta11<19:
        t.goto(-100,-100)
    if delta12<19:
        t.goto(-100,-100)
    if delta13<19:
        t.goto(-100,-100)
    if delta15<19:
        t.goto(-100,-100)
    if delta16<19:
        t.goto(-100,-100)
    if delta17<19:
        t.goto(-100,-100)
    if delta20<19:
        t.goto(-100,-100)
    if delta21<19:
        t.goto(-100,-100)
    if delta22<19:
        t.goto(-100,-100)
    if delta24<19:
        t.goto(-100,-100)
    if delta25<19:
        t.goto(-100,-100)


def left():
       
    condition(180)
         
def right():
       
    condition(0)
         
def up():
        
    condition(90)
        
def down():
        
    condition(-90)
        
        
turtle.onkey(left,"Left")
             
turtle.onkey(right, "Right")
             
turtle.onkey(up, "Up")
             
turtle.onkey(down, "Down")

wn.listen()




      


    




            


