import time

import pygame as p
import random
from pygame.locals import *


# info doc :
#
# - Rect((left, top), (width, height))
#
# - pygame.draw.rect(surface, color, rect)
#   p.draw.rect(root , BLACK, ((10, 10), (size_of_cell, size_of_cell)))
#
# 2 rules :
# - une cellule morte possédant exactement trois cellules voisines vivantes devient vivante (elle naît) ;
# - une cellule vivante possédant deux ou trois cellules voisines vivantes le reste, sinon elle meurt.


#   RGB
BLACK = (0 , 0 , 0)
WHITE = (255 , 255 , 255)

print("WELCOME IN 'JEU DE LA VIE' :")
print("==========================")
print()


windows_y = 1000
print (windows_y)
# create variable to define resolution of windows (we need carre)
windows_x = windows_y

#   create windows with resolution
root = p.display.set_mode((windows_x , windows_y))

#create cell :
# the real number of cell is : (number_of_cell * number_of_cell)
print("Enter cell number (cell*cell): ")
n = int(input())

number_of_cell = n
print (number_of_cell)

size_of_cell = windows_y / number_of_cell

# create cells[number_of_cell][number_of_cell] to display
cells = [[random.choice([0 , 1]) for j in range(number_of_cell)] for i in range(number_of_cell)]


# function to calculate score of cell (number of friend's in 8cases around)
# we need : 
#           - coordinate in cell two dimentionnal TAB (PosX, posY)
#           - the max coordinate in cell TAB (maxX, maxY)
#           - the TAB cell 
def score_cell(posX, posY, maxX, maxY, cell) :
    score = 0

    if (cell[posX][posY] == 1) :
        score -= 1 # we delete the origin cell count

    for x  in range(0, 3):
        cpX = (posX - 1) + x
        #print("cpX : ", cpX)

        for y in range(0, 3):
            cpY = (posY - 1) + y
            #print("cpY : ", cpY)
            
            if (cpY >= maxY) or (cpX >= maxX) or (cpY < 0) or (cpX < 0) or (cell[cpX][cpY] == 0):
                score += 0
            else :
                score += 1
                # control enable coordinate

    return (score)


# function to update cells tab
def calculate_cell(tab):
    # create new tab of cell to calculate update of cells tab
    next_cells = [[0 for j in range(number_of_cell)] for i in range(number_of_cell)]


    # move X axe in tab, ex : cells[X][Y]
    for x in range(number_of_cell):
        #move Y axe in tab
        for y in range(number_of_cell):

            score = score_cell(x, y, number_of_cell, number_of_cell, tab)

                # it's alive condition
            if (tab[x][y] == 1) :
                if ((score == 2) or (score == 3)):
                    next_cells[x][y] = 1
                    #print ("score is alive ---", score)
                else :
                    next_cells[x][y] = 0
                # dead condition
            else :
                if (score == 3) :
                    #print ("score is dead !!!! ", score)
                    next_cells[x][y] = 1
                else :
                    next_cells[x][y] = 0

    return (next_cells)


# function to display all cells
def show_cell():
    # move X axe in tab, ex : cells[X][Y]
    for x in range(number_of_cell):
        #move Y axe in tab
        for y in range(number_of_cell):
            # if cell is alive, is == 1
            if (cells[x][y] == 1) :
                p.draw.rect(root , BLACK, ((x*size_of_cell, y*size_of_cell), (size_of_cell, size_of_cell)))
            else :
                p.draw.rect(root , WHITE, ((x*size_of_cell, y*size_of_cell), (size_of_cell, size_of_cell))) 


while 1:    
    
    root.fill(WHITE)    # background color

    show_cell()
    cells = calculate_cell(cells)

    for i in p.event.get():
        if i.type == QUIT:
            quit()    

    #time.sleep(0.1)
    # frame, refresh display
    p.display.update()




#      == DEBUG ==
#
#p = [[0 for j in range(5)] for i in range(5)]
#print ("test ")
#p[2][1] = 1
#p[2][2] = 1
#p[2][3] = 1

#for x in range(5):
#    print(p[x])

#print("score : ", score_cell(2,1, 5, 5, p))