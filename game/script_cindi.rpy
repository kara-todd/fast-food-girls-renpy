# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define c = Character("Cindi")
define me = Character("[playername]")
define anon = Character("???")
define haySushi = Character("Hayashi Sushi")
define phone = anon
define girl = anon

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
