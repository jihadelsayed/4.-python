# copy right
def copyRight():
    print("""
        ____   __ __       ____  ____  __ __   ____  ___          ___  _           _____  ____  __ __    ___  ___   
        |    \ |  |  |     |    ||    ||  |  | /    ||   \        /  _]| |         / ___/ /    ||  |  |  /  _]|   \  
        |  o  )|  |  |     |__  | |  | |  |  ||  o  ||    \      /  [_ | |        (   \_ |  o  ||  |  | /  [_ |    \ 
        |     ||  ~  |     __|  | |  | |  _  ||     ||  D  |    |    _]| |___      \__  ||     ||  ~  ||    _]|  D  |
        |  O  ||___, |    /  |  | |  | |  |  ||  _  ||     |    |   [_ |     |     /  \ ||  _  ||___, ||   [_ |     |
        |     ||     |    \  `  | |  | |  |  ||  |  ||     |    |     ||     |     \    ||  |  ||     ||     ||     |
        |_____||____/      \____||____||__|__||__|__||_____|    |_____||_____|      \___||__|__||____/ |_____||_____|
        look at www.neetechs.com for more script
        """)

# Main function
def main():
    copyRight()
    print("Area of a Rectangle is: %.2f" %rectangleArea())

def rectangleArea():
    length = float(input('Enter the length of a Rectangle: '))
    width = float(input('Enter the width of a Rectangle: '))
    area = length * width
    return area
Pet Class Program
# Calling the main function
if __name__ == "__main__":
    main()