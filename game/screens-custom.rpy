transform btn_disabled:
        alpha 0.6

style phone_chat:
    xpadding 20
    ypadding 10
    xalign 0.5
    yalign 0.5
    xsize 999
    ysize 1080
    background Image("Phone-rough-v1.png")

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


screen phone_messages(dialogue, items=None):

    window:
        # style "nvl_window"
        style "phone_chat"

        frame:
            xsize 600
            ysize 900
            xalign 0.7
            yalign 0.25
            has vbox:
                spacing gui.nvl_spacing
                use nvl_dialogue(dialogue)

            ## Displays the menu, if given. The menu may be displayed incorrectly if
            ## config.narrator_menu is set to True, as it is above.
            for i in items:

                textbutton i.caption:
                    action i.action
                    style "nvl_button"

# screen im_message(name, message):
#     window:
#         background Image("gui/overlay/confirm.png")
#         vbox:
#             hbox:
#                 text name + ": " size 24 color "#fff"
#             hbox:
#                 text message size 24 color "#fff"
#             hbox:
#                 null height (24 * 1.5)

# screen chat_log(log = False):
#     window:
#         id "chatlog"
#         xpadding 20
#         ypadding 10
#         xalign 0.5
#         yalign 0.5
#         xsize 999
#         ysize 1080
#         background Image("Phone-rough-v1.png")
#         side "c b r":
#             area (100, 100, 600, 400)
#             viewport id "chatwindow":
#                 mousewheel False
#                 yinitial 0.0
#                 scrollbars None
#                 vbox:
#                     if len(log.history) > 0:
#                         for msg in log.history:
#                             use im_message(msg.name, msg.message)
#                     else:
#                         text "No messages."

# python early:
#     def parse_sms_line(lex):
#         who = lex.simple_expression()
#         what = lex.rest()
#         return (who, what)

#     def execute_sms_line(o):
#         who, what = o
#         active_phone.add_message(who, what)
#         renpy.call_screen("chat_log", active_phone)

#     def lint_sms_line(o):
#         who, what = o
#         try:
#             eval(who)
#         except:
#             renpy.error("Character not defined: %s" % who)

#         tte = renpy.check_text_tags(what)
#         if tte:
#             renpy.error(tte)

#         if active_phone is None:
#             renpy.error("You must specify an active phone.")

#     renpy.register_statement("sms", parse=parse_sms_line, execute=execute_sms_line, lint=lint_sms_line)