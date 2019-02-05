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

        displayHeader()
        print("Would you like to:\n1. Use shuffled cube.\n2. Use your own values.\n3. Use completed cube.")
        choice = input("Choice: ")

        if choice == 1:
            theCube.shuffle()
        elif choice == 2:
            userValues()
        elif choice == 3:
            theCube.restore()
        else:
            print("You must enter a 1, 2, or 3")

    def userValues():
        ''' For the user to enter their own values. '''

        # Dictionairies for holding square colours for each side on cube.
        white = {}
        red = {}
        yellow = {}
        orange = {}
        green = {}
        blue = {}

        # Gather colours for white side
        print("With white facing forward and blue facing up, enter the color of each square on white side in the following order;")
        for i in range(8):
            print(i+".", end ="")
            white.update({i:input("Colour: ")})

        # Gather colours for red side
        print("Do the same with red forward and blue up: ")
        for i in range(8):
            print(i+".", end ="")
            red.update({i:input("Colour: ")})

        # Gather colours for yellow side
        print("Do the same with yellow forward and blue up: ")
        for i in range(8):
            print(i+".", end ="")
            yellow.update({i:input("Colour: ")})

        # Gather colours for orange side
        print("Do the same with orange forward and blue up: ")
        for i in range(8):
            print(i+".", end ="")
            orange.update({i:input("Colour: ")})

        # Gather colours for green side
        print("Do the same with green forward and white up: ")
        for i in range(8):
            print(i+".", end ="")
            green.update({i:input("Colour: ")})

        # Gather colours for blue side
        print("Do the same with blue forward and yellow up: ")
        for i in range(8):
            print(i+".", end ="")
            blue.update({i:input("Colour: ")})


