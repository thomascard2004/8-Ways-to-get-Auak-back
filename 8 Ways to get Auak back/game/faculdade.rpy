default entrevista = False
default humilha = False
default passou = False

label ct_fachada:

    scene ct_ufrj
    play sound "voz/96.wav"
    eu "Finalmente cheguei!"
    play sound "voz/97.wav"
    eu "Eu não tô reclamando."
    play sound "voz/98.wav"
    eu "Em breve serei um engenheiro formado."
    play sound "voz/99.wav"
    eu "Na segunda melhor instituição de ensino superior do Brasil."
    play sound "voz/100.wav"
    eu "Isso não é para qualquer um."

    jump ct_dentro1

label ct_dentro1:

    scene ct_dentro
    play sound "voz/101.wav"
    eu "Pra onde eu quero ir?"

    call screen ct_dentro1

screen ct_dentro1():

    modal True

    imagebutton:
        xalign 0.1
        yalign 0.5
        idle "setacima"
        hover "setacima_hover"
        action Jump("corredor_H1")

    imagebutton:
        xalign 0.9
        yalign 1.0
        idle "setadireita"
        hover "setadireita_hover"
        action Jump("ct_aeroespacial")

label corredor_H1:

    scene corredor_H
    play sound "voz/102.wav"
    eu "Finalmente, eu cheguei no bloco H."
    play sound "voz/103.wav"
    eu "O que eu faço agora?"

    call screen corredor_H1

screen corredor_H1():

    modal True

    imagebutton:
        xalign 0.5
        yalign 1.0
        idle "setabaixo"
        hover "setabaixo_hover"
        action Jump("corredor_H2")

label corredor_H2:

    scene salinha_H
    play sound "voz/104.wav"
    eu "Será que ele está na salinha dessa vez?"

    if entrevista:
        jump salinha_dentro2
    jump salinha_dentro1

label salinha_dentro1:

    scene salinha_dentro
    play sound "voz/105.wav"
    eu "Não tem ninguém aqui, eu posso voltar depois."

    jump ct_dentro1

label salinha_dentro2:

    scene salinha_dentro

    show kaua_chocado at center
    play sound "voz/106.wav"
    eu "Auak, você está aqui."
    play sound "voz/107.wav"
    kaua "Você é louco?"
    play sound "voz/108.wav"
    kaua "Depois de aparecer na minha casa daquele jeito."
    play sound "voz/109.wav"
    kaua "O que você estava pensando?"
    play sound "voz/110.wav"
    kaua "E agora, o que você quer?"

    if humilha:
        play sound "voz/111.wav"
        eu "Você me deve parabéns."
        play sound "voz/112.wav"
        eu "Eu entrei pra Minerva Aeroespacial."
        play sound "voz/113.wav"
        eu "Foi bem mais fácil do que você fez parecer."
        play sound "voz/114.wav"
        eu "Eu só tive que ser decente na entrevista."

        jump finale2_12

    menu:
        "Como você vai responder?"

        "Ser astuto.":
            if passou:
                $ discordia += 1
                $ print(discordia)
                play sound "voz/115.wav"
                eu "Fala comigo direito."
                play sound "voz/116.wav"
                eu "Você está falando com um estimado membro da Minerva Aeroespacial."
                play sound "voz/117.wav"
                eu "Isso mesmo."
                play sound "voz/118.wav"
                eu "Eu consegui entrar."
                play sound "voz/119.wav"
                eu "Mas sorte da próxima vez..."

                jump finale2_12

            hide kaua_chocado
            "Como você quer lacrar alguém se não foi capaz de ser melhor que ele? Seja humilde! Você também fracassou!"
            jump GAMEOVER

        "Ser paciente.":
            $ legal += 1
            $ print(legal)

            if passou:
                play sound "voz/120.wav"
                eu "Eu... só queria dizer que passei na Minerva Aeroespacial."
                play sound "voz/121.wav"
                eu "Seria legal se você tentasse de novo e a gente pudesse ser membros juntos."
                play sound "voz/122.wav"
                eu "Eu posso te dar umas dicas de profissionalismo na entrevistas, sei lá."
                play sound "voz/123.wav"
                eu "O que você me diz?"

            play sound "voz/124.wav"
            eu "Eu só queria dizer que estou com saudades."
            play sound "voz/125.wav"
            eu "De almoçar juntos."
            play sound "voz/126.wav"
            eu "De ir embora juntos."
            play sound "voz/127.wav"
            eu "Saudades de nós dois."

            jump finale2_22

    jump cena3_sonho

