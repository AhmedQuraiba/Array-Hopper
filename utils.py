#This file contains generic methods mostly unrelated to game behaviour

def show_screen(matrix):
    height = len(matrix)
    width = len(matrix[0])

    ###Printing the matrix
    #upper-border outside the matrix
    print(f" _{(width-2)*" "}_")
    #printing first row
    print(f"|{width*" "}|")

    #middle rows
    for row in range(height-2): #-2 to execlude first and last rows
        print(f" {width*" "} ")

    #last row
    print(f"|{width*" "}|")
    #upper-border outside the matrix
    print(f" ‾{(width-2)*" "}‾")