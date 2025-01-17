###Program: Color image to negative image

from graphics import *

def convert_negative(file)->None:
    #displaying the gif image
    win = GraphWin("Color to negative converter", 320, 320)
    image = Image(Point(160, 160), file)
    image.draw(win)

    #image height and width
    height, width = image.getHeight(), image.getWidth()

    #converting to negative image
    for i in range(0, height):
        for j in range(0, width):
            r, g, b = image.getPixel(i, j)
            image.setPixel(i, j, color_rgb(255-r, 255-g, 255-b))
        win.update()

    #saving the gif image
    name:str = input("Enter a name to save the negative image: ")
    image.save(name+".gif")
    
def main()->None:
    file = "Image_1.gif"

    #converting to negative image
    convert_negative(file)


main()
