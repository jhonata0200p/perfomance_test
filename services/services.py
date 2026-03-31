
#Scalable interactive menu that uses a list with the options
def getOption (options):
    
    while True:
        for i, option in enumerate(options, start=1):
            print(f"{i} - {option}")
        
        try:
            choice = int(input("Enter de option \n"))

            if choice < 0:
                print("the option cannot be negative, please try again")
                continue
        
            else:
                return choice
        
        except ValueError:
            print("select a valid option, try again")
            continue

