'''

    Program : Rubik's
    Author  : Maximilian Dean
    Date    : 3/1/19
    Purpose : File to import all classes for Rubik's program.

'''

import cube

def displayHeader():
    ''' For printing game title. '''

    print("RUBIK's CUBE")

def main():
    ''' Main function contain game loop. '''

    # Instantiate cube
    theCube = cube()

    # Program loop
    while True:
        print("Would you like to:\n1. Use shuffled cube.\n2. Use your own values.\n3. Use completed cube.")
        choice = input("Choice: ")

        if choice == 1:
            shuffledCube()
        elif choice == 2:
            userValues()
        elif choice == 3:
            completedCube()
        else:
            print("You must enter a 1, 2, or 3")



    def shuffledCube():
        ''' Shuffle the Cube. '''

        pass

    def userValues():
        ''' For the user to enter their own values. '''

        pass

    def completedCube():
        ''' For the user to play with a completed cube. '''

        pass

