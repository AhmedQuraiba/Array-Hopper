#This file contains generic methods mostly unrelated to game behaviour

def show_screen(matrix):
    print("\033[H\033[J", end="")
    height = len(matrix)
    width = len(matrix[0])

    #upper-border outside the matrix
    print(f" _{(width-2)*" "}_")

    #bellow loop is to print the actual matrix
    counter = 0 #to keep track of which row in the loop
    for row in matrix:
        #printing first row
        if (counter == 0):
            print(f"|{"".join(row)}|")

        #last row
        elif (counter == (height-1)):
            print(f"|{"".join(row)}|")

        #middle rows
        else:
            print(f" {"".join(row)} ")
        
        counter +=1

    #lower-border outside the matrix
    print(f" ‾{(width-2)*" "}‾")

#options is an array of strings repersenting user choices
#message is the message represented to the user before selecting an item
def get_input(message, options):
    option_range = len(options)

    user_choice = None

    print(f"{message}")
    while True:
        for option in range (option_range):
            print(f"{option+1}-{options[option]}")
        
        try:
            user_choice = int(input(">"))
            
            if user_choice in range(1,option_range+1):
                break
            else:
                print(f"\nPlease enter a number between 1 and {option_range}")
        except:
            print("\nPlease enter an integer.") #To catch decimals and letters
    
    return user_choice
