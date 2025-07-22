label cena1_casa:

    scene casa_thomas

    eu "Hoje está um dia tão lindo."

    eu "O que eu quero fazer?"

    eu "Eu poderia andar de bicicleta na ciclovia, e talvez esbarraria com ele."

    eu "Ou eu poderia sair andando, e ver onde vou parar."

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