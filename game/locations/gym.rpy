define alcas = Character("Alcas", color="#1803ff")
define s = Character("Sania")
define r1 = Character("Random Gym-goer 1")
define r2 = Character("Random Gym-goer 2")
define r3 = Character("Random Gym-goer 3")
define r4 = Character("Random Gym-goer 4")
define iahb = 0
define ah1 = 0
define ah2 = 0
define ah3 = 0
define ah4 = 0


label Gym:
    show bg gym
    play music "Gym.mp3"

    "You train good"
    "You train good"
    "You train good"

    if strength == 3:
        call inAHealphyBody

    if strength == 4 and iahb == 1:
        "After training u decide to go to Sania"
        call saniaRoom


    $ strength +=1
    "You feel stronger"

    hide bg gym
    "you go home"
    stop music
    return

label park:
    $ energy = 3
    show bg park
    "you run"
    if 4 <= strength <= 6 and iahb == 2:
        call ambiguousHelp1

    if strength == 6 and ah1:
        call ambiguousHelp2

    if strength == 8 and ah2:
    call ambiguousHelp2

    if strength == 9 and ah3:
    call ambiguousHelp3

    if strength == 10 and ah4:
    call ambiguousHelp4


    "you go home"
    hide bg park
    return



label ambiguousHelp1:
    "You're on your usual run through the park, enjoying the peaceful atmosphere and the feeling of freedom that comes with each stride."
    "However, today is different. As you round a corner, you hear raised voices and the sound of a scuffle ahead."
    "Your instincts kick in, and you quicken your pace, curiosity mingling with concern as you approach the source of the commotion."
    "There, you see a man being accosted by a group of aggressors, their faces twisted in anger as they surround him."
    "The man cries out for help, his voice filled with desperation, and something inside you snaps into focus."
    "Your inner voice urges you forward, reminding you of the hours you've spent training, the strength and confidence you've built with each workout."
    " \"This is the moment\" it says. \"Your training wasn't for nothing. I need also to train my hearth\" "
    menu:
        "Go into fight":
            jump fight

        "Get out of this":
            jump parkOut

    label fight:
        "Without hesitation, you spring into action, intervening in the altercation and using your newfound strength to defend the man."
        "As you approach the scene of the altercation, you see an old man standing defiantly in front of a thug, his face a mask of determination despite his age."
        "Without hesitation, you step forward, ready to confront the thug and defend the old man."
        "After a fierce struggle, you emerge victorious, the thug defeated and slinking away in defeat."
        "As the dust settles, the old man approaches you, gratitude shining in his eyes."
        alcas "Thank you, young one. You saved me from a dire situation."
        "He offers you a drink from a nearby flask, a gesture of appreciation."
        alcas "Please, take a sip. It's the least I can do to repay you."
        "You can choose whether to accept the drink or not."
        "If you accept, [alcas] nods in approval and takes a seat on a nearby bench, motioning for you to join him."
        "You sit down, and [alcas] begins to speak, his voice filled with bitterness and resentment."
        alcas "Life... It's a cruel joke, isn't it? Full of unfairness and disappointment."
        "He launches into a tirade, regaling you with tales of woe and lamenting the injustices he's faced over the years."
        "His words are filled with bitterness and frustration, and you find yourself listening out of politeness rather than genuine interest."
        "As the sun sets in the distance, you realize that sometimes, the most unexpected encounters can lead to the most meaningful connections."

    label parkOut:
        "U calmly go to you room"

return

label ambiguousHelp2:

    "Once again, you find yourself coming to the aid of [alcas], who is in trouble yet again."
    "You face off against his assailant, determined to protect him from harm."
    "With your skill and strength, you defeat the attacker once more, ensuring [alcas]'s safety."
    alcas " \"slurring slightly\" Well, ain't you a sight for sore eyes, kid? Saved my hide again, you did."
    "He gestures towards his home, a small but welcoming abode nearby, his movements unsteady."
    alcas "Come on, let's go. I got some grub at my place. Might not be much, but it'll fill yer belly."
    show bg alcashome
    "You can sense the alcohol on his breath, but you decide to accept his offer, knowing you could use some nourishment after the intense training and exertion."
    "As you walk together, [alcas] regales you with stories, some amusing, some tragic, all tinged with the bitterness of someone who's seen too much."
    "Despite his rough exterior and occasional slurring, you find yourself drawn to [alcas]'s candid honesty and genuine gratitude."
    "At his home, he rummages through his meager supplies, offering you what little he has with a weary but sincere smile."
    "As you eat, you can't help but feel a sense of camaraderie with [alcas], grateful for the chance to share in his hospitality and bond over a shared experience of overcoming adversity."
    "After this pleasant and delicious food , u decide that u need to go already"
    hide bg alcashomes


