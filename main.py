import utils as ut

size = 10
map =[]

#generates n rows and insert them into map
for row in range(size):
    add_row = []
    #generates n elements and insert them into the row
    for column in range(size):
        add_row.append(" ")
    
    map.append(add_row)

ut.show_screen(map)