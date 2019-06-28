# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define ang = Character("Angela")
define me = Character("[playername]")
define anon = Character("???")
define phatPies = Character("Phat Pies")
define phone = anon
define girl = anon
define gave_angname = False
define gave_cindiname = False
define gave_blyname = False
define gave_domname = False

label pizza1_start:
    show char angela neutral2:
        xalign 0.5
        yalign 0.75
    with dissolve

    girl "Hey, did you order the medium Mega Meats and breadsticks?"
    me "Yeah, that was me."
    girl "Oh good. I don't know what I'd do if you didn't."
    girl "That’ll be $12."
    me "Here you go, keep the change."
    girl "Thanks! Enjoy your pizza!"

    menu:
        "Wait, can I ask you a question?":
            jump pizza1_question1

        "Have a good night!":
            jump pizza1_end1

    label pizza1_end1:
        me "Thanks! Have a good night!"
        girl "You too!"

        hide char angela neutral2
        with dissolve

        jump review_pizza1

    label pizza1_question1:
        me "Wait, can I ask you a question?"
        girl "Yeah, long as you make it quick."
        me "What’s your name?"
        girl "I'm not sure why that's any of your business but it's Angela."
        ang "I'm not sure why that's any of your business but it's Angela."
        ang "What's yours?"

        menu:
            "It's [playername].":
                $ gave_angname = True

            "It's [cindiname]." if gave_cindiname:
                $ gave_angname = True
                jump pizza1_cindiang

            "It's [domname]." if gave_domname:
                $ gave_angname = True
                jump pizza1_domang

            "It's [blyname]." if gave_blyname:
                $ gave_angname = True
                jump pizza1_blyang

            "Give a new name":
                $ gave_angname = True
                jump pizza1_newname

label pizza1_samename:
    python:
        angname = playername.strip()
    me "It's [angname]."
    jump pizza1_why

label pizza1_cindiname:
    python:
        angname = cindiname.strip()
    me "It's [cindiname]."
    jump pizza1_why

label pizza1_blyname:
    python:
        angname = blyname.strip()
    me "It's [blyname]."
    jump pizza1_why

label pizza1_domname:
    python:
        angname = domname.strip()
    me "It's [domname]."
    jump pizza1_why

