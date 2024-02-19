label Gym:
    show bg gym
    "You train good"
    "You feel stronger"

    hide bg gym
    "you go home"
    return

label park:
    $ energy = 3
    show bg park
    "you run"
    hide bg park
    "you go home"
    return