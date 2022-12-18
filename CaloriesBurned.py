
# copy right
def copyRight():
    print(""""
        ____   __ __       ____  ____  __ __   ____  ___          ___  _           _____  ____  __ __    ___  ___   
        |    \ |  |  |     |    ||    ||  |  | /    ||   \        /  _]| |         / ___/ /    ||  |  |  /  _]|   \  
        |  o  )|  |  |     |__  | |  | |  |  ||  o  ||    \      /  [_ | |        (   \_ |  o  ||  |  | /  [_ |    \ 
        |     ||  ~  |     __|  | |  | |  _  ||     ||  D  |    |    _]| |___      \__  ||     ||  ~  ||    _]|  D  |
        |  O  ||___, |    /  |  | |  | |  |  ||  _  ||     |    |   [_ |     |     /  \ ||  _  ||___, ||   [_ |     |
        |     ||     |    \  `  | |  | |  |  ||  |  ||     |    |     ||     |     \    ||  |  ||     ||     ||     |
        |_____||____/      \____||____||__|__||__|__||_____|    |_____||_____|      \___||__|__||____/ |_____||_____|
        look at www.neetechs.com for more script
        """)
# Displays a table function
def displaysCalories():
    # 10, 15, 20, 25, 30
    for minute in range(5,35,5):
        print("On " + str(minute) + " Minutes. You have burned " + str(calculateCalories(minute)) + " calories.")

# Converting from Celsius to Fahrenheit function
def  calculateCalories(timePerMinute):
    CaloriesPerMinute = 3.9
    calculatedCalories = CaloriesPerMinute * timePerMinute
    return calculatedCalories
    
# Main function
def main():
    copyRight()
    displaysCalories()

# Calling the main function
if __name__ == "__main__":
    main()




