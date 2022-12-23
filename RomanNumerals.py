# input number between 1 and 10

# Display roman numeral of that number

# if outside of the range display error
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

## array of roman numbers
romanNumber = [
 "I",
 "II",
 "III",
 "IV",
 "V",
 "VI",
 "VII",
 "VIII",
 "IX",
 "X",
]
# keep runing the app
while(True):
    # input the value
    valuee = input("Enter a number between 1 and 10 and type exit to exit: ")
    # check if number
    if valuee.isnumeric():
        # convert to number
        number = int(valuee)
        # check if between 1 and 10
        if number>10 or number<1:
            # print the value
            print("your number:", number,"is not between 10 and 1")
        else:
            print("your selected number in roman numerals is:", romanNumber[number-1])
            number = None
    else:
        if valuee == "exit":
            print("Thank you for using me!")
            break
        else:
            print(valuee, "is not a number")
    valuee = None
