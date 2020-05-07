# The script of the game goes in this file.

# Characters
define ang = Character("Angela", image="angela", window_right_padding=200)
define cin = Character("Cindi")
define mc = Character("")

# Randos
define anon = Character("???")
define phone = Character("phone")
define girl = anon

# Location Names
define locPizza = Character("Phat Pies")
define locSushi = Character("EZKaya")
define locBBQ = Character("Butt Hutt")
define locTaco = Character("Taco Bonita")

# Game state declration

transform btn_disabled:
    alpha 0.6

screen phone_dial():
    modal True
    zorder 100
    frame:
        xalign 0.5 ypos 100
        grid 2 2:
            textbutton "Pizza" action [Hide("phone_dial"), Jump("angela_1")]
            textbutton "Tacos" at btn_disabled
            textbutton "Sushi" at btn_disabled
            textbutton "BBQ" at btn_disabled


# The game starts here.

label start:
    show bg apartment night
    with dissolve

    show screen phone_dial

    mc "What should I have for dinner tonight?"

