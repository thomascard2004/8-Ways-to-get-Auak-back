label bar_mesquita:

    scene bar_mesquita
#12
    play sound "voz/12.wav"
    eu "Esse lugar sempre me faz pensar nele."

    call screen barmesquita_tela



screen barmesquita_tela():

    modal True

    #seta pra ir pro ponto
    imagebutton:
        xalign 0.2
        yalign 0.5

        idle "setaesquerda"
        hover "setaesquerda_hover"
        action Jump("ponto_mesquita")

    #seta pra ir pro outro lado
    imagebutton:
        xalign 0.7
        yalign 0.2

        idle "setadireita"
        hover "setadireita_hover"

        action Jump("lado_de_la")
    

