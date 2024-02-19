# import renpy.random


define danu = Character("Danu Macrii")
define fool = Character("Fool")

label partyRoom:
    show bg partyroom
    "you party, till morning"
    $ energy = 2
    $ sociability += 1

    if sociability == 3 :
        call pokerEvent

    if sociability == 6 :
        call kitchenIncident

    label common:
        "you go home"
        hide bg partyroom
return

label kitchenIncident:

    $ maxEvent1 = 0
return

label pokerEvent:
    "You find yourself at another lively dorm party, the sounds of laughter and music filling the air. Amidst the crowd, a group of friends invites you to join a game of poker."
    "Friend1" "Hey Covalenco, you in for some poker?"
    "You check your wallet, finding that you have enough money to join the game."

    menu:
        "Yeah sure":
            jump choicepoker1

        "No , i dont have the money":
            jump commonPokerEnd

    label choicepoker1:
        c "Yeah, sure, why not? Lead the way."

    "With a nod of agreement, you follow your friends as they make their way to the Poker Room, ready for a night of fun and excitement."

    show bg pokerroom


    "You enter the dimly lit Poker Room, the atmosphere heavy with anticipation. Five figures sit around the table, their faces partially obscured by shadows."
    "At the front of the desk, dealing the cards, is [danu], the dealer, while the other players are positioned opposite, surrounding the edges of the table."
    "You take a seat between the Poker Players and [danu] ready to join in the game."
    c "Alright, let's play."
    "With a shuffle of cards and a flick of the wrist, Danu begins dealing the hand, setting the stage for an intense game of poker."
    "As the first few rounds progress, you decide to pass, observing the reactions of the other players."
    "Frustration fills the air as the Poker Players berate the dealer, blaming him for the poor hands they've been dealt."
    "Poker Player 1" "What is this garbage? These cards are crap!"
    "Poker Player 2" "Yeah, [danu], what are you trying to pull here?"
    "Danu Macrii, the dealer, simply smiles in response to their complaints, unfazed by their accusations."
    danu "Just luck of the draw, my friends. You win some, you lose some."
    "In the next round, the [fool] wins a significant prize, gleefully handing over a portion to [danu] as a token of appreciation."
    fool "Here you go, [danu], 5 percent for good luck. Thank the Karma, guys!"
    "The other players react with skepticism and disagreement, clearly not convinced by the Fool's words."
    "Poker Player 3" "Come on, that's nonsense. Luck has nothing to do with it."
    "Poker Player 4" "Yeah, we make our own luck at this table."
    "Despite the dissenting opinions, the game continues, tensions running high as the players vie for victory."
    "As the [fool] storms out in frustration after losing all his money, the atmosphere in the room turns hostile."
    "The remaining players, fueled by their own ego, begin to mock and bully him for his losses and his belief in tipping the dealer for luck."
    "Poker Player 1:" "Looks like someone's luck finally ran out! Maybe next time, don't waste your money tipping the dealer for luck!"
    "Poker Player 2" "Yeah, what were you thinking, [fool]? You should know better than to believe in that nonsense!"
    "The [fool], visibly shaken by the barrage of insults, clenches his fists in anger but remains silent, realizing the folly of his actions."
    fool " \"muttering to himself\" I can't believe I fell for that..."
    "As the tension in the room mounts, you observe the scene, silently grateful for your decision to play the game with integrity and without relying on superstition."
    "As the game progresses, you find yourself with a winning hand in the next round. You pause, contemplating whether to offer a bribe to [danu], the dealer, who continues to wear his enigmatic smile."
    c " \"internal monologue\" Should I slip a little something to [danu], for luck?"
    c "Nah, I'll let fate decide."
    "Covalenco locks eyes with Danu, the dealer, and is met with a gaze that seems to convey a silent message of encouragement and support. In that moment, Covalenco feels a surge of confidence, as if the dealer is silently urging him to take a chance and go all in."
    "In the next round, you go all in, risking nearly all of your remaining chips on the hand. The tension in the room is palpable as the cards are revealed, but to your relief and elation, you emerge victorious."
    "With a triumphant grin, you turn to [danu], reaching into your pocket to retrieve a generous tip."
    c "Thanks for the luck, [danu]. This one's for you."
    "Danu accepts the tip with a nod and a knowing smile, the gold in his eyes seeming to glimmer with satisfaction. The other players watch in awe as your bold move pays off, impressed by your daring and skill."
    "The Fool, consumed by rage and frustration, directs his anger towards Danu, the dealer, accusing him of deceit and manipulation."

    fool "You motherfucker!"

    "[danu], unfazed by the outburst, interrupts with a smirk."

    danu "You got that right.))(your mother)"

    "The [fool] continues, his accusations growing more vehement as he accuses [danu] of trickery and collusion."

    fool "You tricked me, you tricked all of us! I've seen those eyes, I know [c] is your man and you changed the cards, fucking cheater! Let's get him, boys!"

    menu:
        "Help [danu]":
            jump choicehelpdanu1

        "Stay silent":
            jump choicehelpdanu2


    label choicehelpdanu1:
        "Covalenco steps forward, facing the enraged Fool with a determined expression."
        c "There's no fucking chance, [fool]. I just got lucky, that's all. This is my first time meeting [danu], and I won fair and square."
        "The Fool scoffs sarcastically, his disbelief evident in his tone."
        fool "Yeah, like my luck."
        "The other players exchange uneasy glances, unsure of whom to believe. The [fool]'s accusations hang in the air, casting a shadow of doubt over the room."
        fool "He... He looked at me all night in the party room like he wants something from me, and I approached him."
        "[danu] steps forward, his expression smug as he confirms the [fool]'s suspicions."
        danu "Yes, of course, I helped him. He said he'd give me half of the prize."
        "Before anyone can react, [danu] swiftly exits the room, disappearing into the corridor. Chaos erupts as the other players confront me, accusing me of colluding with the dealer. In the midst of the commotion, I attempt to sneak away with my winnings, but I am caught by the others, who seize the money and deliver a punishing blow."
        hide bg pokerroom
        show bg bedroomnight
        "After the chaotic events in the Poker Room, I retrieve what's left of my winnings and quickly exit the room, eager to escape the tension and conflict. I navigate through the dimly lit corridors of the dormitory, my mind buzzing with a mix of adrenaline and uncertainty. The echoes of angry voices fade into the distance as I finally reach the familiar comfort of my own room."
        hide bg bedroomnight
        show bg bathroom
        "After the tumultuous events of the poker game, I seek solace in the bathroom, craving a moment of quiet reflection before retiring for the night. As I step into the familiar space, a sense of calm begins to wash over me, easing the tension in my shoulders."
        "My peace is shattered when I lay eyes on [danu], standing silently in the dimly lit room."
        "Startled by the unexpected encounter, I stand frozen as [danu] casually retrieves the amount of money I had entered the game with and hands it over to me."
        danu "What a great night, huh? So many emotions... fun, lies, hope, disappointment, betrayal. This is why I play with people."
        danu "I've never seen someone like you before. No one has ever tried to save my ass like that. Why are you even doing this?"
        "Caught off guard by Danu's unexpected question, I freeze, my mind racing as I struggle to find the right words to respond."
        c "Uh... I guess I just couldn't stand by and watch someone get unfairly accused like that."
        "Danu's gaze intensifies as he continues, his words taking on a cryptic tone."
        danu "[c], studying at Software Engineering at TAEM. Good boy. I'll help you sometime."
        "My eyes widen in astonishment as [danu] casually reveals personal details about me. A mix of confusion and curiosity fills my mind as I grapple with the implications of his words. I hesitate, unsure of what to make of this enigmatic encounter, and decide to probe further."
    label choicehelpdanu2:
        "As I witness the escalating tension in the poker room, I hesitate as the [fool] launches a punch at [danu]. The room erupts into chaos, but amidst the confusion, [danu]'s smile remains unnervingly intact."
        fool "You cheating scumbag! This is for tricking us!"
        "[danu], unfazed by the blow, calmly retrieves the money he earned from the game and places it on the table. With a calculated move, he reveals the hidden cards taped under the table, exposing the deceit that tainted the game."
        danu "Looks like someone tried to stack the deck. Shame on you."
        "I watch in disbelief as the tables turn, the Fool's bravado crumbling in the face of Danu's revelation. The other players, realizing they've been duped, turn their fury on the Fool, delivering swift retribution for his deceit."
        "Player 1" "You lying cheat! How dare you!"
        "As the room descends into chaos, [danu] slips away unnoticed, leaving me to fend for myself. Before I can make my escape, I'm cornered by the enraged players, who unleash their anger on me, leaving me battered and bruised, with my hard-earned winnings slipping through my fingers."

    label commonPokerEnd:

        "You feel exhausted and go to your room"

return