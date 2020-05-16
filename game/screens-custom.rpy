transform btn_disabled:
        alpha 0.6

transform left_to_right:
    xalign 0.0
    linear 2.0 yalign 1.0

style phone_chat:
    xpadding 0
    ypadding 0
    xalign 0.5
    yalign 0.5
    xsize 1920
    ysize 1080
    background Image("Phone-rough-v3.png")

style phone_chat_name is nvl_label
style phone_chat_msg is nvl_dialogue

style phone_chat_name:
    xfill True
    min_width 0
    text_align 0.0
    xpos 10
    ypos 0
    xsize None
    xalign 0
    yalign 0
    color "#fff"

style phone_chat_msg:
    xfill True
    min_width 0
    text_align 0.0
    xsize None
    xpos 10
    ypos 10
    xalign 0
    yalign 0
    color "#000"

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


screen phone_notification(popup):
    zorder 10

    window:
        background "#000"
        xsize 600
        ysize 120
        xalign 0.47
        yalign 0.01
        left_padding 20
        right_padding 20
        xfill False
        hbox:
            xalign 0.5
            yalign 0.5
            text popup id "popup" xalign 0.5 yalign 0.5 size 30 color "#fff"



screen nvl(dialogue, items=None):
    window:
        # style "nvl_window"
        style "phone_chat"

        frame:
            xsize 600
            ysize 900
            xalign 0.43
            yalign 0.15
            background None
            has vbox:
                spacing gui.nvl_spacing
                use nvl_text_chat(dialogue)



screen nvl_text_chat(dialogue):
    style_prefix None

    for d in dialogue:

        window:
            id d.window_id
            background None
            ypadding 20

            vbox:
                yfit True

                text d.who:
                    id d.who_id
                    # style "phone_chat_name"
                    size (gui.text_size * 0.75)
                    xfill True
                    min_width 0
                    text_align 0.0
                    xpos 10
                    ypos 0
                    xsize None
                    xalign 0
                    yalign 0
                    color "#000"

                text d.what:
                    id d.what_id
                    # style "phone_chat_msg"
                    xfill True
                    min_width 0
                    text_align 0.0
                    xsize None
                    xpos 10
                    ypos 10
                    xalign 0
                    yalign 0
                    color "#000"


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
