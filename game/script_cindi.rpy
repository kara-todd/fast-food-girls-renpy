# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define c = Character("Cindi")
define me = Character("[playername]")
define anon = Character("???")
define haySushi = Character("Hayashi Sushi")
define phone = anon
define girl = anon
define gave_angname = False
define gave_cindiname = False
define gave_blyname = False
define gave_domname = False

label sushi1_start:
    show char cindi neutral2:
        xalign 0.5
        yalign 0.75
    with dissolve

    girl "Hi! did you order a Chef’s Deluxe Assorted Plate and a seaweed salad?"
    me "Yeah, that was me."
    girl "Okay, great. That'll be $30."
    me "Here you go, keep the change."
    girl "Wow, look at you big spender. Thanks!"

    menu:
        "You deserve it.":
            jump sushi1_hardworker

        "Can I ask you a question?":
            jump sushi1_question1

        "You're welcome!":
            jump sushi1_end1

    label sushi1_end1:
        me "You're welcome! Have a good night!"
        girl "You too!"

        hide char angela neutral2
        with dissolve

        jump review_sushi1

    label sushi1_question1:
        me "Can I ask you a somewhat strange question?"
        girl "You've already asked me a strange question but sure. Can't promise I'll answer it though."
        me "You look really familiar. What's your name?"
        girl "It's Cindi. What about you?"
        c "It's Cindi. What about you?"

        menu:
            "It's [playername].":
                $ gave_cindiname = True
                jump sushi1_samename

            "It's [angname]." if gave_angname:
                $ gave_cindiname = True
                jump sushi1_cindiang

            "It's [domname]." if gave_domname:
                $ gave_cindiname = True
                jump sushi1_domang

            "It's [blyname]." if gave_blyname:
                $ gave_cindiname = True
                jump sushi1_blyang

            "Give a new name":
                $ gave_cindiname = True
                jump sushi1_newname

label sushi1_samename:
    python:
        cindiname = playername.strip()
    me "It's [cindiname]."
    jump sushi1_why

label sushi1_angname:
    python:
        cindiname = angname.strip()
    me "It's [cindiname]."
    jump sushi1_why

label sushi1_blyname:
    python:
        cindiname = blyname.strip()
    me "It's [blyname]."
    jump sushi1_why

label sushi1_domname:
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
    jump review_sushi1

#temporary
    label review_sushi1:
    "this is where the review portion would go. Go to next day."
    jump day2
