label cena1_quarto:

    scene quarto_thomas
    play music "fundo_jogo.wav" loop

#1  
    play sound "voz/1.wav"
    eu "Eu realmente sonhei que eu era a Adele?"
   
#2  
    play sound "voz/2.wav"
    eu "E que eu estava cantando pra ele..."
#3  
    play sound "voz/3.wav"
    eu "Misericórdia."
#4  
    play sound "voz/4.wav"
    eu "Esses sonhos tem sido cada vez mais recorrentes."
#5  
    play sound "voz/5.wav"
    eu "O que eu vou fazer agora?"

    call screen quarto_tela


label cena2_quarto:

    scene quarto_thomas

    #84
    eu "EU TÔ ATRASADO!"

    #85
    eu "Nossa, dessa vez eu ganhei um Grammy."
    #86
    eu "Depois eu penso nisso..."
    #87
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


