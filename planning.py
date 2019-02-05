'''

    APPROACH 1

        List / Dictionary

            > Keys = 1 to 6
            > when the color of the current working side is passed, it becomes 1
            > Front = 1
            > Left  = 2
            > Right = 3
            > Up    = 4
            > Down  = 5
            > Back  = 6

            > Yellow    || White    as Front = Blue     as Up
            > Red       || Orange   as Front = Yellow   as Up
            > Green     || Blue     as Front = White    as Up

    APPROACH 2

        > Label each side a Front, back, up etc...
        > F = White     / U = 
        > F = Yellow    / U =
        > F = Blue      / U =
        > F = Green     / U =
        > F = Orange    / U =
        > F = Red       / U =

    Rotate a side:

        > 1 = 6
        > 2 = 4
        > 3 = 1
        > 4 = 7
        > 5 = 2
        > 6 = 8
        > 7 = 5
        > 8 = 3

    DEFINING INPUT COMMANDS

        > R     = Right clockwise
        > Ri    = Right anti-clockwise
        > L     = Left clockwise
        > Li    = Left anti-clockwise
        > F     = Front clockwise
        > Fi    = Front anti-clockwise
        > B     = Back clockwise
        > Bi    = Back anti-clockwise
        > U     = Up clockwise
        > Ui    = Up anti-clockwise
        > D     = Down clcokwise
        > Di    = Down anti-clcokwise

    OUTPUT IDEAS

          X
        X X X X
          X

                X X X
                X B X
                X X X

                X X X
                X U X
                X X X

        X X X   X X X   X X X
        X L X   X F X   X R X
        X X X   X X X   X X X

                X X X
                X D X
                X X X



    GENERAL IDEAS

        > Allow user to input which side they would like to be facing
            > Don't show the back side as to not confuse the user

        > Promt
            > Would you like:
                1. Shuffle cube
                2. Enter your own values
                3. Play with a completed cube
            > Which side foreward:
                1. Front
                2. Back
                3. Left
                4. Right
                5. Up
                6. Down
            > Turn clockwise or anti-clockwise? C/a:

'''

