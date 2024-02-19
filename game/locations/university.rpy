label seminarRoom:
        $ energy -= 1

        show bg semiarroom:
            matrixcolor TintMatrix("#ebae3480")*ContrastMatrix(1.48)*BrightnessMatrix(0.1)

        "You are listening to math classes"
        hide bg semiarroom
        show bg hallway

        "leisure time"

        hide bg hallway

        show bg semiarroom
        "You are listening to even more math classes"
        "You feel smarter"
        hide bg semiarroom

        "you go home"
        return


label library:
    show bg library
    "you go to library"
    $ energy = 3
    hide bg library
    "you go home"
    return
