define nic = Character("Nichita")
define f = Character("Fifa")
define coj = Character("Cojuhari")

play music "Massage.mp3"

label massageRoom:
    show bg massageroom

    "You massage some people and gain some cash"
    $ energy -= 1
    $ charisma +=1


    if charisma == 3 :
        call bigGuy

    "you go home"
    hide bg massageroom


    return

label bigGuy:
    "As you work in the massage room, a student named Nichita enters. Despite his large frame, you sense strength beneath the layers of fat."
    "He lays on the massage table, silent and seemingly lost in thought."
    c "Would you like me to use professional gloves or just my hands?"
    nic "Hands will be fine."
    "There's a long silence before Nichita speaks up, asking about you."
    nic "So, [c], what's your story?"
    c "Well, I'm a student at TAEM, like you. I don't go to classes much. I'm starting to think massage might be my calling."
    nic "Ah, I see. Yeah, university life can be pretty overwhelming sometimes. I'm Nichita, by the way. I'm also at TAEM."
    "You nod, grateful for the chance to connect with someone who understands."
    c "Nice to meet you, Nichita. Yeah, dorm life isn't exactly what I expected."
    nic "Tell me about it. It's like living in a circus sometimes. But hey, at least we're all in the same boat, right?"
    "You chuckle at his analogy, realizing that you're not alone in your struggles."
    c "True. It can be chaotic, but there's a certain camaraderie among dorm mates."
    nic  "Absolutely. Speaking of which, how's your experience been in the dorms so far?"
    c  "It's been... interesting, to say the least. I've met some characters, that's for sure."
    nic "I hear you. You never know what to expect. But hey, that's part of the adventure, right?"
    "You nod, appreciating Nichita's optimism despite the challenges of dorm life."
    c "Definitely. It's all part of the experience."
    nic "You know, if you ever want to improve your skills, I could help. Or maybe just talking to different students in my room could give you some insight."
    "You're touched by his offer of assistance and realize that perhaps there's more to learn about massage therapy than you initially thought."
    "As you continue to chat, Nichita suddenly interrupts, praising your massage skills and the quality of the oils you use."
    nic  "Hey, [c], I have to say, you're really good at this. The oils you use are top-notch, and your technique is impressive."
    "You smile gratefully, but inwardly, you feel a pang of doubt. Despite the praise, you know that there's more to being a massage therapist than just the physical techniques."
    c "Thanks, Nichita. I appreciate that. I try my best."
    "Nichita nods, sensing your hesitation, before offering his help."
    c "You might be onto something there, Nichita. I've been focusing so much on the physical aspect of massage, but maybe I need to understand my clients better too."
    "You appreciate the importance of connecting with others, realizing that it's not just about the physical techniques, but also about understanding the needs and preferences of your clients."



return


