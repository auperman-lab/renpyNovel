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

        $ intelligence += 1

        "you go home"
        return


label library:
    show bg library
    "you go to library"
    $ energy = 3
    hide bg library
    "you go home"
    return


label exam:
    show bg courseroom
    "Exam Day!"
    define correctAnswer = 0

    menu:
        "Problem 1"
        "State the initial value problem, with initial condition imposed at t0 = 0, having implicit solution y*e^y +t^2 = sin t"
        "y = 0":
            jump problem2
        "y = t":
            jump problem2
        "y = e^t+t":
            jump problem2
        "y = 1":
            jump problem2
        "y = t^x + e":
            jump problem2
        "Friend help":
            if sociability == 10:
                $ correctAnswer +=1
                "Oh i know this problem ,I did it with [max] when preparing for exam"
                jump problem2
            else:
                "Sad i dont have someone to study with(("
                jump problem2


    label problem2:
    menu:
        "Problem 2"
        "Solve the diferential equation: y' = x*e^(-sin(x)) - y*cos(x)"
        "y = 0":
            jump problem3
        "y = e^(x+sin(x))":
            jump problem3
        "y = sin(x)":
            jump problem3
        "y = cos(x)":
            jump problem3
        "I dont know":
            jump problem3
        "Friend help":
            if sociability == 10:
                $ correctAnswer +=1
                "Oh i know this problem ,I did it with [max] when preparing for exam"
                jump problem3
            else:
                "Sad i dont have someone to study with(("
                jump problem3

    label problem3:
    menu:
        "Problem 3"
        "Find Symetric equations for the line of inntersection of the planes 5x-2y-2z = 1"
        "y+x+z = 0":
            jump problem4
        "y^2+x = 3":
            jump problem4
        "z+x+x^2 = pi":
            jump problem4
        "I dont know":
            jump problem4
        "I dont know":
            jump problem4
        "Friend help":
            if sociability == 10:
                $ correctAnswer +=1
                "Oh i know this problem ,I did it with [max] when preparing for exam"
                jump problem4
            else:
                "Sad i dont have someone to study with(("
                jump problem4

    label problem4:
    menu:
        "Problem 4"
        "Determine whether the planes are parallel , perpendicular, or neither. If neither find the angle between them"
        "I dont know":
            jump problem5
        "perpendicular":
            jump problem5
        "neither(34 degrees)":
            jump problem5
        "I dont know":
            jump problem5
        "I dont know":
            jump problem5
        "Friend help":
            if sociability == 10:
                $ correctAnswer +=1
                danu "I will help u here"
                jump problem5
            else:
                "Sad that i dont have friends"
                jump problem5


    label problem5:
    menu:
        "Problem 5"
        "Evaluate the line integral F over C (xyz^2)dS, where C is line segment from (-1,5,0) to (1,6,4)"
        "I dont know":
            jump result
        "I dont know":
            jump result
        "I dont know":
            jump result
        "I dont know":
            jump result
        "I gues i know":
            jump result
        "Friend help":
            if sociability == 10:
                $ correctAnswer +=1
                danu "I will help u here"
                jump result
            else:
                "Sad that i dont have friends"
                jump result

    label result:
        if correctAnswer == 5:
            hide courseroom
            call ending1

        if ah5 == 1:
            hide courseroom
            call ending2

        if charisma >=9:
            hide courseroom
            call ending3

        if intelligence>=9:
            hide courseroom
            call ending4

        if correctAnswer != 5 and ah5 == 0 and charisma < 9 and intelligence <9:
            hide courseroom
            call ending5

return

label ending1:
    "Good job You got First Ending"
    "You are really a good person , and very friendly one also, keep going"
return

label ending2:
    "Good job You got Second Ending"
    "You big boy , you got muscles , but the most important muscle for you is your hearth"
return

label ending3:
    "Good job You got Third Ending"
    "Such hannds, goldenn hands , even others see that , feel that "
return

label ending4:
    "Good job You got Forth Ending"
    "Who are you ,why are you even here , no one should do it, it is boring"
    "Sorry that , it should be romannce route , but i cant write romace ,really, more time , better product!"
return

label ending5:
    "Bad job You got Fiftieth Ending"
    "You are really mediocre, sorry , Bostan said to you this already, but , at Software Engineering you need to evidentiate yourself(("
return