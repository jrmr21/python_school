import random

# the real number of cell is : (number_of_cell * number_of_cell)
print("Enter cell number (cell*cell): ")
number_of_cell = int(input())

f = open('start_cell.txt', 'w')

# move X axe in tab, ex : cells[X][Y]
for x in range(number_of_cell):
        #move Y axe in tab
    for y in range(number_of_cell):
        if random.choice([0 , 1]) == 1 :
            f.write('O')
        else :
            f.write('.')
    f.write('\n')

f.close()