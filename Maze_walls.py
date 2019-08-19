import turtle
t1=turtle.Turtle('square')
t2=turtle.Turtle('square')
wn=turtle.Screen()
walls=[]
ARRAY= [[1,1,1,1,1,1,1,1,1,1],
            [1,0,0,0,0,0,0,0,0,1],
            [1,0,1,1,1,1,1,1,1,1],
            [1,0,0,0,0,1,1,1,1,1],
            [1,1,1,1,0,1,1,1,1,1],
            [1,1,1,0,0,1,1,1,1,1],
            [1,1,1,1,0,0,0,0,0,1],
            [1,1,1,1,1,1,1,1,0,1],
            [1,0,0,0,0,0,0,0,0,1],
            [1,0,1,1,1,1,1,1,1,1]]

wn.setup(650,650)
t2.shapesize(2.8)
t2.speed('fastest')
t2.penup()

for i in range(10):
    
    for j in range(10):
        print(ARRAY[i][j],end='')
        
        sx=-300+i*60
        sy=300-j*60
        if ARRAY[i][j]==1:# array element Aij
            t2.goto(sx,sy)
            t2.stamp()
            walls.append((sx,sy))
    print()
                                
t1.color('blue')
t1.shapesize(2.6)
t1.speed(2.6)
t1.penup()
t1.goto(-240,-180)

def up():
    
    X=t1.xcor()
    Y=t1.ycor()+60
    if (X,Y) not in walls: # file array8.py in folder Python Projects/Array
        #output format
        t1.sety(Y)
      
def down():
    X=t1.xcor()
    Y=t1.ycor()-60
    if (X,Y) not in walls:
        t1.goto(X,Y)

def left():
    X=t1.xcor()-60
    Y=t1.ycor()
    if (X,Y) not in walls:
        t1.goto(X,Y)
    
def right():
    X=t1.xcor()+60
    Y=t1.ycor()
    if (X,Y) not in walls:
        t1.goto(X,Y)
turtle.listen()
turtle.onkey(up, 'Up')
turtle.onkey(down, 'Down')
turtle.onkey(left, 'Left')
turtle.onkey(right, 'Right')


