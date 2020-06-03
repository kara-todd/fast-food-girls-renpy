# The script of the game goes in this file.

# Credit to: https://pastebin.com/QnXknASm
init python:
    speaking = None
 
    def while_speaking(name, speak_d, done_d, st, at):
        if speaking == name:
            return speak_d, .1
        else:
            return done_d, None

    curried_while_speaking = renpy.curry(while_speaking)

    def WhileSpeaking(name, speaking_d, done_d=Null()):
        return DynamicDisplayable(curried_while_speaking(name, speaking_d, done_d))

    def speaker_callback(name, event, **kwargs):
        global speaking
 
        if event == "show":
            speaking = name
        elif event == "slow_done":
            speaking = None
        elif event == "end":
            speaking = None

    speaker = renpy.curry(speaker_callback)

# Characters
define ang = Character("Angela", image="angela", window_right_padding=200, callback=speaker("angela"))
define cin = Character("Cindi", image="cindi", window_right_padding=200, callback=speaker("cindi"))
define mc = Character("boss")
define jo = Character("jo")

define im_mc = Character("ChefBoiUrD", kind=nvl)
define im_jo = Character("JoGetter", kind=nvl)
define im_ang = Character("Angela", kind=nvl)

# Randos
define anon = Character("???")
define phone = Character("phone")
define van = Character("Vanessa", image="vanessa", window_right_padding=200, callback=speaker("vanessa"))
define sam = Character("Sam", image="sam", window_right_padding=200, callback=speaker("sam"))

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
