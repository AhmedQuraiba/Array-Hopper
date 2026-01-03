import utils as ut

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

while True: #game loop
    ut.show_screen(map)

    while True: #input loop
        move = ut.get_input("Choose the direction of your movement:",["Up","Down","Right","Left"])
        #1->Up | 2->Down | 3->Right | 4->Left
        #Up: pos_y - 1 | Down: pos_y + 1 | Right: pos_x + 1 | Left: pos_x - 1

        if (move == 1 and (new_pos_y-1)>=0):
            new_pos_y-=1
            break
        elif (move == 2 and (new_pos_y+1)<=(size-1)):
            new_pos_y+=1
            break
        elif (move == 3 and (new_pos_x+1)<=(size-1)):
            new_pos_x+=1
            break
        elif (move == 4 and (new_pos_x-1)>=0):
            new_pos_x-=1
            break
        else:
            print("You can't move in that direction.")
    
    map[pos_y][pos_x] = " "
    map[new_pos_y][new_pos_x] = "X"

    pos_y = new_pos_y
    pos_x = new_pos_x