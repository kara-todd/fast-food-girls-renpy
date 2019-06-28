# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define ang = Character("Angela")
define me = Character("[playername]")
define anon = Character("???")
define phatPies = Character("Phat Pies")
define c = Character("Cindi")
define haySushi = Character("Hayashi Sushi")
define phone = anon
define girl = anon

# State declration
default hearts = 0
default hasAddress = False
default hasName = False

transform btn_disabled:
    alpha 0.6

screen phone_dial():
    modal True
    zorder 100
    frame:
        xalign 0.5 ypos 100
        grid 3 2:
            textbutton "Pizza" action [Hide("phone_dial"), Jump("order_pizza")]
            textbutton "Sushi" action [Hide("phone_dial"), Jump("order_sushi")]
            textbutton "BBQ" at btn_disabled

            textbutton "Dessert" at btn_disabled
            textbutton "Sandwhich" at btn_disabled
            textbutton "Grub Daddy" at btn_disabled

# The game starts here.

label start:
    python:
        playername = renpy.input("What is your name?")
        playername = playername.strip()
        hasName = True

        if not playername:
            hasName = False
            playername = "???"

        blogname = renpy.input("What would you like to name your food review blog?")
        blogname = blogname.strip()
        hasblogName = True

        if not blogname:
            hasblogName = False
            blogname = "Yummy in my Tummy"

label day1:
    scene doorway

    "Monday. Five days before the dinner party."

    me "Ugh, I forgot to pick up groceries again and there’s nothing left in the fridge."
    me "I guess it’s actually not such a bad thing a bunch of restaurants left me takeout menus, then."

    show screen phone_dial

    me "What should I get for dinner tonight?"


label order_pizza:
    anon "Phat Pies. What do you want?"
    $ phone = phatPies

    me "Hello, can I get the medium Mega Meats pizza and an order of breadsticks?"
    phone "Yeah sure. Can I get your address?"
    me "It’s 1111 2nd Street."
    phone "Okay. It’ll be there ASAP."

    hide screen phone_dial
    $ phone = anon

    "A knock on the door."

    me "That should be my pizza."

    # Click to answer door

    jump pizza1_start

label order_sushi:
    anon "Thank you for calling Hayashi Sushi. What can we do for you?"
    $ phone = haySushi

    me "Hello, can I get the Chef’s Deluxe Assorted Plate. I would also like seaweed salad on the side, please."
    phone "Alright. Can I get your address?"
    me "It’s 1111 2nd Street."
    phone "Great. It’ll be there in twenty minutes. I hope that you have a delicious night."

    hide screen phone_dial
    $ phone = anon

    "A knock on the door."

    me "I hope that's my sushi."

    # Click to answer door

    jump sushi1_start

#temporary
label day2:
    scene doorway

    "Tuesday. Four days before the dinner party."

    me "Ugh, I forgot to pick up groceries again and there’s nothing left in the fridge."
    me "I guess it’s actually not such a bad thing a bunch of restaurants left me takeout menus, then."

    show screen phone_dial

    me "What should I get for dinner tonight?"

    hide screen phone_dial
    $ phone = anon

    "A knock on the door."

    me "I hope that's my sushi."

    # Click to answer door

    jump sushi1_start
