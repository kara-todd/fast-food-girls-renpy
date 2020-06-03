image angela = "char-angela-doorway-v2.png"
image angela angry = "char-angela-doorway-v2.png"
image angela sad = "char-angela-doorway-v2.png"
image angela happy = "char-angela-doorway-v2.png"
image angela wtf = "char-angela-doorway-v2.png"

image angela upset = "char-angela-doorway-v2.png"

image angela upset1 = "side-angela-upset-lips1.png"
image angela upset2 = "side-angela-upset-lips2.png"
image angela upset3 = "side-angela-upset-lips3.png"
image angela upset4 = "side-angela-upset-lips4.png"

image angela speaking:
    0.5
    "talking-angela4.png"
    0.2
    "talking-angela1.png"
    0.5
    # This will choose one of the following delays at random
    # choice:
    #     0.15
    # choice:
    #     0.05
    # choice:
    #     0.1
    "talking-angela2.png"
    0.2
    "talking-angela3.png"
    0.2
    repeat

image side angela upset = Composite(
    (374, 418),
    (0, 0), "side-angela-upset.png",
    (64, 254), WhileSpeaking("angela", "angela speaking", "talking-angela4.png"),
)

# image side angela upset:
#     choice (6.0):
#         "angela upset4"
#     choice:
#         "angela upset3"
#         pause 0.05
#         "angela upset2"
#         pause 0.05
#         "angela upset1"
#         pause 0.03
#         "angela upset2"
#         pause 0.03
#         "angela upset3"

#     pause 0.1
#     repeat



image vanessa = "vanessa.png"
image vanessa angry = "vanessa.png"
image vanessa happy = "vanessa.png"

image sam = "sam.png"
image sam happy = "sam.png"

image side angela = Image("char side angela neutral.png")
image side angela sad = Image("side-angela-sadv2.png")
image side angela angry = Image("side-angela-angry.png")
image side angela wtf = Image("side-angela-wtfv2.png")
image side angela happy = Image("side-angela-happy.png")

image side vanessa happy = Image("side-vanessa-happy.png")
image side vanessa angry = Image("side-vanessa-angry.png")

image side sam happy = Image("side-sam-rough.png")


# transform change_transform(old, new):
#     contains:
#         old
#         alpha 1.0
#         linear 0.3 alpha 0.0
#     contains:
#         new
#         alpha 0.0
#         linear 0.3 alpha 1.0

# define config.side_image_change_transform = change_transform

define config.say_attribute_transition = Dissolve(0.2, alpha=True)
