###Program: Color to grayscale converter

from graphics import *

def convert_gray(file)->None:
    #Displaying the gif image
    win = GraphWin("Grayscale converter", 320, 320)
    image = Image(Point(160, 160), file)
    image.draw(win)

    #image height and width
    height, width = image.getHeight(), image.getWidth()


    #converting each pixels to grayscale
    for i in range(0, height):
        for j in range(0, width):
            r, g, b = image.getPixel(i, j)
            brightness = int(round(0.299*r + 0.587*g + 0.114*b))
            image.setPixel(i, j, color_rgb(brightness, brightness, brightness))
        win.update()

    #saving the gif file
    name = input("Enter the name to save the grayscale image: ")
    image.save(name+".gif")
    
def main()->None:
    
    #gif image location
    file = "Image_1.gif"

    #converting the color image to grayscale
    convert_gray(file)

main()
