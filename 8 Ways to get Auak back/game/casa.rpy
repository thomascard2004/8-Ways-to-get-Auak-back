label cena1_casa:

    scene casa_thomas
#6
    play sound "voz/6.wav"
    eu "Hoje está um dia tão lindo."
#7 
    play sound "voz/7.wav"
    eu "O que eu quero fazer?"
#8
    play sound "voz/8.wav"
    eu "Eu poderia andar de bicicleta na ciclovia, talvez eu esbarraria com ele."
#9
    play sound "voz/9.wav"
    eu "Ou eu poderia sair andando, e ver onde eu vou parar."

    call screen casa

label cena2_casa:

    scene casa_thomas

    eu "O dia está tão lindo, mas estou com pressa."


screen casa():

    modal True

    imagebutton:
        xalign 0.0
        yalign 1.0
        idle "bicicleta"
        hover "bicicleta_hover"
        action Jump("ciclovia")

    imagebutton:
        xalign 0.9
        yalign 1.0
        idle "setadireita"
        hover "setadireita_hover"
        action Jump("vila_olimpica")