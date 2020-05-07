image angela = "char angela doorway.png"
image side angela = Image("char side angela neutral.png")

transform change_transform(old, new):
    contains:
        old
        alpha 1.0
        linear 0.3 alpha 0.0
    contains:
        new
        alpha 0.0
        linear 0.3 alpha 1.0
    
define config.side_image_change_transform = change_transform

define config.say_attribute_transition = Dissolve(0.2, alpha=True)