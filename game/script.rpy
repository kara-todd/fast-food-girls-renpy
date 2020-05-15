# The script of the game goes in this file.

# Characters
define ang = Character("Angela", image="angela", window_right_padding=200)
define cin = Character("Cindi")
define mc = Character("boss")
define jo = Character("jo")

define im_mc = Character("ChefBoiUrD", kind=nvl)
define im_jo = Character("JoGetter", kind=nvl)
define im_ang = Character("Angela", kind=nvl)

# Randos
define anon = Character("???")
define phone = Character("phone")
define girl = anon
define sam = Character("Sam")

# Location Names
define locPizza = Character("Phat Pies")
define locSushi = Character("EZKaya")
define locBBQ = Character("Butt Hutt")
define locTaco = Character("Taco Bonita")

# Game state declration
# init python:
#     from ChatLog import ChatLog

#     # boss_phone = ChatLog("BossPhone")
#     # jo_phone = ChatLog("JoPhone")

#     active_phone = None

# The game starts here.

label start:
    show bg apartment night
    with dissolve

    show screen phone_dial

    mc "What should I have for dinner tonight?"
