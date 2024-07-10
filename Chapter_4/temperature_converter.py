###Program: GUI temperature converter from degree celsius to fahrenheit

from graphics import * 

def gui():
    win = GraphWin("Temperature Cnverter", 500, 500)
    win.setCoords(0.0, 0.0, 50, 50)

    Text(Point(20, 40), "Celsius Temperature:").draw(win)

    input_box = Entry(Point(30, 40),5)
    input_box.setText("0.0")
    input_box.draw(win)

    button = Text(Point(25, 25), "Convert it")
    button.draw(win)

    Rectangle(Point(10, 28), Point(40,20)).draw(win)

    Text(Point(20, 10), "fahreheit:").draw(win)

    celcius = float(input_box.getText())
    fahreheit = 9 / 5 * celcius + 32
    print(fahreheit)

    win.getMouse()

    output = Text(Point(40, 10), str(fahreheit))
    output.draw(win)

    input("")
    win.close()


gui()

