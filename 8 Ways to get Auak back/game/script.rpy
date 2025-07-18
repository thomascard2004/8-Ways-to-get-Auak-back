# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define kaua = Character("Auak")

define eu = Character("Thomas")
image fundo_preto = Transform("preto.jpeg", zoom = 1.0)
image quarto_thomas = Transform("quarto_thomas.png", zoom = 1.25) 

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    jump sonho
    
    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # These display lines of dialogue.

    # This ends the game.

    return
