import utils as ut
import keyboard as kb
import time

size = 20
map =[]

#generates n rows and insert them into map
for row in range(size):
    add_row = []
    #generates n elements and insert them into the row
    for column in range(size):
        add_row.append(" ")
    
    map.append(add_row)

pos_y = 0                   #to navigate through rows of matrix
pos_x = 0                   #to navigate through columnss of matrix

new_pos_y = 0               #New pos vars are to keep track of both pos after and before a move
new_pos_x = 0               #They will be made equal to pos once a move is completed
map[pos_y][pos_x] = "X"

ut.show_screen(map)

while True: #game loop

    while True: #Input loop
        if kb.is_pressed("w") or kb.is_pressed("up"):
            if (new_pos_y-1)>=0:
                new_pos_y-=1
                break
        elif kb.is_pressed("s") or kb.is_pressed("down"):
            if (new_pos_y+1)<=(size-1):
                new_pos_y+=1
                break
        elif kb.is_pressed("d") or kb.is_pressed("right"):
            if (new_pos_x+1)<=(size-1):
                new_pos_x+=1
                break
        elif kb.is_pressed("a") or kb.is_pressed("left"):
            if (new_pos_x-1)>=0:
                new_pos_x-=1
                break
    
    map[pos_y][pos_x] = " "
    map[new_pos_y][new_pos_x] = "X"

    pos_y = new_pos_y
    pos_x = new_pos_x

    ut.show_screen(map)
    time.sleep(0.2)
