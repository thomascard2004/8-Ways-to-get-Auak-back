label ciclovia:

    scene ciclovia
#10
    play sound "voz/10.wav"
    eu "Tenho que ficar atento."
#11
    play sound "voz/11.wav"
    eu "Para não perder ele de vista."

    call screen ciclovia_tela


screen ciclovia_tela():
    
    modal True

    imagebutton:
        xalign 0.445
        yalign 0.4
        idle "setacima"
        hover "setacima_hover"
        action Jump("bar_mesquita")