label ct_dentro2:

    scene ct_dentro
    play sound "voz/128.wav"
    eu "Pra onde eu quero ir agora?"

    call screen ct_dentro2

screen ct_dentro2():

    modal True

    imagebutton:
        xalign 0.1
        yalign 0.5
        idle "setacima"
        hover "setacima_hover"
        action Jump("corredor_H1")


label ct_aeroespacial:

    $ entrevista = True

    scene minerva_fora
    play sound "voz/129.wav"
    eu "Minerva Aeroespacial."
    play sound "voz/130.wav"
    eu "Na minha opinião, a melhor equipe de competição da UFRJ."
    play sound "voz/131.wav"
    eu "(Por *coincidência*, ele já tentou entrar e não conseguiu.)"
    play sound "voz/132.wav"
    eu "Acho que vou me inscrever."

    play sound "campainha.wav"

    show entrevistadora:
        xpos 0.1
        ypos 0.0

    play sound "voz/134.wav"
    entre "Oi, quem é você?"

    play sound "voz/135.wav"
    eu "Eu sou o Thomas, eu gostaria de fazer parte da equipe."

    play sound "voz/136.wav"
    entre "Você acha que tem o que precisa para entrar na equipe?"

    show entrevistadora at center

    play sound "voz/137.wav"
    eu "Com certeza."

    play sound "voz/138.wav"
    entre "Vem comigo."

    jump minerva_lab

label minerva_lab:

    scene minerva_lab

    show entrevistadora at center

    play sound "voz/139.wav"
    entre "Aqui é o nosso laboratório."

    play sound "voz/140.wav"
    entre "Vou te levar para a nossa sala de entrevistas."

    jump minerva_entrevista

label minerva_entrevista:

    scene minerva_entrevista

    show entrevistadora at center

    play sound "voz/141.wav"
    entre "Vamos começar?"

    play sound "voz/142.wav"
    entre "Porque você escolheu especificamente a nossa equipe?"

    menu:
        entre "Porque você escolheu especificamente a nossa equipe?"

        "Porque é a melhor.":
            play sound "voz/144.wav"
            eu "Eu sou o melhor em tudo que eu faço."
            play sound "voz/145.wav"
            eu "Faz sentido escolher a melhor equipe."
            play sound "voz/146.wav"
            eu "E para mim é essa!"

            jump q2

        "Eu sou apaixonado pelo Aeroespacial.":
            play sound "voz/147.wav"
            eu "Eu amo Aeroespacial."
            play sound "voz/148.wav"
            eu "Sou apaixonado por estudar constelações."
            play sound "voz/149.wav"
            eu "Quando eu era criança meu sonho era ser Astronauta."
            play sound "voz/150.wav"
            eu "(ufa, tive que improvisar essa resposta.)"

            jump q2

        "Pra fazer algo que meu ex-melhor amigo não conseguiu fazer.":

            $ humilha = True
            $ print(humilha)

            $ renpy.notify("Essa escolha terá impacto direto no futuro.")
            play sound "voz/151.wav"
            eu "Posso ser sincero?"
            play sound "voz/152.wav"
            entre "Claro, por favor."
            play sound "voz/153.wav"
            eu "Meu maior motivo é vingança."
            play sound "voz/154.wav"
            eu "Eu quero entrar para mostrar que consigo."

            jump q2

        "Escolhi aleatoriamente.":
            play sound "voz/155.wav"
            eu "Na verdade eu escolhi aleatoriamente."
            play sound "voz/156.wav"
            eu "Uni-duni-tê."
            play sound "voz/157.wav"
            eu "E essa foi a equipe que caiu."
            play sound "voz/158.wav"
            eu "Não poderia ter sido mais fácil."

            jump q2

label q2:

    scene minerva_entrevista

    show entrevistadora at center
    play sound "voz/159.wav"
    entre "Quem é o seu herói?"

    menu:
        entre "Quem é o seu herói?"

        "Neil Armstrong.":
            play sound "voz/160.wav"
            eu "(talvez se eu disser o primeiro cara a pisar na lua, eles com certeza vão me querer.)"
            play sound "voz/161.wav"
            eu "Neil Armstrong."
            play sound "voz/162.wav"
            eu "Ele é o meu heroi."

            jump q3

        "Minha mãe.":
            play sound "voz/163.wav"
            eu "(talvez eles apreciem a minha sinceridade.)"
            play sound "voz/164.wav"
            eu "Minha mãe."
            play sound "voz/165.wav"
            eu "Ela é a minha heroína."
            play sound "voz/166.wav"
            eu "Ela fez de tudo para que eu pudesse estar aqui hoje."

            jump q3

        "Homem-Aranha.":
            play sound "voz/168.wav"
            eu "(sinto que eu estou sendo literal demais.)"
            play sound "voz/167.wav"
            eu "O meu herói é o Homem-Aranha."
            play sound "voz/169.wav"
            eu "Ele é muito radical."

            jump q3

        "Luciano Hulk":

            jump q3

