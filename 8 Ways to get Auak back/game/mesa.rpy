label escrivaninha:

    scene mesa_quarto

    show celular:
        xalign 0.1
        yalign 0.9

    
    eu "Minha escrivaninha está tão bagunçada."

    eu "Alexia, que horas são?"

    alexia "São 15:00."

    alexia "Ainda bem que é domingo."

    alexia "Se não você teria faltado a faculdade."

    alexia "Vagabundo."

    hide celular
    
    call screen escrivaninha


screen escrivaninha():

    modal True

    imagebutton:
        xalign 0.1
        yalign 0.9
        idle "celular"
        hover "celular_hover"
        action Jump("celular")