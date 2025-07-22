label vila_olimpica:

    scene vilaolimpica_mesquita

    show preto_correndo at right

    eu "A vila Olímpica...."

    eu "A gente vinha aqui juntos no início."

    eu "Acho que ele não tá aqui agora."

    hide preto_correndo
    call screen vila_olimpica


label moco_semtempo:

    scene vilaolimpica_mesquita

    show preto_correndo at right

    eu "Moço."

    eu "O senhor viu um menino branco de olhos azuis correndo por aqui?"

    moco "Não tenho tempooo!!"

    moco "Estou ocupado treinando corrida."

    hide preto_correndo
    with moveoutright

    pause

    call screen vila_olimpica2    


screen vila_olimpica():

    modal True

    imagebutton:
        xalign 0.0
        yalign 1.0 
        idle "setaesquerda"
        hover "setaesquerda_hover"
        action Jump("cena1_casa")

    imagebutton:
        at right
        idle "preto_correndo"
        hover "preto_correndo_hover"
        action Jump("moco_semtempo")

screen vila_olimpica2():

    modal True

    imagebutton:
        xalign 0.0
        yalign 1.0 
        idle "setaesquerda"
        hover "setaesquerda_hover"
        action Jump("cena1_casa")

   