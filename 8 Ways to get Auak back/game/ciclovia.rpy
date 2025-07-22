label ciclovia:

    scene ciclovia

    eu "Tenho que ficar atento."

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

