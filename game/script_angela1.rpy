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
  mc "(Ah, sounds like my meal has arrived)"

  $ ang.name = "???"

  show bg frontdoor night
  pause 1.0
  show angela

  ang @ angry "[locPizza]. Here’s your order."
  "She holds out the pizza box and looks away."
  mc "Hm...{w=.5} I called in this order over an hour ago.{w=.5} Don’t you have some kind of delivery guarantee?"
  ang "Look dude, talk is cheap and so is this pizza.{w=.5} You can call corporate and whine over your $10 if you want.{w=.25} I don’t care."
  ang @ sad "For me, the only question is are you going to take this pizza or am I?"
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

  im_mc "Hi Jo! I have decided to order pizza for the team.{fast}"
  im_mc ":){fast}"
  im_jo "Ok… Thanks boss. How random and suspiciously considerate of you. Do you want me to find a place{fast}"
  im_mc "No, I already got it covered.{fast}"
  im_mc "In fact I've already put in the order and they are being delivered as we speak.{fast}"
  im_jo "Uh-huh.{fast}"
  im_jo "And did you perhaps also want the team to know about the pizza?{fast}"
  im_jo "Or is this more of a for the team \"in spirit\" kinda thing?{fast}"
  im_mc "Certainly.{fast}"
  im_mc "I would hate for all that good food to go to waste. You should just have everybody head over here tonight for an after party.{fast}"
  im_jo "Everybody.{fast}"
  im_jo "Tonight.{fast}"
  im_mc "Well, in the next few hours I'd expect. I didn't get a clear delivery time.{fast}"
  im_mc "They say 30 minutes or less, but I'm not sure that's to be trusted.{fast}"
  im_mc "A bit of leeway is reasonable. Given the order and all.{fast}"
  im_jo "What order {i}exactly{/i} is that.{fast}"
  im_mc "Jo! Don't fret over the specifics. I wanted to take something off your plate. You'll have a lot going on getting the whole team here tonight.{fast}"

  show screen phone_notification("Incomming call [locPizza]") with wipedown

  im_mc "Oh. Speaking of… I've got a call to take.{fast}"
  im_mc "I look forward to the party Jo!{fast}"

  hide screen phone_notification
  nvl hide

  phone "Hello sir. This is John. I'm the manager down at Thic Pies."
  mc "Hello John. Nice to hear from you."
  phone "I'm calling about an online order we received from this number."
  mc "Yes. Is there some kind of problem?"
  phone "The order was for 150 pizzas for immediate delivery... Is that correct?"
  mc "Yes, that is correct. I have a big party planned tonight."
  phone "Sir. I mean no offense, but there is no way you need 150 pizzas. Perhaps I can help you figure out a better order size. What's your head count?"
  mc "Are you not able to deliver the pizzas then? I can order elsewhere…"
  phone "No. It's not that we can't deliver… I'm just concerned. I want to make sure this is what you really want."
  mc "I definitely want 150 pizzas. Does that still come with the 30 minute guarantee?"
  phone "Well-"
  mc "Ha ha! No, that would be crazy. However, I do need them tonight. I have a big team in town for a few months and they'll be pulling a lot of late nights. Do you accept billing accounts and routine scheduling?"
  phone "Oh, certainly sir! We'd love to have you come in and talk through some options."
  mc "Great. I'll swing by then. Assuming tonight goes well of course…"
  phone "I'm sure you'll be fully satisfied."

  scene black
  with dissolve
  pause 2.0
  "*Knock, Knock*"

  mc "(It's a bit early for the pizzas. It must be some of the crew.)"

  show bg frontdoor night
  pause 1.0
  show sam

  sam "Hey Boss! It's Sam. Jo told us to come over and set up for a party tonight?"
  mc "Yeah, there's a clearing and deck around back."
  sam "You really throw a last minute shin-dig with no warning to Jo?"
  mc "Nothing she can't handle. Jo's top class. I know she'll enjoy it when she's here."
  sam "Lol. Classic move. Party like a boss. Well, refusing free food is against my code of ethics- So we'll get started."
  mc "Put out the food tables first. I got this local pizza place catering and they should be here soon."
  sam "Mmm. Mmm. Pizza."

  hide sam with dissolve

  "(He disappears around back. I hear the trucks pull around and the clang of tables and outdoor furniture being erected.)"

  "(*knock. knock.*)"

  "(I open the door. An energetic delivery girl and a nonplussed Angela are standing there. Angela is holding a stack of pizzas. She glances my way then purposely looks another direction.)"

  show anon zorder 4 at center
  show angela zorder 1 at left

  anon "Thic Pies. We have an extra large order here."
  anon "Uh… you did order 150 pizzas… right?"
  mc "I most certainly did."
  ang "..."
  anon "Great! Well, we can start getting them from the cars-"
  ang "Sure is a lot pizzas for one dude."
  "(The delivery girls cuts an angry glance at Angela)"
  anon "Haha. I mean… It is the biggest order I've seen."
  mc "It would be. However, it's not all for me. I have a party out back."
  anon "Oh. Well that makes sense-"
  ang "You do not need this many pizzas dude."
  anon "*whispers* oh my god. Angela! What is wrong with you. Don't harass the customer."
  anon "haha. It does maybe seem like a bit much though?"
  mc "Oh? I wanted to be sure I was prepared."
  mc "And what would your recommendation be miss… Angela? Was it?"
  ang "I don't know man. If you want hella pizzas that's your business I guess."
  ang "The only thing I need to know is where to put them."
  anon "Y-Yeah. You want these inside I guess? We normally just hand them off at the door, but I'm not sure that will quite work. Haha?"
  mc "I'll show you. I have a few guys around back."
  "(They follow me around to the back of the house. There are a few event tables put out along with the beginnings of string lights and a large pavilion tent.)"
  mc "Just put them here under the pavilion there."
  anon "I'll grab some more boxes Angela!"
  "(She runs back around the house.)"
  hide anon with dissolve
  show angela at center with dissolve
  ang "What's your deal man? Are you messing with me or something?"
  mc "I'd say that's kind of presumptions isn't it?"
  ang "Yeah. I don't know. You call me. Then we get this weird order."
  mc "Well, firstly. I never called you Angela. I believe I have called Thic Pies and only twice at that. Getting you was… a happy coincidence?"
  ang "… I guess"
  "(she looks away again)"
  ang "…"
  ang "It's still weird man. Who orders that many pizzas?"
  mc "Ok, I must confess there. I did feel a little guilty for giving you such a hard time the other day. I hated to think I might be responsible for your loss of work."
  mc "I might have gone a bit overboard. (I shrug.) It can be a bit hard for me to gauge things sometimes. I should probably leave things to my manager."
  "(she looks a little confused)"
  ang "Manager? Like your boss or something?"
  mc "Haha. No, in this case I would be the boss. I run a company and I have a manager and personal assistant who helps me coordinate things. She's very good."
  ang "Oh. So you're loaded."
  mc "(I can't help but grin) Maybe. That would depend on your definition."
  ang "Yeah. I don't think that matters in this case dude."
  anon "Angela! Are you getting more pizzas! Where are you?"
  ang "I'm coming man! Chill! I have questions about the order!"
  mc "Sounds like you've got work."
  ang "Yeah."
  mc "Well. If you've got some free time after maybe you should drop by the party tonight."
  ang "Why would I crash your weird work thing?"
  mc "Free pizza? No? How about free booze?"
  mc "And hey. You delivered the pizzas in the first place. Really this party wouldn't be happening without you."
  ang "Maybe. I'll think about it."
  ang "I got stuff to do and all. So I don't know if I'll have time."
  "(The other pizza girl comes back around the house arms full of pizza boxes.)"
  anon "Angela!!!"
  ang "Dude!! Lay off!"
  mc "That's my fault, miss. I was talking to Angela about setting up a service account. After our talk, I finally see this really is far too many pizzas."
  mc "How embarrassing. I enjoy the delivery though. I'll be ordering again I'm sure."
  anon "Uh… really? Well, Ok. I do need her help though. We have so many boxes."
  mc "Of course. We were just wrapping up."
  mc "Could I get your direct line Angela?"
  ang "My what?"
  mc "So I can finalize details about the service account?"
  ang "Uh. I don't really have-"
  mc "You can just text it to me. My number is on the order. Paper is environmentally unfriendly."
  "(She looks over at the now quite impatient delivery girl.)"
  ang "Yeah. Sure."
  "(She pulls out her phone.)"

  nvl clear
  nvl show

  $ im_ang.name = "<Unkown>"
  im_ang "What are you on about man?!?{fast}"

  mc "Perfect. I got it. Thank you for your hard work ladies. I'll leave you to it."
  mc"We'll chat later Angela."

  nvl hide
  scene black
  with dissolve
  pause 2.0

  "*(bing)*"

  nvl clear
  nvl show
  $ im_ang.name = "Angela"
  im_ang "What are you on about man?!?{nw}{fast}"
  im_ang "what the hell man?!{fast}"
  im_ang "i don't know about some accounts or whatever{fast}"
  im_ang "i.{fast}"
  im_ang "deliver.{fast}"
  im_ang "pizza.{fast}"
  im_mc "I was covering for you!"
  im_mc "I'm sure you can get it done for me. Just tell your manager."
  im_ang "it does NOT work like that dude"
  im_mc "You sure? Have you tried it before?"
  im_ang "no"
  im_ang "i don't have to"
  im_mc "Well. If it bothers you, I can call in and get somebody else. I just wanted to give you the opportunity."
  im_ang "what do you mean"
  im_ang "opportunity?"
  im_mc "Landing a big account would be a good look to other employers."
  im_ang "nobody cares about a dumb take out job"
  im_mc "It's not about the job. It's about framing."
  im_mc "You aren't delivering pizza. You are signing clients onto stable accounts."
  im_ang "no dude"
  im_ang "im not"
  im_mc "If you don't want to that's fine."
  im_ang "its not"
  # "(she types and then deletes things a few times)"
  im_ang "why do you care"
  im_mc "I don't really. It goes against my nature to look the other way though."
  im_ang "that makes no sense"
  im_mc "You clearly are frustrated with your work. I hate to see good talent wasted."
  im_mc "I found my manager while she was at another job. She's the best hire I ever made."
  im_mc "It's always stuck with me."
  im_ang "so you help out some sob story"
  im_mc "No I find talent. People who are motivated. Driven."
  im_mc "People who aren't content to just let the daily grind wear them down."
  im_mc "You could say I have good taste in people."
  # "(she types and then deletes things a few times)"
  im_ang "you're weird"
  im_mc "Nothing ventured nothing gained."
  im_mc "There's always risk in business."
  im_mc "And you know I'm loaded."
  im_mc "At least I'm rich and weird. :)"
  im_mc "💸"
  pause 5
  im_ang "ill ask about the account"
  im_mc "Don't ask. Get it done. That's how you get ahead."
  im_ang "whatever"
  im_ang "rich guy"

  nvl hide
  nvl clear
  scene black
  with dissolve
  pause 2.0

  "*(bing)*"

  im_jo "Wow Jo! What a great party! I can't believe you did all that on zero notice!"
  im_jo "For your jerk of a boss!"
  im_mc "Is that a template letter? Should I sign it?"
  im_jo "😒"
  im_mc "You know you rocked it Jo. It was great."
  im_jo "Yeah. Well. No more surprise parties… please."
  im_jo "I don't know if my heart can take it."
  im_jo "Sam said something about you doing this again? You got a local deal or something? Care to comment?"
  im_mc "Yeah I didn't want to put more on your plate."
  im_mc "I got it covered."
  im_jo "Forgive my lack of faith. You got what covered."
  im_jo "Regular parties strike me as wholly unnecessary here boss."
  im_jo "Shouldn't we be focused on getting the new location open?"
  im_mc "Team morale is an important part of meeting deadlines."
  im_jo "Uh-huh."
  im_jo "And how's team morale boss? You been on site lately?"
  im_jo "I mean I certainly wouldn't know."
  im_jo "Not like I'm there every day from sunup to sun down. Making decisions, checking budgets, running operations. Y'know all the little stuff."
  im_jo "I'm sure you've got a real pulse on the team dynamic."
  im_mc "I know I've been heads down on this project."
  im_mc "But I'm picking up some of that slack starting now."
  im_mc "I've had a few breakthroughs recently and now I'm headed in a solid direction."
  im_jo "And I assume these explorative endeavours of yours will translate into actual profit somehow?"
  im_mc "Don't they always? :D"
  im_jo "Somehow…"
  im_jo "We've gotten off topic here."
  im_jo "Routine parties? No. Please. We don't need them."
  im_mc "Spoil sport."
  im_mc "I bet if we had a party every week it would only add about 2\% to the budget."
  im_mc "C'mon. I got a great hookup."
  im_jo "Ah yes. Who can resist the siren song of \"C'monnn\""
  im_jo "And \"hookup\" sounds highly encouraging."
  im_mc "I say... Yes. Routine parties."
  im_mc "Parties all around."
  im_jo "ಠ_ಠ"
  im_mc "Glad to know you're on board with this."
  im_mc "I'll text you when everything is finalized."
