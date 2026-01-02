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

#options is an array of strings repersenting user choices
#message is the message represented to the user before selecting an item
def get_input(message, options):
    option_range = len(options)

    print(f"{message}")
    while True:
        for option in range (option_range):
            print(f"{option+1}-{options[option]}")
        
        try:
            user_choice = int(input(">"))
            
            if user_choice in range(1,option_range+1):
                print(user_choice,options[user_choice-1])
                break
            else:
                print(f"\nPlease enter a number between 1 and {option_range}")
        except:
            print("\nPlease enter an integer.") #To catch decimals and letters
