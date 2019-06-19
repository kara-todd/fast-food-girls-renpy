# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define ang = Character("Angela")
define me = Character("[playername]")
define anon = Character("???")
define thiccPies = Character("Thicc Pies")
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
            textbutton "Noodles" action [Hide("phone_dial"), Jump("order_pizza")]
            textbutton "Sushi" at btn_disabled
                
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

        address = renpy.input("Where do you live?")
        address = address.strip()
        hasAddress = True

        if not address:
            hasAddress = False
            address = "Nowhere in paricular"

    scene bg frontdoor

    "Tuesday. Twelve days before the dinner party."
    
    me "Ugh, I forgot to pick up groceries again and there’s nothing left in the fridge besides some wine from the last dinner party. I guess it’s actually not such a bad thing this new pizza place left me a takeout menu, then."
    
    show screen phone_dial

    me "Ugh, I forgot to pick up groceries again and there’s nothing left in the fridge besides some wine from the last dinner party. I guess it’s actually not such a bad thing this new pizza place left me a takeout menu, then."
    

label order_pizza:
    anon "Thicc Pies. What can I get you?"
    $ phone = thiccPies

    me "Hello, can I get a medium meat lover’s pizza and breadsticks with both marinara and pizza sauce on the side."
    phone "Sure. Can I get your address?"
    me "Yeah, it’s [address]."
    phone "Great. It’ll be there ASAP. Have a great night."

    hide screen phone_dial
    $ phone = anon

    "//A knock on the door.//"

    me "Must be my pizza. Finally."

    # Click to answer door

    show char angela neutral:
        xalign 0.5
        yalign 0.25
    with dissolve

    girl "Hey, did you order a medium meat lover’s pizza and breadsticks?"
    me "Yes, that was me."
    girl "That’ll be $12."

    menu:
        "Thanks, here you go. You can keep the change.":
            jump pizza_bigspender

        "Thanks. Hey, can I ask you a strange question?":
            jump pizza_question1

        "Thanks, beautiful.":
            jump pizza_beautiful

        "What’ll it be for your phone number?":
            jump pizza_number1

    label pizza_bigspender:
        girl "Look at you, big spender."

        menu:
            "I’m hoping to get in your good graces. Is it working yet?":
                # jump pizza_unsure
                jump pizza_goodbye1

            "You deserve it for being such a hard worker.":
                # jump pizza_hardworker
                jump pizza_goodbye1

            "You’re welcome.":
                jump pizza_goodbye1

            "I would be willing to spend more if you wanted to go out on a date with me later.":
                # jump pizza_adate1
                jump pizza_goodbye1

    label pizza_question1:
        girl "You’ve already asked me a strange question but sure. Can’t promise I’ll answer it, though."
        me "You look really familiar. What’s your name?"
        jump pizza_question2

    label pizza_question2:
        $ girl = angela
        girl "Angela. What about you, Meat Lover sensei?"
        me "[playername]"

    label pizza_beautiful:
        girl "Oh, you’re one of those guys."
        me "One of what guys?"

    label pizza_number1:
        girl "My number is not on the menu."
        me "I didn’t see it on there, but I thought it couldn’t hurt to ask."

    label pizza_goodbye1:
        girl "Alright, well, enjoy the pizza! I hope you have a good night!"