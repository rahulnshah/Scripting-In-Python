import turtle 


def printRecursion(tina, pen, x, theSize):
    if(x > 0 ):
        # print('recursion"), printRecursion(x - 1)
        pen.write("Recursion", move = False, align="center", font=("Times New Roman", theSize, "normal"))
        print(x)
        #move turtle down
        tina.right(90)
        tina.penup()
        tina.forward(25)
        tina.left(90)
        tina.pendown()
        #pen.clear()
        printRecursion(tina, pen, x - 1, theSize - 3) # 

def main():
    tina = turtle.Turtle()
    s = turtle.Screen()
    s.bgcolor("black")
    tina.penup()
    tina.goto(0,100)
    pen = tina.getpen()
    pen.pencolor("#33cc8c")
    #pen.write("Recursion", move = False, align="center", font=("Times New Roman", -100, "normal"))
    printRecursion(tina, pen, 4, 12)

    
if __name__ == '__main__':
    main()

    