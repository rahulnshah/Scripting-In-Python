import turtle 
import time
from datetime import datetime, date

# the main method  
def main():
    s = turtle.Screen()
    s.bgcolor("black")
    t = turtle.Turtle()
    t.hideturtle() 
    pen = t.getpen()
    pen.pencolor("#33cc8c")
    pen.write(time.strftime("%I : %M : %S %p"), move=False, align="center", font=("Times New Roman", 24, "normal"))
    time.sleep(1)
    pen.clear()
    pen.write(str(24 - (1 + int(time.strftime("%H"))))+ " hours" + " and " + str(60 - int(time.strftime("%M"))) + " mins left until\n      " + datetime.now().strftime('%B') + " " + str(date.today().day) + ", " + str(date.today().year) + " ends." , move=False, align="center", font=("Times New Roman", 24, "normal"))
    time.sleep(2)
    # closes the window
    turtle.bye()
if __name__ == '__main__':
    main()