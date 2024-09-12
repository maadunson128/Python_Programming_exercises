
from graphics import *
win = GraphWin ( " Ti c-Tac-Toe " )
# set coordinates t o go from (0 , 0) in the lower left
# to (3 , 3) in the upper right .
win . setCoords( 0.0 , 0.0 , 3.0 , 3.0 )
# Draw vert i cal lines
Line (Point ( 1 , 0) , Point ( 1 , 2 ) ) . draw (win)
#

input()