return

label ambiguousHelp3:

    "Once again, you find yourself coming to the aid of Alcas, who seems to attract trouble wherever he goes."
    "You step in to defend him, your determination unwavering despite the familiarity of the situation."
    "With your skill and strength, you defeat the attacker once more, ensuring Alcas's safety."
    alcas  " \"gratefully\" I owe you more than I can repay, kid. But maybe this'll help."
    "He reaches into his pocket, pulling out a handful of coins, and presses them into your hand."
    alcas "It ain't much, but it's all I got. Take it."
    "You're taken aback by his gesture, unsure of what to make of the money."
    c " \"confused\" I... I don't understand, Alcas. Why are you giving me this money?"
    alcas " \"sadly\" Because you're the only one who's shown me any kindness in a long time. You're restoring a bit of hope in this broken world, kid."
    "Despite your misgivings, you accept the money, realizing that it comes from a place of genuine gratitude and desperation."
    "As you part ways with Alcas, you can't help but feel a mix of emotions, grateful for his thanks but troubled by the circumstances that led to his generosity."

return

label ambiguousHelp4:
    "As I sit down at [alcas]'s home, I notice a change in the atmosphere. Instead of the usual boasting and complaints about society, [alcas] seems more somber, as if carrying a weight on his shoulders."\
    c "Hey, [alcas], everything alright?"
    alcas " \"sights\"Yeah, just been thinking about some things lately."
    c "Anything you want to talk about?"
    alcas " \"pauses, then nods\"Yeah, actually. You know, life is such a haotic thing .Everyone say that you can change your life anytime , but it really isn’t that."
    alcas " \"hesitant\" Well, it's not a story I share often, but I suppose you deserve to know. Back in the 90s, things were different. I had dreams, Covalenco. Big dreams."
    c "What kind of dreams?"
    alcas " \"wistful\"  I wanted to be a doctor. I was top of my class, you know? Always had my sights set on making a difference in people's lives."
    alcas  " \"nods sadly\"Yeah, but then everything went to hell. '91 came along, new regime, new language, new rules. Suddenly, everything I knew was turned upside down."
    alcas  "\"grimacing\" I couldn't keep up, man. Couldn't wrap my head around the new language, didn't want to learn it either. Failed my exams, lost my shot at becoming a doctor."
    c "That must have been tough."
    alcas " \"bitter laugh\"Tough doesn't even begin to cover it. Ended up working in some factory, but that didn't last long. Then there was the drinking... lots of drinking."
    c "I'm sorry, [alcas]. That sounds rough."
    alcas  "\"waves it off\"Eh, what can you do? Life's a bitch, and then you die, right? Tried another job after that, but I was always the problem. Got fired, lost hope, lost everything."
    c "And now?"
    alcas  "\"shrugs\"Now? Now I'm just trying to survive, my friend. Begging for scraps in a city that doesn't give a damn about people like me. It's a tough world out there."
    alcas "At first, I played by their rules, begged where they told me to beg. Didn't understand the business , you know? City's like a jungle, and every street has its king. Begging was like an industry, and I was just another worker."
    c "But things changed?"
    alcas  "\"nods\"Yeah, things changed. I got older, stopped giving a damn about their system. Started begging wherever I damn well pleased. But you know what happens when you step out of line? Every night, like clockwork, there were men waiting to remind me who owned the streets."
    c  "\"reflecting silently\"It's incredible how quickly life can take a turn. One moment, you're on top of the world, dreaming of becoming a doctor. The next, you're scraping by, just trying to survive. It makes me grateful for what I have, for the opportunities I've been given. My parents survived the chaos of the '90s, and here I am, living in a time of relative peace and stability. It's easy to take it all for granted, but stories like Alcas's remind me just how fortunate I am."
    alcas "So now tell me too about yourself, every time you help me , i dont like it."
    c  "\"hesitant\"Well, [alcas], it's... it's complicated. You know, university stuff. I have exams coming up, and there's this one professor, [coj]. She's tough, really tough. I'm worried she won't let me pass."
    alcas  "\" smiling reassuringly\"Don't worry, my friend. Everything will be alright. Meet me at the park next evening, and we'll figure things out together."


