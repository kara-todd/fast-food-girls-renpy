# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define cindi = Character("Cindi")
define me = Character("[playername]")
define anon = Character("???")
define haySushi = Character("Hayashi Sushi")
define phone = anon
define girl = anon
define gave_angname = False
define gave_cindiname = False
define gave_blyname = False
define gave_domname = False
define cindiDate = False
define cindidateact = "nothing"
define date = False

label sushi1_start:
    show char cindi neutral1:
        xalign 0.5
        yalign 0.75
    with dissolve

    girl "Hi! did you order a Chef’s Deluxe Assorted Plate and a seaweed salad?"
    me "Yeah, that was me."
    girl "Okay, great. That'll be $30."
    me "Here you go, keep the change."

    show char cindi neutral2:
        xalign 0.5
        yalign 0.75
    with dissolve

    girl "Wow, look at you big spender. Thanks!"

    menu:
        "You deserve it.":
            jump sushi1_hardworker

        "Can I ask you a question?":
            jump sushi1_question1

        "You're welcome!":
            jump sushi1_end1

    label sushi1_hardworker:
        me "You deserve it for being such a hardworker."
        girl "Well, that is very sweet of you to say. I appreciate your... appreciation."
        me "You're welcome."
        girl "Alright, well, enjoy the sushi! I hope you have a good night!"

        menu:
            "Can I ask you a question?":
                jump sushi1_question1

            "I hope you have a good night too.":
                jump sushi1_end2

            "Are you sure you have to go now?":
                jump sushi1_todo

    label sushi1_end1:
        me "You're welcome! Have a good night!"
        girl "You too!"

        hide char cindi neutral2

        jump review_sushi1

    label sushi1_end2:
        me "I hope you have a good night too. Maybe I'll see you again soon."
        girl "If you order enough sushi, I'm sure you will. Good night!"

        hide char cindi neutral2
        with dissolve

        jump review_sushi1

    label sushi1_todo:
        me "Are you sure you have to go now? This is a lot more sushi than I expected. There's plenty to share."
        girl "I'm kind of on the clock and there are a lot of hungry people waiting on me. I'm sorry. But thanks for the offer. Maybe another time."
        me "How about tomorrow night?"
        girl "Are you asking me out right now? You don't even know my name yet."
        me "Yeah, I'm sorry. I'm getting ahead of myself. I just thought you were cute and interesting and I didn't want to miss my chance."
        girl "Well, that's pretty nice, I guess. But I still gotta say no for now. Maybe after we get to know each other a little more. Good night, Romeo."

        menu:
            "Wait, give me another chance.":
                jump sushi1_secondchance

            "Good night, Juliet!":
                jump sushi1_end3

    label sushi1_end3:
        me "Good night, Juliet! I'll see you soon!"
        girl "Hopefully not too soon. I'd hate for us to have a tragic ending as well."

        hide char cindi neutral2
        with dissolve
        jump review_sushi1

    label sushi1_secondchance:
        me "Wait, give me another chance. Please."
        girl "Alright. You get one more chance."
        me "What's your name?"
        girl "It's Cindi. What's yours?"
        cindi "It's Cindi. What's yours?"

        menu:
            "It's [playername].":
                $ gave_cindiname = True
                jump sushi1_samename2

            "It's [angname]." if gave_angname:
                $ gave_cindiname = True
                jump sushi1_angcindi2

            "It's [domname]." if gave_domname:
                $ gave_cindiname = True
                jump sushi1_domcindi2

            "It's [blyname]." if gave_blyname:
                $ gave_cindiname = True
                jump sushi1_blycindi2

            "Give a new name":
                $ gave_cindiname = True
                jump sushi1_newname2

    label sushi1_samename2:
        python:
            cindiname = playername.strip()
        me "It's [cindiname]."
        jump sushi1_reward

    label sushi1_angcindi2:
        python:
            cindiname = angname.strip()
        me "It's [cindiname]."
        jump sushi1_reward

    label sushi1_blycindi2:
        python:
            cindiname = blyname.strip()
        me "It's [blyname]."
        jump sushi1_reward

    label sushi1_domcindi2:
        python:
            cindiname = domname.strip()
        me "It's [domname]."
        jump sushi1_reward

    label sushi1_newname2:
        python:
            cindiname = renpy.input("What name would you like to give?")
            cindiname = cindiname.strip()
            hascindiName = True

            if not cindiname:
                hascindiName = False
                cindiname = playername.strip()
        me "It's [cindiname]."
        jump sushi1_reward

    label sushi1_reward:
        cindi "Hmm, [cindiname]. Nice to meet you too. But you still asked me out before you asked for my name and I don’t know if I want to reward that kind of behavior."

        menu:
            "What if I invited you to a picnic and rollerskating?":
                jump sushi1_rollerskates

            "What if I invited you out to some drinks?":
                jump sushi1_drinks2

            "After you taste my food, you might change your mind.":
                jump sushi1_chef

            "What if I asked you a few more questions?":
                jump sushi1_question2

    label sushi1_drinks2:
        me "What if I offered to take you to your favorite bar or club and buy the drinks while we get to know each other a bit more."
        cindi "As much as I enjoy going to breweries. I'm not sure. It sounds like you might just want to get me drunk, not really get to know me."
        me "I definitely said I wanted to get to know you a bit more."
        cindi "Then why don't you get to know me now?"

        menu:
            "Tell me about yourself.":
                jump sushi1_end4

            "

    label sushi1_rollerskates:
        me "Alright. But what if I were to, say, invite you to a romantic but fun dinner in the park? There might even be rollerskates involved."
        cindi "I'm not really a rollerskates and picnic kind of girl."
        me "What kind of girl are you?"
        cindi "If I had to put myself in a box, I guess I'd say I'm more of an art gallery and craft brewery connoisseur."
        me "Well, I haven't yet made the picnic so I guess we could take our date elsewhere. I think I've heard of a show going on tomorrow night."
        cindi "Strange. I hadn't heard of one."
        me "All the more reason for you to join me then."
        cindi "Hmm... I am intrigued. If you know of a show that I haven't heard about, then you must be pretty interested in art."
        cindi "Alright. What time should we meet?"
        me "How about here, tomorrow at 6pm. We can drive together."
        cindi "Alright. It's a date."
        me "Great! I will see you then."

        $ dateCindi = True
        $ date = True
        $ datecindiact = "get some drinks"

        hide char cindi neutral2
        with dissolve
        jump review_sushi1

    label sushi1_question1:
        me "Can I ask you a somewhat strange question?"
        girl "You've already asked me a strange question but sure. Can't promise I'll answer it though."
        me "You look really familiar. What's your name?"
        girl "It's Cindi. What's yours?"
        cindi "It's Cindi. What's yours?"

        menu:
            "It's [playername].":
                $ gave_cindiname = True
                jump sushi1_samename

            "It's [angname]." if gave_angname:
                $ gave_cindiname = True
                jump sushi1_angcindi

            "It's [domname]." if gave_domname:
                $ gave_cindiname = True
                jump sushi1_domcindi

            "It's [blyname]." if gave_blyname:
                $ gave_cindiname = True
                jump sushi1_blycindi

            "Give a new name":
                $ gave_cindiname = True
                jump sushi1_newname

    label sushi1_samename:
        python:
            cindiname = playername.strip()
        me "It's [cindiname]."
        jump sushi1_why

    label sushi1_angcindi:
        python:
            cindiname = angname.strip()
        me "It's [cindiname]."
        jump sushi1_why

    label sushi1_blycindi:
        python:
            cindiname = blyname.strip()
        me "It's [blyname]."
        jump sushi1_why

    label sushi1_domcindi:
        python:
            cindiname = domname.strip()
        me "It's [domname]."
        jump sushi1_why

    label sushi1_newname:
        python:
            cindiname = renpy.input("What name would you like to give?")
            cindiname = cindiname.strip()
            hascindiName = True

            if not cindiname:
                hascindiName = False
                cindiname = playername.strip()
        me "It's [cindiname]."
        jump sushi1_why

    label sushi1_why:
        cindi "Hmm, [cindiname]. Nice name but I don't think I know you."

        menu:
            "I don't think we've met after all.":
                jump sushi1_goodbye2

            "Did you grow up around here?":
                jump sushi1_growup

            "You look familiar. Are you an artist?":
                jump sushi1_artist

    label sushi1_goodbye2:
        me "I don't think we've met after all. But it's nice to meet you."
        cindi "Well, now that we've gotten that cleared up, I should probably get back to work."
        me "I hope the rest of your night goes well!"
        cindi "Thanks, I hope yours does too!"

        hide char cindi neutral2
        with dissolve

        jump review_sushi1

    label sushi1_growup:
        me "Maybe not. Did you grow up around here?"
        cindi "Yeah. My uncle actually owns the restaurant."
        me "Wow. A family business. Have you worked for them most of your life?"
        cindi "Most of it, yeah."
        me "Do your parents like that you're still working at the family business?"
        cindi "Well, it's not really the family business. They don't work there."
        cindi "I think they really hoped I'd get some high up corporate marketing job with my degree. But here I am, still at the restaurant. So yeah, there's a little disappointment."
        cindi "From them and me, I guess."
        cindi "Wow. This got a little more personal than I meant it to. I think I'm going to head out. Enjoy the sushi!"

        hide char cindi neutral2
        with dissolve
        jump review_sushi1

    label sushi1_artist:
        me "Maybe we haven't met officially but you look really familiar. Are you an artist? Maybe we've run into each other at one of the galleries nearby."
        cindi "Oh! Yeah! Actually, I was just part of a show downtown a couple of weeks ago. Were you there? It was at Post Script Gallery, the black and white show."
        me "Yes! I knew I had seen you before. Your work was so insightful. What're you doing delivering sushi with talent like that?"
        cindi "That talent comes with some hefty student loans. I haven't quite found a way to make enough money to support myself with my art yet. But thanks."
        cindi "It's cool to meet someone who's seen my works just out in the wild."

        menu:
            "Maybe we could get drinks?":
                jump sushi1_date2

            "Hopefully, you'll pay off your student loans soon.":
                jump sushi1_waste

            "It's cool to meet someone so talented.":
                jump sushi1_compliment

            "I have a day job I don't particularly like too.":
                jump sushi1_schooling

    label sushi1_date2:
        me "Well, I would love to see you again. Out in the wild. Maybe we could get drinks? I'd love to learn more about you and your process."
        cindi "I feel a little vain saying yes but that sounds really nice. So, yeah, sure."
        me "Great, how about tomorrow around 7pm? We could meet here and go together?"
        cindi "Yeah, I'm off tomorrow so that works perfectly. It's a plan!"
        me "I'll see you then!"

        $ dateCindi = True
        $ date = True
        $ datecindiact = "get some drinks"

        hide char cindi neutral2
        with dissolve
        jump review_sushi1

#temporary
    label review_sushi1:
    "this is where the review portion would go. Go to next day."
    jump day2
