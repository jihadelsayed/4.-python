
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
def displaysTemperature():
    for celsius in range(20):
        print("If the temperature in celsius is " + str(celsius) + " then the teperature in fahrenheit is " + str(celsiustoFahrenheit(celsius)))
# Converting from Celsius to Fahrenheit function
def  celsiustoFahrenheit(celsius):
    fehrenheit = (9/5)*celsius+32
    return fehrenheit

# Main function
def main():
    copyRight()
    displaysTemperature()

# Calling the main function
if __name__ == "__main__":
    main()