label pizza1_newname:
    python:
        angname = renpy.input("What name would you like to give?")
        angname = angname.strip()
        hasangName = True

        if not angname:
            hasangName = False
            angname = playername.strip()
    me "It's [angname]."
    jump pizza1_why

    label pizza1_why:
        ang "So were you just being nosy or did you have a reason for asking for my name?"

        menu:
            "Yeah, I was just being nosy.":
                jump pizza1_nosy

            "I wanted to ask you out.":
                jump pizza1_drinks

            "I wanted your name for a review.":
                jump pizza1_blogger

            "I just wanted to get to know you.":
                jump pizza1_fun

    label pizza1_drinks:
        me "I thought I should ask for your name before I asked you out. What do you think about grabbing drinks tomorrow?"
        ang "I’m not really a 'going out for drinks' kind of girl and I’ve actually got plans."
        me "What if I joined you for those plans?"
        ang "You don’t even know what I’m doing. I could be doing something very disgusting or horrifying or personal."

        menu:
            "I'll do anything.":
                jump pizza1_askforit

            "I'm sorry. You're right.":
                jump pizza1_end4

    label pizza1_blogger:
        me "I’m a food blogger and I wanted to make sure I got your name for the review."
        ang "A blogger huh? What’s it called? I want to read what you’ve got to say about our pizza later."
        me "It's [blogname]."
        ang "Cool. I'll look that up tonight then. I've gotta make sure you weren't just making up a blog as an excuse to get my name."
        me "Why would I do that?"
        ang "I don't know, maybe you're too nervous to admit you like me."

        menu:
            "That's both rude and untrue.":
                jump pizza1_hurtfeelings
            "I have a blog but I also like you.":
                jump pizza1_likeyou

    label pizza1_hurtfeelings:
        me "Well, you're both rude and wrong. I've been working on this blog since Wordpress became available last year."
        ang "And you don't like me?"
        me "If I did, I wouldn't be too nervous to admit that I did."
        ang "That's not a full answer."

        menu:
            "I did but now I'm not so sure.":
                jump pizza1_yesbutno

            "I do.":
                jump pizza1_yes

            "No.":
                jump pizza1_rudeend

    label pizza1_rudeend:
        me "No. In fact, you seem really rude for someone working in customer service."
        ang "And you seem awfully chatty for someone too lazy to get out of your house to get food."
        me "Excuse me but my laziness basically employs you."
        ang "Sure. But at least other people are decent enough not to waste my time. It's simple. Just take the food, hand the delivery person some money, and close the door."
        me "Fine. Then just go."
        ang "Fine."

        hide char angela neutral2
        with dissolve

        jump review_pizza1

    label pizza1_yes:
        me "I do like you. But that doesn't make me nervous."
        ang "Then what took you so long to just say that."
        me "Just saying 'I like you' is a little first grade don't you think?"
        ang "Yeah but I'm not really into small talk and wasting time. Especially when I'm technically at work."
        me "So would you like to go out tomorrow then?"
        ang "Ooh yeah, probably not tomorrow. I'm busy. And I'm not sure if you're my type just yet."
        ang "But maybe order a pizza again on Wednesday and we'll talk more."

        hide char angela neutral2
        with dissolve

        jump review_pizza1

    label pizza1_yesbutno:
        me "I thought I might like you but now I'm not so sure. You seem like you might be a little too tough for my taste."
        ang "Yeah, if you want someone softer, you might want to order your food from somewhere else. Find another takeout girl to hit on."
        me "What if I just really wanted some more pizza?"
        ang "You'll get me or Joe here at your door."
        me "And what if I decided I wanted someone tough."
        ang "Maybe if you're real convincing, I'll give you a shot."
        ang "But that's enough hypotheticals and chit-chat for one night. I've got more pizzas to deliver. Enjoy your Phat Pie."

        hide char angela neutral2
        with dissolve

        jump review_pizza1

    label pizza1_likeyou:
        me "Well, I do have a blog. But I also am a little nervous to admit I like you."
        ang "But see that wasn't so hard, was it?"

        menu:
            "Tell the truth.":
                jump pizza1_honest

            "Play it cool.":
                jump pizza1_cool

    label pizza1_cool:
        me "Not at all. While I'm taking chances, do you have plans tomorrow?"
        ang "Actually, I do."

        menu:
            "Mind if I tag along?":
                jump pizza1_tagalong

            "Would you be free for dinner after?":
                jump pizza1_dinner

            "Have a good time.":
                jump pizza1_end3

    label pizza1_honest:
        me "You're right. While I'm being honest, let me say. You're gorgeous and I'd love to have you over for dinner."
        ang "Well, if I'm being honest. You don't look so bad yourself. But I don't usually do dinners in some stranger's house."

        menu:
            "We could get to know each other first.":
                jump pizza1_knowfirst

            "I'm having a dinner party on Saturday with some friends. I'd love for you to be there.":
                jump pizza1_dinnerparty

    label pizza1_nosy:
        me "Yeah, I was just being nosy."
        ang "Well at least you're honest as well as nosy. But, if that's all you want, then I might as well go now. Have a good night."
        me "Wait, I'm not done being nosy. I have another question."
        ang "Alright. But seriously, this is it for the Q&A portion of the show."

        menu:
            "Where did you grow up?":
                jump pizza1_growup

            "What do you do for fun?":
                jump pizza1_fun

            "Tell me some inside secrets from the restaurant.":
                jump pizza1_secrets

    label pizza1_secrets:
        me "Do you have any restaurant secrets that I can put in my food blog when I review this pizza?"
        ang "Trust me, no one really wants to know restaurant secrets. Working in food service almost made me stop eating out. But then I remembered I'm a terrible cook."
        me "Maybe I can make you dinner sometime. I don't have any michelin stars or anything but I consider myself a pretty good cook."
        ang "I don't usually do dinners in some stranger's house."
        me "I'm actually have a dinner party on Saturday with a group of friends. I'd love for you to be there. There would be other people there too. So maybe it wouldn't be so weird."
        ang "That would actually be weirder. I won't know anyone there."
        me "Well, we could always get to know each other first."
        ang "How would you want to get to know each other then?"
        me "We could continue to quiz each other back and forth or we could go out tomorrow?"
        ang "I have plans tomorrow."

        menu:
            "Can I ask you another question then?":
                jump pizza1_question3

            "Mind if I tag along?":
                jump pizza1_tagalong

            "Would you be free for dinner after?":
                jump pizza1_dinner

    label pizza1_question3:
        me "Well I guess that only leaves one choice. We have to quiz each other."
        ang "You know I'm still on the clock right. I really do need to go back to work."
        me "Just one more question. Promise."
        ang "Fine. But that's it. Then I've gotta go."

        menu:
            "What do you do for fun?":
                jump pizza1_fun

            "Are you ever scared by your job?":
                jump pizza1_mom

            "What is your favorite color?":
                jump pizza1_color

            "What is your blood type?":
                jump pizza1_bloodtype

    label pizza1_bloodtype:
        me "Alright. An important one here - what's your blood type?"
        ang "What? Why is that an important one?"
        me "There are lots of things you can know based off of blood types. In Japanese culture, it's sometimes associated with personality and demeanor."
        me "There's the blood type diet to know what foods settle best. And, if anything were to happen to you, it's important to know."
        ang "Alright. That makes it a less creepy but still surprising. I'm type B. What about you?"
        me "I'm AB."
        ang "Cool. Well, like I said, that's it for now. Order another pizza and maybe we'll see each other again soon."

        hide char angela neutral2
        with dissolve

        jump review_pizza1

    label pizza1_color:
        me "Let's go with the basics. What's your favorite color?"
        ang "Red and black. What about you?"

        python:
            angcolor = renpy.input("What name would you like to give?")
            angcolor = angcolor.strip()
            hasangColor = True

            if not angcolor:
                hasangColor = False
                angcolor = "blood red"
        me "Mine is actually [angcolor]."
        $ gave_angcolor = True

        ang "Cool. Well, I guess you'll just have to order another pizza before Saturday to get to know me better because I need to go. But it's been fun."
        ang "Good night, [angname]! I hope I see you again soon."
        me "You will!"

        hide char angela neutral2
        with dissolve

        jump review_pizza1

    label pizza1_mom:
        me "Are you ever scared while doing your job?"
        ang "You mean because I drive a motorcycle? Because it's really not that scary."
        me "No, because you're going to strangers' houses. You never worry that your customers might try to hurt you?"
        me "I mean, you’re delivering pizza but you’re also just walking up to strangers’ doors with no one around to have your back."
        me "Some guy could just grab you and do anything to you. You could be delivering to an abandoned building. And they could be long gone before anyone even came to check on you."
        ang "You’re starting to sound like my mom. No, I’m not worried about some crazy person grabbing me off their porch and killing me or something."
        ang "Is your overwhelming paranoia the reason you’re ordering delivery and not leaving your house to get some real food yourself?"
        me "No. I'm just tired tonight so I didn't feel like going out."
        ang "Then why are you trying to scare me right now?"
        me "I just know that crazy people are out there. I’d be nervous about my sister if she worked as a delivery girl, just going to anyone’s house."
        ang "That’s sweet of you to be nervous about your sister. But I am not your sister so don’t worry about me. I’ll be just fine and I’m sure your sister will be too."
        me "She died, actually."
        ang "Oh. I’m so sorry. I didn’t know. The way you talked about her, it sounded like…"
        me "It’s fine. You couldn’t have known. I shouldn’t have brought it up. I know you’re not my sister."
        me "You just never look at the world the same way again after someone you love is killed and the person who did it just gets away with it and goes on with their lives."
        ang "Yeah. I can’t imagine. That’s really rough. I’m sorry."
        me "It’s alright. I’ll let you get back to work. I’m sorry I wasted your time. Good night and please stay safe."
        ang "I will. Good night."

        hide char angela neutral2
        with dissolve

        jump review_pizza1

    label pizza1_growup:
        me "Did you grow up around here?"
        ang "Wow, you weren’t kidding about being nosy. No, I grew up in the north and moved down south to get away from all of the snow when I went to college."
        ang "Is there anything else you'd like to know? How many guys I've dated, my work history, favorite color?"

        menu:
            "No, sorry to keep you.":
                jump pizza1_end2

            "Actually, yes.":
                jump pizza1_question2

    label pizza1_end2:
        me "Haha no. Sorry to keep you, I was just curious. You sounded like you weren't from around here."
        ang "And I take it you grew up here."
        me "Not really. I've moved around pretty frequently ever since I was young. I like to think of myself as a taste tester and the world is my buffet."
        ang "That's an interesting take. Although, I kind of hate buffets. But I get what you mean."
        ang "Anyways, I should probably go now. Good night!"
        jump pizza_review1

    label pizza1_question2:
        me "Actually, there is more that I'd like to know about you."
        ang "Alright. But make it a good one this time. I need to get back to my job at some point."

        menu:
            "What do you do for fun?":
                jump pizza1_fun

            "Tell me some inside secrets from the restaurant.":
                jump pizza1_secrets

            "Are you ever scared of your job?":
                jump pizza1_mom

    label pizza1_fun:
        me "What do you like to do for fun?"
        ang "I love doing anything that'll get my heart racing. Lately it's been rock climbing, skating at Factory Skatepark, and taking joy rides out to the mountains on my bike."
        me "Any of those sound good to me. Do you have any plans for tomorrow?"
        ang "Actually, I do."

        menu:
            "Mind if I tag along?":
                jump pizza1_tagalong

            "Would you be free for dinner after?":
                jump pizza1_dinner

            "Have a good time.":
                jump pizza1_end3

    label pizza1_end3:
        me "Cool. Well I hope you have a good time. I hope to see you again soon."
        ang "Maybe. Good night, [angname]. Enjoy your pizza."

        hide char angela neutral2
        with dissolve

        jump review_pizza1

    label pizza1_tagalong:
        me "Great, I didn't have any plans yet. Mind if I tag along?"
        ang "You don't even know what I'm doing. I could be doing something very disgusting or horrifying or personal."

        menu:
            "I'll do anything.":
                jump pizza1_askforit

            "I'm sorry. You're right.":
                jump pizza1_end4

    label pizza1_askforit:
        me "I don't mind. I'll do anything."
        ang "Alright. But just remember, you asked for it and there’s no backing out now."
        me "Should we meet here? Or somewhere else?"
        ang "Yeah, we’ll meet here and drive together. That way I know for sure you won’t chicken out. I’ll be here at four."
        me "Great, I’ll see you then!"
        ang "Great!"

        hide char angela neutral2
        with dissolve

        jump review_pizza1

    label pizza1_dinner:
        me "Think maybe you could pencil me in for dinner afterwards?"
        ang "As much as I would need to eat dinner at some point, no."
        ang "I like to get out of my comfort zone for first dates and I'm afraid that'd be a little tame after my other plans for the day."

        menu:
            "Do you want to come in and eat with me now then?":
                jump pizza1_backtowork

            "Mind if I join in on your plans then?":
                jump pizza1_joinin

            "Maybe another time, then.":
                jump pizza1_end5

            "What are your other plans?":
                jump pizza1_skydiving

    label pizza1_skydiving:

        me "You keep being really vague about your plans. I'm kind of curious, what are your plans?"
        ang "I'm going skydiving for the first time."
        me "Wow, you're a real daredevil aren't you?"
        ang "Yeah, I like to think I am. You know, I've got the red suit and everything ready for tomorrow."
        me "I meant that in like an Evil Knievil sort of way."
        ang "Yeah, I figured."
        me "I could see how just dinner would be tame after skydiving but are you sure you wouldn't enjoy cooling down with some company?"
        me "We could still do something that would make you uncomfortable if it really means that much to you."
        ang "And what would that be?"

        menu:
            "I could make you dinner here.":
                jump pizza1_homemadedinner

            "We could play strip poker.":
                jump pizza1_gambler

            "We could go to a strip club.":
                jump pizza_hardno

    label pizza1_homemadedinner:
        me "I can’t think of anything more uncomfortable for a person to do than to come into a stranger’s house."
        me "I mean, you have no idea if I'm a good guy let alone a good cook. I think I am. But you'll have to take my word for it."
        ang "I don't know. You're giving me pretty good reasons not to come over."
        me "So have I found something outside of your comfort zone?"
        ang "I don't know."
        me "Then why don't you come over tomorrow. I'll make something delicious. It'll be fun. And if it's boring, we'll do whatever you want."
        ang "Alright. Fine. I'll be here when I'm done and cleaned up after my skydiving adventure tomorrow."
        me "I can't wait!"
        ang "Well, I better get to work. Good night!"

        hide char angela neutral2
        with dissolve

        jump review_pizza1

    label pizza1_gambler:
        me "We could play strip poker. We'd get everything out in the open, it'd be exciting and fun."
        ang "I don't think so. I like to take chances but not based off of pure luck."
        ang "Plus, I don't really want to get naked with a guy who thinks strip poker is a good date idea."
        me "I'm just trying to think of something exciting and different for you. My first idea was dinner."
        ang "Yeah. Well maybe think a little harder about it. I've gotta go back to work. Feel free to order another pizza if you come up with a better idea."

        hide char angela neutral2
        with dissolve

        jump review_pizza1

    label pizza1_hardno:
        me "We could go to a strip club together. I can't think of anything more uncomfortable for either of us than watching other women strip during our first date."
        ang "Yeah, that's gonna be a hard no for me. I don't know why you would even think of that. It's gross, not exciting."
        me "The word I used was uncomfortable."
        ang "Still no. Enjoy that pizza."

        hide char angela neutral2
        with dissolve

        jump review_pizza1

    label pizza1_backtowork:
        me "I can’t think of anything more uncomfortable for a person to do than to come into a stranger’s house. So what do you think about coming in for a minute and eating dinner with me?"
        ang "No. I’ve already stayed here way longer than I should have. If I come in and eat, I will definitely get fired."
        me "It sounds like you’re nervous to come inside. Have I found something outside of your comfort zone?"
        ang "I am definitely uncomfortable right now."
        me "So come in, then. Just for a minute. You said you really see what a person is like when they have to get out of their comfort zone. I'd like to see what you're really like."
        me "I promise to do something I find incredibly uncomfortable next to make it even."
        ang "If my mom were here, she would murder me for even considering but okay. Just for a minute, though."

        hide char angela neutral2
        with dissolve

        jump review_pizza1
        #remove option of ordering pizza - she dead

    label pizza1_joinin:
        me "Everything else you mentioned sounded like a lot of fun. Mind if I join in on whatever you've got planned tomorrow?"
        ang "That is a dangerous question. You don't even know what I'm doing. I could be doing something very disgusting or horrifying or personal."

        menu:
            "I'll do anything.":
                jump pizza1_askforit

            "I'm sorry. You're right.":
                jump pizza1_end4

    label pizza1_end4:
        me "I’m sorry. I didn’t think about that. You’re right. Maybe another time."
        ang "Maybe. Good night, [angname]. Enjoy your pizza."

        hide char angela neutral2
        with dissolve

        jump review_pizza1

    label pizza1_end5:
        me "Alright. Well, maybe another time, then. Enjoy whatever exciting thing you've got planned tomorrow."

        hide char angela neutral2
        with dissolve

        jump review_pizza1

#temporary
    label review_pizza1:
    "this is where the review portion would go. Go to next day."
    jump day2
