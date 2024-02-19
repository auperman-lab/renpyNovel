label massageRoom:
    show bg massageroom

    "You massage some people and gain some cash"
    $ energy -= 1
    $ charisma +=1
    hide bg massageroom

    "you go home"
    return




