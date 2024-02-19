define c = Character('Covalenco', color="#ff0303")
define a = Character("Andrei Sarov", color="#1803ff")


define energy = 0
define totalday = 1
define location = ""

define strength = 0
define intelligence = 0
define charisma = 0
define sociability = 0


screen DayDisplay:
    frame:
        xpadding 40
        ypadding 20
        xalign 0.1
        yalign 0.05
        textbutton "abilities" action [ToggleScreen("DayDisplay"), Show("abilities_screen")]
    frame:
        xpadding 40
        ypadding 20
        xalign 0.5
        yalign 0.05
        text "Day Nr: [totalday]"
    frame:
        xpadding 40
        ypadding 20
        xalign 0.95
        yalign 0.05
        text "Energy : [energy]"

screen abilities_screen:
    grid 4 1:
        frame:
            vbox:
                text "Strength: [strength]"
                text "Intelligence: [intelligence]"
                text "Charisma: [charisma]"
                text "Sociability: [sociability]"
        frame:
            textbutton "Close" action [Hide("abilities_screen"), ToggleScreen("DayDisplay")] text_color "#FF0000"

label start:

    call introduction

    while totalday < 10:
        show screen DayDisplay


        $ totalday +=1
        if energy == 3:
            call morning

        if location == "uni":
            call seminarRoom
        elif location == "MassageRoom":
            call massageRoom

        if energy == 2:
            call day

        if location == "gym":
            call Gym

        if energy == 1:
            call evening

        if location == "partyRoom":
            call partyRoom
        elif location == "library":
            call library
        elif location == "park":
            call park

        show bg bedroomnight
        "You pass out"
        hide bg bedroomnight





return


label morning:
    $ energy -=1
    show bg bedroomday:
        matrixcolor TintMatrix("#ebae3490")*ContrastMatrix(1.48)*BrightnessMatrix(0.1)
    menu:
        "Go to University":
            $ location = "uni"

        "Sleep More":
            $ location = "home"
            "Ahh little extra sleep"

        "Go to Work":
            $ location = "MassageRoom"

    hide bg bedroomday
return


label day:
    $ energy -= 1
    show bg bedroomday
    menu:
        "Go to Gym":
            $ location = "gym"

    hide bg bedroomday
return


label evening:
    $ energy -= 1
    show bg bedroomevening

    menu:
        "Go Party":
            $ location = "partyRoom"
        "Do Homework":
            $ location = "library"
        "Go for a run":
            $ location = "park"

    hide bg bedroomevening
return