return

label inAHealphyBody:

    "You enter the gym, focused on your workout regimen. As you lift weights and run on the treadmill, you notice Sania across the room, also deep in his own training."
    c "\"noticing Sania\" Hmm, that guy seems pretty serious about his workout."
    "Sania catches [c]'s glance but quickly averts his gaze, showing no interest in conversation."
    c "\"to himself\" Guess he's not the chatty type. Oh well, no harm in trying."
    "You approach Sania, hoping to strike up a conversation."
    c "Hey there, nice workout, huh?"
    "Sania barely acknowledges [c]'s presence, his focus remaining solely on his training."
    s "Mm."
    c "\"noticing Sania's lack of enthusiasm\" Well, I was just wondering if you'd like to join me for a round of arm wrestling. You seem like you'd be pretty strong."
    "At the mention of arm wrestling, Sania's demeanor changes slightly, a spark of interest igniting in his eyes."
    s "Arm wrestling, huh?"
    r1 "Yeah, let's see what you've got!"
    "However, to your surprise, Sania doesn't participate in the armwrestling himself, citing a past trauma. Instead, he encourages you to take on the other challengers."
    s "I'll sit this one out. You go ahead, show them what you're made of."
    "Despite his refusal to participate, the other guys speak highly of Sania's armwrestling skills, claiming he can beat anyone."
    r2 "Yeah, Sania's a beast at armwrestling. You're lucky he's not competing."
    "You step up to the armwrestling table, feeling a mixture of nerves and excitement as the match begins."
    c "\"determined\" Alright, let's do this."
    "After a hard-fought battle, you emerge victorious, earning the respect of the other guys at the gym."
    r3 "Whoa, nice job, man! You've got some serious strength."
    "They commend you on your strength and invite you to participate in more armwrestling games, some even offering prizes for the winners."
    r4 "Hey, we have a tournament next week. You should definitely join."
    "As the excitement dies down, Sania approaches you, a hint of a smile on his face."
    s "Not bad, not bad at all. Come visit me sometime , I live in 810A .I could teach you some tricks."
    c "\"surprised but pleased\" Sure thing, Sania. Thanks for the invite."
    "As you both head towards the dorms, you can't help but wonder what other surprises await you in this new friendship."

    $ iahb = 1

return

label saniaRoom:
    "You knock on Sania's door, hoping to continue your conversation from the gym and perhaps learn more about armwrestling."
    show bg 810A

    c "Hey, Sania, it's me again. Mind if I come in?"
    s "\"opens the door looking surprised but welcoming\" Oh, hey. Sure, come on in."
    "You enter Sania's room, noticing the various armwrestling trophies and posters adorning the walls."
    c "\"impressed\" Wow, you really are into armwrestling, huh?"
    s "\"nods\" Yeah, it's kind of my thing. So, what brings you here?"
    "You explain that you're interested in learning more about armwrestling and improving your skills."
    c "I was hoping you could give me some tips or maybe share some training techniques."
    s "\"smiles\" Of course, I'd be happy to help. Armwrestling is all about technique and strength. Let me show you a few exercises you can do to improve both."
    "Over the next hour, Sania shares his knowledge and expertise, teaching you various armwrestling techniques and showing you how to train effectively."
    s "Remember, consistency is key. Keep practicing, and you'll see improvement over time."
    s "Also remember your hearth , go for a RUN somewhere , it is really helping , both your hearth and your mind"
    c "\"grateful\" Thanks, Sania. I really appreciate you taking the time to help me out."
    s "\"shrugs\" No problem. It's always good to see someone passionate about armwrestling. Let me know if you need anything else."
    "As you leave Sania's room, you feel motivated and inspired, ready to put what you've learned into practice and dominate the armwrestling scene."

    hide bg 810A
    $ iahb = 2
return
