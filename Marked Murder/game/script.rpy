# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define j = Character("Joel")
define a = Character("Adam")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

   
    play music "/audio/audioillurock.ogg"

    show Joel

    # These display lines of dialogue.

    j "Finalmente, México!"

    j "Agora só preciso me instalar em algum lugar.Mas onde seria melhor? No centro ou em um bairro quieto?"

menu:

    "No centro.":
        jump one

    "Em um bairro quieto.":
        jump book
label one:

j "Lá é muito agitado passa muita gente."

jump marry
label book:

j "Ótima escolha."

jump marry
label marry:

j "Acho que o melhor seria em um lugar calmo.Eu gosto da paz."

hide Joel

"Joel pega um táxi para o Estado do México, e encontra uma casa para alugar."

show Joel

j "Aqui parece ser perfeito, já tem até mobilias."





    # This ends the game.
