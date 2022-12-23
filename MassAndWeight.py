import os
os.system('color')


print(""""
 ____   __ __       ____  ____  __ __   ____  ___          ___  _           _____  ____  __ __    ___  ___   
|    \ |  |  |     |    ||    ||  |  | /    ||   \        /  _]| |         / ___/ /    ||  |  |  /  _]|   \  
|  o  )|  |  |     |__  | |  | |  |  ||  o  ||    \      /  [_ | |        (   \_ |  o  ||  |  | /  [_ |    \ 
|     ||  ~  |     __|  | |  | |  _  ||     ||  D  |    |    _]| |___      \__  ||     ||  ~  ||    _]|  D  |
|  O  ||___, |    /  |  | |  | |  |  ||  _  ||     |    |   [_ |     |     /  \ ||  _  ||___, ||   [_ |     |
|     ||     |    \  `  | |  | |  |  ||  |  ||     |    |     ||     |     \    ||  |  ||     ||     ||     |
|_____||____/      \____||____||__|__||__|__||_____|    |_____||_____|      \___||__|__||____/ |_____||_____|
look at www.swapynet.com for more script
                                                                                                              
""")


# weight = mass * 9.8
# mass in kilograms

# weight in Newtons

# keep runing the app
while(True):
    # input the value
    valuee = input("Enter the value of the mass in kilograms to calculate the object weight or type exit to exit: ")
    # check if number
    if valuee.isnumeric():
        # convert to number
        mass = int(valuee)
        # check if between 1 and 10
        if mass<1:
            # print the value
            print("your number:", number,"is not bigger or equal to one")
        else:
            weight = mass * 9.8
            print("The weight of the object is:", weight,"Newtons")
            number = None
    else:
        if valuee == "exit":
            print('\033[92m' +' Thank you for using me!'+ '\033[0m')
            break
        else:
            print(valuee, "is not a number")
    valuee = None
