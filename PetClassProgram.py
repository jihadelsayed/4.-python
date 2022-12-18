
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

# Pet class
class Pet:
    def setName(self, petName): # The setName method stores a value in the name field.
        self.petName = petName 
    def setType(self, petType): # The setType method stores a value in the type field.
        self.petType = petType 
    def setAge(self, petAge): # The setAge method stores a value in the age field.
        self.petAge = petAge 
    def getName(self): # The getName method returns the value of the name field.
        return self.petName 
    def getType(self): # The getType method returns the value of the type field.
        return self.petType 
    def getAge(self): # The getAge method returns the value of the age field.
        return self.petAge 

def addPet(petName, petType, petAge):
    # Create Object
    animal = Pet() 

    # set values
    animal.setName(petName)
    animal.setType(petType)
    animal.setAge(petAge)

    # get and print the value
    print(animal.getName() + ":" + animal.getAge() + " which is a " + animal.getType()+ " has been added")

    return animal

# Main function
def main():
    copyRight()
    listOfPets = []
    while(True):
        # create and add value to the object
        petName = input("What is the name of the pet: ")
        petType = str(input('what is his type: '))
        petAge = input('what is his age: ')
        listOfPets.append(addPet(petName, petType, petAge))
        print("____________________________________________")

        exitt = input("do you want to add more pet(yes, no):")
        print("____________________________________________")

        if(exitt =="no"):
            break

    print("The Registered animal are:")
    for pet in listOfPets:
        print( pet.petName, pet.petType, pet.petAge, sep =' ' )


# Calling the main function
if __name__ == "__main__":
    main()