label complicatedMadam:

    f "Ugh, girl, you won't believe what happened at the party last night! It was insane!"

    "Fifa puts her things away, leaving her phone on the table, and gets on the Massage Table, still chatting away."

    "You start massaging, trying to concentrate, but Fifa continues to talk and move around."

    f "Oh my gosh, I know, right? It was like, the craziest thing ever!"

    "You try to focus on your work, but [f]'s constant chatter is distracting."

    f "What is this? I didn't pay for a massage just to feel more stressed! This is terrible! The last masseuse I had was so much better!"

    "You try to remain calm, but [f]'s harsh words sting."

    menu:
        "Respond calmly and accepting":
            jump calmResponse1

        "Respond aggressively":
            jump aggressiveResponse1

    label calmResponse1:
        c "I'm sorry to hear that you're not satisfied, ma'am. Is there anything specific you'd like me to adjust?"
        f "Can you believe this? I can't even relax for a minute! Ugh, I should've gone somewhere else."
        jump madamCommon1


    label aggressiveResponse1:
        c "Listen, lady, if you're not happy, you can leave. I don't need to deal with this kind of attitude."

        f "Can you believe this? I can't even relax for a minute! Ugh, I should've gone somewhere else."
        jump madamCommon1

    label madamCommon1:
        "..."
        "..."
        "..."
        f "Um, can you please wear gloves? My skin is really sensitive."
        "You comply with [Fifa]'s request and put on the gloves, adjusting your approach to accommodate her sensitivity."


    menu:
        "Respond calmly and accepting":
            jump calmResponse2

        "Respond aggressively":
            jump aggressiveResponse2

    label calmResponse2:
        c "Of course, ma'am. I'll be happy to accommodate your request."
        jump afterCalmResponse2

    label aggressiveResponse2:
        c "Seriously? You're complaining about my touch now? Fine, I'll wear gloves, but don't expect the same level of massage."
        f "Forget it. I don't need this kind of treatment. I'm leaving."
        jump madamOut


    label afterCalmResponse2:
        "..."
        "..."
        "..."
        f "You know what? Actually, I think without the gloves might be better. But honestly, overall, this massage isn't great."

    menu:
        "Respond calmly and accepting":
            jump calmResponse3

        "Respond aggressively":
            jump aggressiveResponse3

    label calmResponse3:
        c "I appreciate your feedback, ma'am. I'll do my best to improve and make sure you have a better experience next time."
        call afterCalmResponse3

    label aggressiveResponse3:
        c "Are you serious? First, you complain about my touch, now you're changing your mind? Make up your mind already!"

        f "Wow, I was just trying to help. Forget it. This whole experience has been a disaster."
        jump madamOut


    label afterCalmResponse3:
        "..."
        "..."
        "..."

        f "This is not how my last boyfriend did it! Why can't you just do it right? Why no one is like him , why , everyone is so stupid , no one understands me"

    menu:
        "Respond calmly and accepting":
            jump calmResponse4

        "Respond aggressively":
            jump aggressiveResponse4

    label calmResponse4:
        c "Hey, hey, it's okay. Let's take a deep breath, alright? I understand you're upset, but let's try to talk this out."

        "You approach Fifa slowly, speaking softly to calm her down. As she begins to sob, you gently embrace her, offering comfort and reassurance."

        c "It's alright, Fifa. Everything's going to be okay. I'm here for you."

        "Your calm demeanor and kind words help to soothe [Fifa]'s emotions, and she gradually relaxes in your arms, grateful for your understanding."
        jump out


    label aggressiveResponse4:
        c "You know what? I'm done with this. Get out of my massage room!"

        f "Fine! I don't need this crap! I'll find someone who knows what they're doing!"
        jump madamOut

    label madamOut:
        "[f] is leaving the saloon , u understand that u will have even less money"

    label out:
        "You get out he work place"

return

label unsatisfiedTeacher1:

    "At a random day near Midterm1 at the Massage Room, [coj] arrives. She behaves elegantly, putting all her clothes in a locker, as if it's not her first time doing so, and proceeds to the massage desk."

    coj "Good afternoon. I'm here for my massage appointment."

    "She strides confidently towards the massage desk, not seeming to recognize you."

    "You quietly observe [coj]'s actions, noting her familiarity with the routine."

    "You watch [coj] silently, feeling a mix of nervousness and curiosity. You approach the massage table cautiously, trying to remain calm despite the tremor in your hands."

    "As you begin the massage, you notice [coj]'s relaxed demeanor, realizing that she likely doesn't recognize you as one of her students who rarely attends lectures. Your nerves gradually subside as you focus on your task, allowing you to massage with more confidence and composure."

    "Now more composed, you focus intently on your work, ensuring each movement is precise and soothing. Suddenly, you hear [coj] let out a soft moan of pleasure, followed by a quick apology."

    coj "Oh, excuse me. That felt wonderful."

    "You are taken aback by the unexpected reaction, but you accept the compliment graciously."

    "You continue with renewed confidence, determined to provide the best experience possible for [coj]."

    "After an hour of blissful relaxation, [coj] rises from the massage table, feeling rejuvenated. She turns to you with a smile, her eyes sparkling with a hint of flirtation."

    coj "Thank you, Covalenco. That was truly wonderful. Perhaps I'll have to come back again sometime soon."

    "Her tone is playful, and there's a subtle twinkle in her eye as she speaks."

    c "I'm glad you enjoyed it, ma'am. You're always welcome back anytime."

    "As [coj] leaves, you breathe a sigh of relief, feeling a mix of emotions."

    c "Thank goodness she doesn't recognize me."

    "You murmur quietly to yourself, grateful for the anonymity that allowed you to provide a professional massage without the pressure of being recognized as one of her students."

    "With a sense of relief washing over you, you gather your thoughts and begin tidying up the massage room, reflecting on the unexpected encounter with the rector."

return

