#image angela = "char angela doorway.png"
#image side angela = Image("char side angela neutral.png")
image side ang sad = Image("side-angela-sadv2.png")
image side ang angry = Image("side-angela-angry.png")
image side angela wtf = Image("side-angela-wtfv2.png")
image side ang happy = Image("side-angela-happy.png")

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
