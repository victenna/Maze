import turtle
import random
import time
t1=turtle.Turtle('square')
wn=turtle.Screen()
wn.setup(500,500)
t1.color('red')
t1.shapesize(0.9)
t1.penup()
turtle.tracer(2,4)
wn.bgcolor('lightgray')

Array0=[1,1,1,1,1,1,1,1,0,1]
Array1=[1,1,1,1,1,1,1,1,0,1]
Array2=[1,1,1,1,1,1,1,1,0,1]
Array3=[1,1,1,1,1,1,1,1,0,1]
Array4=[1,0,0,0,0,0,0,0,0,1]
Array5=[1,0,1,1,1,1,1,1,1,1]
Array6=[1,0,1,1,1,1,1,1,1,1]
Array7=[1,0,1,1,1,1,1,1,1,1]
Array8=[1,0,0,0,0,0,0,1,1,1]
Array9=[1,1,1,1,1,1,0,1,1,1]


q0=[0,0,0,0,0,0,0,0,0,0]
q1=[0,0,0,0,0,0,0,0,0,0]
q2=[0,0,0,0,0,0,0,0,0,0]
q3=[0,0,0,0,0,0,0,0,0,0]
q4=[0,0,0,0,0,0,0,0,0,0]
q5=[0,0,0,0,0,0,0,0,0,0]
q6=[0,0,0,0,0,0,0,0,0,0]
q7=[0,0,0,0,0,0,0,0,0,0]
q8=[0,0,0,0,0,0,0,0,0,0]
q9=[0,0,0,0,0,0,0,0,0,0]

delta0=[0,0,0,0,0,0,0,0,0,0]
delta1=[0,0,0,0,0,0,0,0,0,0]
delta2=[0,0,0,0,0,0,0,0,0,0]
delta3=[0,0,0,0,0,0,0,0,0,0]
delta4=[0,0,0,0,0,0,0,0,0,0]
delta5=[0,0,0,0,0,0,0,0,0,0]
delta6=[0,0,0,0,0,0,0,0,0,0]
delta7=[0,0,0,0,0,0,0,0,0,0]
delta8=[0,0,0,0,0,0,0,0,0,0]
delta9=[0,0,0,0,0,0,0,0,0,0]

#_______________________________

t=turtle.Turtle()
t.shape('square')
t.shapesize(0.8)
t.color('blue')
t.penup()
t.goto(-120,-120)

def show(j):
   #print (q)
   if q==1:
       t1.showturtle()
       t1.goto(-100+i*20,j)
       t1.stamp()
       t1.hideturtle()

for i in range (10):
   
   q=Array0[i]
   #print (q)
   show(-100)
   q0[i]=t1.position()
       
#Array1    
for i in range (10):
   
   q=Array1[i]
   #print (q)
   show(-80)
   q1[i]=t1.position()
   
       
#Array2
for i in range (10):
   
   q=Array2[i]
   #print (q)
   show(-60)
   q2[i]=t1.position()
       
#Array3
for i in range (10):
   
   q=Array3[i]
   #print (q)
   show(-40)
   q3[i]=t1.position()

#Array4

for i in range (10):
   
   q=Array4[i]
   #print (q)
   show(-20)
   q4[i]=t1.position()

#Array5
    
for i in range (10):
   
   q=Array5[i]
   #print (q)
   show(0)
   q5[i]=t1.position()

#Array6

for i in range (10):
   
   q=Array6[i]
   show(20)
   q6[i]=t1.position()

#Array7
    
for i in range (10):
   
   q=Array7[i]
   #print (q)
   show(40)
   q7[i]=t1.position()
   
#Array8
    
for i in range (10):
   
   q=Array8[i]
   #print (q)
   show(60)
   q8[i]=t1.position()

#Array9

for i in range (10):
   
   q=Array9[i]
   #print (q)
   show(80)
   q9[i]=t1.position()


def condition(dir):
   

   t.setheading(dir)
   t.fd(20)
   a=t.position()
   
 
   for k in range(10):
       
      #print('a=',a)
      
      delta0[k]=abs(q0[k]-a)
      delta1[k]=abs(q1[k]-a)
      delta2[k]=abs(q2[k]-a)
      delta3[k]=abs(q3[k]-a)
      delta4[k]=abs(q4[k]-a)
      delta5[k]=abs(q5[k]-a)
      delta6[k]=abs(q6[k]-a)
      delta7[k]=abs(q7[k]-a)
      delta8[k]=abs(q8[k]-a)
      delta9[k]=abs(q9[k]-a)
      
      #print('delta=',delta0[k])
      
      if delta0[k]<19:
         t.goto(-200,-120)
         t.fd(-20)     
         a=t.position()

      if delta1[k]<19:
         t.goto(-200,-120)
         t.fd(-20)     
         a=t.position()

      if delta2[k]<19:
         t.goto(-200,-120)
         t.fd(-20)     
         a=t.position()

      if delta3[k]<19:
         t.goto(-200,-120)
         t.fd(-20)     
         a=t.position()

      if delta4[k]<19:
         t.goto(-200,-120)
         t.fd(-20)     
         a=t.position()

      if delta5[k]<19:
         t.goto(-200,-120)
         t.fd(-20)     
         a=t.position()

      if delta6[k]<19:
         t.goto(-200,-120)
         t.fd(-20)     
         a=t.position()

      if delta7[k]<19:
         t.goto(-200,-120)
         t.fd(-20)     
         a=t.position()

      if delta8[k]<19:
         t.goto(-200,-120)
         t.fd(-20)     
         a=t.position()

      if delta9[k]<19:
         t.goto(-200,-120)
         t.fd(-20)     
         a=t.position()

#________________________________________________
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


