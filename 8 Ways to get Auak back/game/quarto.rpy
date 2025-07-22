label cena1_quarto:

    scene quarto_thomas

    eu "Nossa..."

    eu "Eu realmente sonhei que eu era a Adele?"

    eu "E que eu estava cantando pra ele..."

    eu "Misericórdia."

    eu "Esses sonhos tem sido cada vez mais recorrentes."

    eu "O que eu vou fazer agora?"

    call screen quarto_tela


label cena2_quarto:

    scene quarto_thomas

    eu "EU TÔ ATRASADO!"

    eu "Nossa, desa vez eu ganhei um Grammy."

    eu "Depois eu penso nisso..."

    eu "EU TENHO QUE IR PRA FACULDADE!"

    call screen quarto_tela2


screen quarto_tela():

    modal True

    imagebutton:
        xalign 0.1
        yalign 0.5
        idle "setaesquerda"
        hover "setaesquerda_hover"
        action Jump("escrivaninha")

    imagebutton:
        xalign 0.9
        yalign 1.0

        idle "setadireita"
        hover "setadireita_hover"
        action Jump("cena1_casa")


screen quarto_tela2():

    modal True

    imagebutton:
        xalign 0.1
        yalign 0.5
        idle "setaesquerda"
        hover "setaesquerda_hover"
        action Jump("escrivaninha")

    imagebutton:
        xalign 0.9
        yalign 1.0

        idle "setadireita"
        hover "setadireita_hover"
        action Jump("cena1_onibus")


