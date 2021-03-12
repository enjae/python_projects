from turtle import *

bgcolor("black")

def draw_O(x,y):
# Draw an O
   pensize(4)
   color("black")
   penup()
   goto(x,y)
   setheading(-45)
   begin_fill()
   color("forest green")
   forward(18) #height
   pendown()
   forward(999) #width
   circle(11, 90)
   forward(48)
   circle(11, 90)
   forward(999)
   circle(11, 90)
   forward(48)
   circle(11, 90)
   forward(999)
   penup()
   forward(12 + 98)
   pendown()
   end_fill()

   onkey(draw_O, "o")

def draw_O1(x,y):
# Draw an O
   pensize(4)
   color("black")
   penup()
   goto(x,y)
   setheading(-135)
   begin_fill()
   color("forest green")
   forward(18) #height
   pendown()
   forward(1199) #width
   circle(11, 90)
   forward(48)
   circle(11, 90)
   forward(1199)
   circle(11, 90)
   forward(48)
   circle(11, 90)
   forward(1199)
   penup()
   forward(12 + 98)
   pendown()
   end_fill()

   onkey(draw_O, "o")

def draw_O2(x,y):
# Draw an O
   pensize(4)
   color("black")
   penup()
   goto(x,y)
   setheading(-90)
   begin_fill()
   color("forest green")
   forward(18) #height
   pendown()
   forward(1199) #width
   circle(5, 90)
   forward(48)
   circle(5, 90)
   forward(1199)
   circle(5, 90)
   forward(48)
   circle(5, 90)
   forward(1199)
   penup()
   forward(12 + 98)
   pendown()
   end_fill()

   onkey(draw_O, "o")


def sun(x,y):
    width(13)
    penup()
    goto(x,y)
    pendown()
    pencolor("dark green")
    setheading(0)
    begin_fill()
    circle(230)
    color("green yellow")
    end_fill()

def text(x,y):
    width(6)
    penup()
    goto(x,y)
    pendown()
    color("green yellow")
    style = ("Comic Sans MS", 39, "bold italic")
    write('Aww', font=style, align='center')


def text3(x,y):
    width(6)
    penup()
    goto(x,y)
    pendown()
    color("green yellow")
    style = ("Comic Sans MS", 39, "bold italic")
    write('Jeeeezz!', font=style, align='center')




def face(x,y):
    width(4)
    color("black")
    penup()
    goto(x,y)
    setheading(0)
    pendown()
    color("black","peach puff")
    begin_fill()
    circle(120)
    end_fill()


def ears(x, y):  # 耳朵
    width(4)
    color("black","peach puff")
    penup()
    goto(x, y)
    pendown()
    begin_fill()
    setheading(0)
    circle(-20, 90)
    circle(-22, 90)
    circle(-45, 20)
    end_fill()

def eye1(x,y):  # 眼睛

    color("black", "white")
    penup()
    goto(x,y)
    pendown()
    setheading(0)
    #forward(-20)
    #setheading(0)
    #forward(-95)
    pendown()
    begin_fill()
    circle(38)
    end_fill()

    color("black")
    penup()
    setheading(60)
    forward(32)
    setheading(0)
    forward(-3)
    pendown()
    begin_fill()
    circle(5)
    end_fill()

def eye2(x,y):
    color("black", "white")
    penup()
    goto(x,y)
    pendown()
    setheading(0)
    #forward(-20)
    #setheading(0)
    #forward(-95)
    pendown()
    begin_fill()
    circle(38)
    end_fill()

    color("black")
    penup()
    setheading(60)
    forward(32)
    setheading(0)
    forward(-3)
    pendown()
    begin_fill()
    circle(5)
    end_fill()

def hair(x,y):
    width(4)
    color("black")
    penup()
    goto(x,y)
    setheading(30)
    pendown()
    color("black","sienna")
    begin_fill()
    circle(98,43)
    setheading(90)
    #circle(120,5)
    forward(50)
    setheading(120)
    forward(60)
    circle(98,43)
    setheading(153)
    circle(125,30)
    circle(120,30)
    setheading(199)
    circle(90,30)
    setheading(260)
    forward(10)
    circle(60,45)

    end_fill()

def brow1(x,y):
    width(4)
    color("black")
    penup()
    goto(x,y)
    setheading(0)
    pendown()
    circle(90,20)
    circle(20, 20)

def brow2(x,y):
    width(4)
    color("black")
    penup()
    goto(x,y)
    setheading(180)
    pendown()
    circle(90,10)
    setheading(164)
    forward(35)
    circle(20, 30)

def nose(x,y):
    width(4)
    color("black")
    penup()
    goto(x,y)
    setheading(220)
    pendown()
    circle(20,30)
    circle(7,150)
    setheading(45)
    forward(14)

def mouth(x,y):
    width(4)
    color("black")
    penup()
    goto(x,y)
    setheading(250)
    pendown()
    forward(16)
    circle(7,200)
    setheading(45)

    forward(5)
    width(4)
    setheading(-90)

    forward(5)

    circle(7,200)
    setheading(100)
    forward(16)









def setting():  # parameter setting
    pensize(4)
    hideturtle()

def main():
    setting()

    #draw_O(-428,336)
    #draw_O1(408,426)
    #draw_O2(-209,356)
    sun(11,-150)


    hair(118,0)
    face(0,-75)
    ears(105,30)
    eye1(-90,30)
    eye2(-2, 30)
    brow1(-98,113)
    brow2(28, 113)
    nose(-54,35)
    mouth(-54,-15)
    text(-78,-200)
    text3(5,-260)


    done()

if __name__ == '__main__':
    main()