label q3:

    scene minerva_entrevista

    show entrevistadora at center
    play sound "voz/170.wav"
    entre "Qual seu maior defeito?"

    menu:
        entre "Qual seu maior defeito?"

        "Perfeccionismo.":
            play sound "voz/171.wav"
            eu "(Vou dar uma reposta clássica, um defeito disfarçado de qualidade.)"
            play sound "voz/172.wav"
            eu "Eu sou muito perfeccionista."

            jump q4

        "Falta de tempo.":
            play sound "voz/173.wav"
            eu "Eu diria que as vezes eu tenho pouco tempo."
            play sound "voz/174.wav"
            eu "Isso é uma coisa que eu poderia aprender a lidar melhor."
            play sound "voz/175.wav"
            eu "Organização do meu tempo."

            jump q4

        "Excesso de energia.":
            play sound "voz/176.wav"
            eu "Eu diria que eu sou muito elétrico."
            play sound "voz/177.wav"
            eu "Isso não necessariamente é ruim."
            play sound "voz/178.wav"
            eu "Mas algumas pessoas podem achar *too much*"

            jump q4

        "Eu não possuo defeitos.":
            play sound "voz/179.wav"
            eu "Defeitos? Como assim defeitos?"
            play sound "voz/180.wav"
            eu "Eu sou perfeito! Não possuo defeitos."

            jump q4

label q4:

    scene minerva_entrevista

    show entrevistadora at center
    play sound "voz/181.wav"
    entre "Qual a sua maior qualidade?"

    menu:
        entre "Qual a sua maior qualidade?"

        "Perfeccionismo.":
            play sound "voz/172.wav"
            eu "Eu sou muito perfeccionista."
            play sound "voz/183.wav"
            eu "Sempre faço de tudo para que meu trabalho seja perfeito."

            jump q5

        "Disruptividade.":
            play sound "voz/184.wav"
            eu "Eu sou muito disruptivo."
            play sound "voz/185.wav"
            eu "Eu sempre penso fora da caixa."
            play sound "voz/186.wav"
            eu "Meu próximo passo é sempre uma surpresa."

            jump q5

        "Excesso de energia.":
            play sound "voz/176.wav"
            eu "Eu diria que eu sou muito elétrico."
            play sound "voz/188.wav"
            eu  "A minha bateria nunca acaba."

            jump q5

        "Todas.":
            play sound "voz/189.wav"
            eu "Eu sou perfeito, tenho todas as qualidades."

            jump q5

label q5:

    scene minerva_entrevista

    show entrevistadora at center
    play sound "voz/190.wav"
    entre "Não tenho mais perguntas, você tem alguma pergunta para mim?"

    menu:
        entre "Não tenho mais perguntas, você tem alguma pergunta para mim?"

        "Como assim?":

            $ passou = True
            play sound "voz/191.wav"
            eu "Como assim você não tem mais perguntas sobre mim?"
            play sound "voz/192.wav"
            eu "Não ficou interessada em me conhecer melhor?"
            play sound "voz/193.wav"
            entre "Muito pelo contrário."
            play sound "voz/194.wav"
            entre "Sem mais perguntas significa que estou satisfeita."
            play sound "voz/195.wav"
            entre "Você está dentro."

            jump finale2_1

        "Qual tipo de água você seria?":

            $ humilha = False
            play sound "voz/196.wav"
            eu "Que tipo de água você seria?"
            play sound "voz/197.wav"
            entre "Que? Porque?"
            play sound "voz/198.wav"
            eu "Dependendo do que você escolher, significa como você é na hora H."
            play sound "voz/199.wav"
            entre "Isso é extremamente anti-profissional."
            play sound "voz/200.wav"
            entre "Você está fora."
            play sound "voz/201.wav"
            entre "Engraçado... só um outro candidato já me perguntou isso."
            play sound "voz/202.wav"
            entre "Ele também foi reprovado, óbvio."
            play sound "voz/203.wav"
            entre "Saia logo daqui."

            jump finale2_2
