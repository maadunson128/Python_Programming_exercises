###Program: To draw a winter scene with chrostmas tree and a snowman

from graphics import *

def main():
    win = GraphWin("Winter Scence", 1000, 600)
    win.setBackground("White")

    ###drawing snowman
    
    #Snowman head
    head = Circle(Point(650, 150), 50)
    head.draw(win)

    #Left eye
    leye = Circle(Point(625, 125), 5)
    leye.draw(win)

    #right eye
    reye = Circle(Point(670, 125), 5)
    reye.draw(win)

    #nose
    nose = Polygon(Point(650, 145), Point(645, 150), Point(655, 160))
    nose.draw(win)

    #mouth
    mouth = Rectangle(Point(625, 175), Point(675, 180))
    mouth.draw(win)

    #outer body
    s_circle = Circle(Point(650, 260), 60)
    s_circle.draw(win)

    l_circle = Circle(Point(650, 420), 100)
    l_circle.draw(win)

    #hands
    l_hand = Line(Point(590, 260), Point(500, 200))
    l_hand.draw(win)

    r_hand = Line(Point(710, 260), Point(800, 200))
    r_hand.draw(win)

    ###Drawing christmas tree
    f_triangle = Polygon(Point(180, 400), Point(70, 500), Point(300, 500))
    f_triangle.draw(win)

    s_triangle = Polygon(Point(180, 300), Point(100, 400), Point(270, 400))
    s_triangle.draw(win)

    t_triangle = Polygon(Point(180, 200), Point(120, 300), Point(250, 300))
    t_triangle.draw(win)

    f_triangle = Polygon(Point(180, 100), Point(125, 200), Point(230, 200))
    f_triangle.draw(win)

    base = Rectangle(Point(170, 500), Point(200, 510))
    base.draw(win)


    ###Drawing snows
    c1 = Circle(Point(100, 108), 5)
    c2 = Circle(Point(120, 229), 5)
    c3 = Circle(Point(110, 326), 5)
    c4 = Circle(Point(130, 409), 5)
    c5 = Circle(Point(300, 101), 5)
    c6 = Circle(Point(320, 222), 5)
    c7 = Circle(Point(300, 330), 5)    
    c8 = Circle(Point(325, 430), 5)
    c9 = Circle(Point(510, 100), 5)
    c10 = Circle(Point(530, 200), 5)
    c11= Circle(Point(525, 300), 5)
    c12 = Circle(Point(522, 400), 5)
    c13 = Circle(Point(723, 110), 5)
    c14 = Circle(Point(734, 230), 5)
    c15 = Circle(Point(740, 340), 5)
    c16 = Circle(Point(750, 450), 5)
    
    c1.draw(win)
    c2.draw(win)
    c3.draw(win)
    c4.draw(win)
    c5.draw(win)
    c6.draw(win)
    c7.draw(win)
    c8.draw(win)
    c9.draw(win)
    c10.draw(win)
    c11.draw(win)
    c12.draw(win)
    c13.draw(win)
    c14.draw(win)
    c15.draw(win)
    c16.draw(win)

   
    for i in range(580):
        c1.move(10, 10)
        update(60)
        
        c2.move(10, 10)
        update(60)
        
        c3.move(10, 10)
        update(60)
        
        c4.move(10, 10)
        update(60)
        
        c5.move(10, 10)
        update(60)
        
        c6.move(10, 10)
        update(60)
        
        c7.move(10, 10)
        update(60)
        
        c8.move(10, 10)
        update(60)
        
        c9.move(10, 10)
        update(60)
        
        c10.move(10, 10)
        update(60)
        
        c11.move(10, 10)
        update(60)
        
        c12.move(10, 10)
        update(60)
        
        c13.move(10, 10)
        update(60)
        
        c14.move(10, 10)
        update(60)
        
        c15.move(10, 10)
        update(60)
        
        c16.move(10,10)
        update(60)
       


    input()

main()