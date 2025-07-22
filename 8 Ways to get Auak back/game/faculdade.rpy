label ct_fachada:

    scene ct_ufrj

    eu "Mais um dia."

    eu "Eu nao tô reclamando."

    eu "Em breve serei um engenheiro formado."

    eu "Na segunda melhor instituição de ensino superior do Brasil."

    eu "Isso não é para qualquer um."

    jump ct_dentro

label ct_dentro:

    scene ct_dentro


    eu "Pra onde eu quero ir?"

    call screen ct_dentro

screen ct_dentro():

    modal True

    imagebutton:
        xalign 0.1
        yalign 0.5
        idle "setacima"
        hover "setacima_hover"
        action Jump("corredor_H")

    imagebutton:
        xalign 0.9
        yalign 1.0

        idle "setadireita"
        hover "setadireita_hover"
        action Jump("ct_aeroespacial")

label corredor_H:

    scene corredor_H

    eu "Finalmente cheguei no bloco H."

    

label ct_aeroespacial:

    scene minerva_fora

    eu "Minerva Aeroespacial."

    eu "Na minha opinião, a melhor equipe de competição da UFRJ."

    eu "(Por *coincidência*, ele já tentou entrar e não conseguiu.)"

    eu "Acho que vou me inscrever."

    #barulho de campainha

    show entrevistadora:
        xpos 0.1
        ypos 0.0
    
    entre "Oi, quem é você?"

    eu "Eu sou o Thomas, eu gostaria de fazer parte da equipe."

    entre "Você acha que tem o que precisa para entrar na equipe?"

    show entrevistadora at center

    eu "Com certeza."

    entre "Vem comigo."

    jump minerva_lab

label minerva_lab:

    scene minerva_lab

    show entrevistadora at center

    entre "Aqui é o nosso laboratório."

    entre "Vou te levar para a nossa sala de entrevistas."

    jump minerva_entrevista

label minerva_entrevista:
    scene minerva_entrevista

    show entrevistadora at center

    entre "Vamos começar?"


    entre "Porque você escolheu especificamente a nossa equipe?"

    menu:
        entre "Porque você escolheu especificamente a nossa equipe?"

        "Porque é a melhor.":
            eu "Eu sou o melhor em tudo que eu faço."

            eu "Faz sentido escolher a melhor equipe."

            eu "E para mim é essa!"

            jump q2

        "Eu sou apaixonado pelo Aeroespacial.":

            eu "Eu amo Aeroespacial."

            eu "Sou apaixonado por estudar constelações."

            eu "Quando eu era criança meu sonho era ser Astronauta."

            eu "(ufa, tive que improvisar essa resposta.)"

            jump q2

        "Pra fazer algo que meu ex-melhor amigo não conseguiu fazer.":

            eu "Posso ser sincero?"

            entre "Claro, por favor."

            eu "Meu maior motivo é vingança."

            eu "Eu quero entrar para mostrar que consigo."

            jump q2

        "Escolhi aleatoriamente.":
            eu "Na verdade eu escolhi aleatoriamente."

            eu "Uni-duni-tê."

            eu "E essa foi a equipe que caiu."

            eu "Não poderia ter sido mais fácil."

            jump q2
label q2:

    scene minerva_entrevista

    show entrevistadora at center

    entre "Quem é o seu herói?"

    menu:
        entre "Quem é o seu herói?"

        "Neil Armstrong.":
            eu "(talvez se eu disser o primeiro cara a pisar na lua, com certeza eles vão me querer.)"

            eu "Neil Armstrong."

            eu "Ele é o meu heroi."

            jump q3
        
        "Minha mãe.":
            eu "(talvez eles apreciem a minha sinceridade.)"

            eu "Minha mãe."

            eu "Ela é a minha heroína."

            eu "Ela fez de tudo para que eu pudesse estar aqui hoje."

            jump q3

        "Homem-Aranha.":

            eu "(sinto que eu estou sendo literal demais.)"

            eu "O meu herói é o Homem-Aranha."

            eu "Ele é muito radical."

            jump q3

        "Luciano Hulk":

            jump q3

label q3:

    scene minerva_entrevista

    show entrevistadora at center

    entre "Qual seu maior defeito?"

    menu:
        entre "Qual seu maior defeito?"

        "Perfeccionismo.":
            eu "(Vou dar uma reposta clássica, um defeito disfarçado de qualidade.)"

            eu "Eu sou muito perfeccionista."

            jump q4

        "Falta de tempo.":

            eu "Eu diria que as vezes eu tenho pouco tempo."

            eu "Isso é uma coisa que eu poderia aprender a lidar melhor."

            eu "Organização do meu tempo."

            jump q4

        "Excesso de energia.":

            eu "Eu diria que eu sou muito elétrico."

            eu "Isso não necessariamente é ruim."

            eu "Mas algumas pessoas podem achar *too much*"

            jump q4

        "Eu não possuo defeitos.":

            eu "Defeitos? Como assim defeitos?"

            eu "Eu sou perfeito! Não possuo defeitos."

            jump q4
      

label q4:

    scene minerva_entrevista

    show entrevistadora at center

    entre "Não tenho mais perguntas, você tem alguma pergunta para mim?"

    menu:
        entre "Não tenho mais perguntas, você tem alguma pergunta para mim?"

        "Como assim?":
            eu "Como assim você não tem mais perguntas sobre mim?"

            eu "Não ficou interessada em me conhecer melhor?"

            entre "Muito pelo contrário."

            entre "Sem mais perguntas significa que estou satisfeita."

            entre "Você está dentro."

            jump finale2_1

        "Qual tipo de água você seria?":

            eu "Que tipo de água você seria?"

            entre "Que? Porque?"

            eu "Dependendo do que você escolher, signfica como você é na hora H."

            entre "Isso é extremamente anti-profissional."

            entre "Você está fora."

            entre "Engraçado... só um outro candidato já me perguntou isso."

            entre "Ele também foi reprovado, óbvio."

            entre "Saia logo daqui."

            jump finale2_2







