# Angela Script

label angela_1:
  phone "Hello, Phat Pies, home of the Thick and Meaty™. Can I take your order?"
  $ phone = locPizza
  mc "Yes, this is my first time ordering. Would you say the Thick and Meaty is one of your more popular items?"
  phone "Yeah, that or the \"Rollin’ in Dough\"."
  mc "Is that a calzone?"
  phone "Sort of.{w=.5} It’s a whole pizza rolled inside phyllo-dough...{w=0.5} and then deep fried in butter{w=0.5} and then coated in sugar.{w=.8} Shockingly popular!"
  mc "Sounds...{w=.5} interesting...{w=.5} but no.{w=.5} No one likes calzones.{w=.5} They’re just pizza that’s harder to eat.{w=.5} I’ll take the \"Thick and Meaty\""
  phone "Alright, it’ll be \"hot and right on to ya in 30 minutes or less!\""
  phone "..."
  phone "That’s our delivery slogan.{w=.5} I have to say it.{w=.5} Please don’t hold it against me."
  phone "*click*"

  scene black
  with dissolve
  pause 2.0
  "*Knock, Knock, Kock*"
  mc " (Ah, sounds like my meal has arrived)"

  $ ang.name = "???"
  show bg frontdoor night
  pause 1.0
  show angela

  ang "[locPizza]. Here’s your order."
  "She holds out the pizza box and looks away."
  mc "Hm...{w=.5} I called in this order over an hour ago.{w=.5} Don’t you have some kind of delivery guarantee?"
  ang "Look dude, talk is cheap and so is this pizza.{w=.5} You can call corporate and whine over your $10 if you want.{w=.25} I don’t care."
  ang "For me, the only question is are you going to take this pizza or am I?"
  mc "(Quite a direct attitude. Hm.)" 
  mc "(How best to handle this?)"
  mc "I guess you can just take the pizza,{w=.5} give me $10,{w=.5} and we’ll call it even."
  mc "(She suddenly jerks her head back to look at me. Anger and confusion written across her face.)"
  ang "What?!{w=.75} That’s crazy. Why would I give {b}you{/b}{w=.25} money?{w=.5} I’ll just leave."
  "(She starts to move away)"
  mc "Well. I already paid when I ordered. So if you take the pizza that would be theft in my book."
  ang "Fine. {i}Whatever{/i} just take the pizza then and call back in for a refund."
  "(She rolls her eyes and pushes the box towards me)"
  mc "Oh no. I’m not taking the box. I think you made it pretty clear that my complaints are unlikely to be taken seriously.{w=0.5} I’ll never see that money again if I accept the delivery."
  "(She grits her teeth a bit; anger winning over confusion.)"
  ang "Just.{w=.5} Take.{w=.5} The.{w=.5} Pizza.{w=1.0} … Dude."
  mc "So will you be giving me my $10?"
  "(she levels me with a menacing glare)"
  ang "Why would I pay you to take the pizza? That makes no sense. Fine.{w=.5} Just-{w=.5} I’ll take this back.{w=.5} Uhg."
  "(She goes to leave again.)"
  "(*Ring*)"
  "(I’ve pulled out my cell-phone and put it on speaker.)"
  "(*Ring*)"
  "(She looks back at me in disbelief.)"
  ang "What on earth are you—"
  phone "Hello, Phat Pies, home of the Thick and Meaty™. Can I take your order?"
  mc "Hi Yes. I have an employee of yours here who is refusing to deliver my pizza."
  ang "!?!-- That’s crazy I am not ref—"
  phone "Angela?! Oh my god… Are you harassing a customer so badly he had to call in while you are still there?!"
  phone "Sir. I can’t apologize for this enough. I assure you we will take care of everything. Of course we will refund your order, but please take it… on the house."
  ang "He wouldn’t take the pizza. He-"
  phone "Angela! Give the customer his order, and report back here. Immediately."
  "(She violently shoves the pizza in my direction.)"
  mc "Why thank you. I certainly appreciate a business with integrity."
  phone "Our pleasure sir. Please just call again anytime from this number and we will honor you with another free delivery."
  phone "Satisfied customers are our business after all!{w=.5} If there is anything else we can do for you let us know."
  mc "Of course. I’m sure I’ll be calling again soon."
  phone "*click*"
  ang "Are you serious right now? What was that?!?"
  mc "Angela, right?{w=.5} That’s a nice name.{w=.5} Look Angela. You did tell me to call didn’t you?"
  $ ang.name = "Angela"
  ang "You said-"
  "(I shrug)"
  mc "I never said I wouldn’t call… only that you implied it wouldn’t work."
  "(I grin at her wolfishly.)"
  mc "I guess you were wrong there. Maybe you just need to know how to work the system."
  ang "...."
  ang "Yeah. Well, I hope you enjoy your free pizza"
  mc "Two now."
  ang "Free Pizzas…"
  mc "Well, technically, one free pizza and a free future meal of my choice. :)"
  ang "Or whatever…"
  ang "I guess now at least I can be over this dumb job."
  mc "Oh… surely you won't lose your job over one little upset customer."
  "(Her death stare slides into a sidelong grimace.)"
  ang "Maybe not one customer no."
  mc "Come to think of it… They were rather accommodating after hearing your voice. Not your first offence Angela?"
  "(Her eyes snap back to glare at me)"
  ang "You don’t know me… and I don’t owe you anything. So I’m out of here. Later jerkwad."
  "(She turns to leave and I call out after her.)"
  mc "Well except the pizza."
  "(Disgusted. She realizes she’s still holding the pizza box turns and throws it at me.)"
  ang "There !@#$#! Hot and right on to ya!"

label angela_2:
  scene black
  with dissolve
  pause 2.0

  mc "Hm.{w=.5} I think I will call in again.{w=.5} Time to claim that free meal."
  pause 1.0

  phone "Hello.{w=.25} Phat Pies.{w=.5} Home of the Thick and Meaty™. Can I take your order?"
  mc "Oh? Angela, how lovely to hear from you!"
  ang "SERIOUSLY!?{w=.75} Erk-{w=.5} *whispers* seriously dude?!{w=.25} Are you calling again?"
  mc "Of course. I am owed another delivery aren’t I? On the house?"
  ang "… Yes."
  ang "You are."
  mc "And I hope you will be delivering it \"hot and right on to me\" Angela."
  ang "No man, I won’t… and you want to know why? Because I’m suspended from delivery duty due to a “customer complaint” issue."
  ang "So there go my cash tips"
  mc "No! That can't be right. I for one think you are an exemplary employee."
  ang "…"
  ang "…"
  ang "You’re kidding right?"
  mc "Not at all. You were only acting in the best interest of the company after all. It seems a waste if they aren't able to see that in you."
  ang "…"
  ang "Yeah.{w=.5} Sure man.{w=.5} Whatever."
  mc "Not that I'll be complaining about it if it means more free service."
  ang "Cool.{w=.5} Great.{w=.5} Thanks for the pep talk.{w=.5} Are you actually going to order something?"
  mc "Yes.{w=.75} However, I think I might have been a little unfair to you Angela, and I want to make it up to you.{w=.5} Do you have an online ordering form?"
  ang "We do…"
  mc "Alright. Thanks then."
  "*click*{w=.5} (I hang up the phone)"
  mc "Ok…{w=.5} let's see what we can do here."
  "*I pull up my phone and find the online ordering form.*"
  "(Yes, this should work quite nicely.{w=.5} Hm.{w=.5} Better leave my number too.{w=.5} I expect they will call…{w=.75} and I'll leave a comment about the free meal.)"
  "(Now I just need to message Jo.)"

  scene bg apartment night

  window hide
  window auto

  nvl show

  # $ boss_phone.delete_history()
  # $ active_phone = boss_phone
  # show screen chat_log(active_phone)

  im_mc "Hi Jo! I have decided to order pizza for the team."
  im_mc ":)"
  im_jo "Ok… Thanks boss. How random and suspiciously considerate of you. Do you want me to find a place"
  im_mc "No, I already got it covered."
  im_mc "In fact I've already put in the order and they are being delivered as we speak."
  im_jo "Uh-huh."
  im_jo "And did you perhaps also want the team to know about the pizza?"
  im_jo "Or is this more of a for the team \"in spirit\" kinda thing?"

  # sms jo "Ok… Thanks boss. How random and suspiciously considerate of you. Do you want me to find a place"

  # $ chat_msg(boss_phone, "ChefBoiUrD", "Hi Jo! I have decided to order pizza for the team.")
  # $ chat_msg(boss_phone, "ChefBoiUrD", ":)")


  # $ chat_msg(boss_phone, "JoGetter", "Ok… Thanks boss. How random and suspiciously considerate of you. Do you want me to find a place")

  # $ chat_msg(boss_phone, "ChefBoiUrD", "No, I already got it covered.")

  # $ chat_msg(boss_phone, "ChefBoiUrD", "In fact I've already put in the order and they are being delivered as we speak.")

  # $ chat_msg(boss_phone, "JoGetter", " Uh-huh.")

  # $ chat_msg(boss_phone, "JoGetter", " And did you perhaps also want the team to know about the pizza?")

  # $ chat_msg(boss_phone, "JoGetter", "Or is this more of a for the team \"in spirit\" kinda thing?")

  mc "that was nice"