# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

default discordia = 0

default legal = 0

#=====================================================================================================
define kaua = Character("Auak")

define eu = Character("Thomas")

define misteriosa = Character("???")

define katia = Character("Mãe do Auak")

define alexia = Character("Alexia (Assistente de voz sem direitos autorais)")

define moco = Character("Corredor Aleatório")

define entre = Character("Entrevistadora")
#=====================================================================================================

image mae_kaua = Transform("mãe_kaua.png", zoom = 1.7)

image kaua_chocado = Transform("kaua_sf.png", zoom = 1.4)

image preto_correndo = Transform("preto_correndo.png", zoom = 1.5)
image preto_correndo_hover = Transform("preto_correndo.png", zoom = 1.55)

image entrevistadora = Transform("entrevistadora.png", zoom = 1.7)
#=====================================================================================================
image fundo_preto = Transform("preto.jpeg", zoom = 1.0)

image casa_thomas = Transform("casa_thomas.png", zoom = 1.25)

image quarto_thomas = Transform("quarto_thomas.png", zoom = 1.25)

image mesa_quarto = Transform("mesa_quarto.png", zoom = 1.25 )

image ciclovia = Transform("ciclovia_mesquita.png", zoom = 1.25)

image bar_mesquita = Transform("bar_mesquita.png", zoom = 1.25)

image ponto_mesquita = Transform("ponto_mesquita.png", zoom = 1.25)

image ladodela_mesquita = Transform("lado_de_la.png", zoom = 1.25)

image vilaolimpica_mesquita = Transform("vilaolimpica_mesquita.png", zoom = 1.25)

image casa_kaua = Transform("casa_kaua.png", zoom = 1.25)

image sala_kaua = Transform("sala_kaua.png", zoom = 1.25)

image quarto_kaua = Transform("quarto_kaua.png", zoom = 1.25)

image porta_kaua = Transform("porta_kaua.png", zoom = 1.25)

image 420 = Transform("420_onibus.png", zoom = 1.25)

image ct_ufrj = Transform("ct_ufrj.png", zoom = 1.25)

image ct_dentro = Transform("ct_dentro.png", zoom = 1.25)

image minerva_fora = Transform("minerva_fora.png", zoom = 1.25)

image minerva_lab = Transform("minerva_lab.png", zoom = 1.25)

image minerva_entrevista = Transform("minerva_entrevista.png", zoom = 1.25)

image corredor_H = Transform("corredor_H.png", zoom = 1.25)

image salinha_H = Transform("salinha_H.png", zoom = 1.25)

image salinha_dentro = Transform("salinha_dentro.png", zoom = 1.25)
#=====================================================================================================
image celular = Transform("celular_thomas.png", zoom = 1.0)
image celular_hover = Transform("celular_thomas.png", zoom = 1.01)

image bicicleta = Transform("bicicleta_thomas.png", zoom = 1.0)
image bicicleta_hover = Transform("bicicleta_thomas.png", zoom = 1.10)
#=====================================================================================================

image setadireita = Transform("setadireita.png", zoom = 0.3)
image setadireita_hover = Transform("setadireita.png", zoom = 0.33)

image setaesquerda = Transform("setaesquerda.png", zoom = 0.3)
image setaesquerda_hover = Transform("setaesquerda.png", zoom = 0.33)

image setacima = Transform("setacima.png", zoom = 0.3)
image setacima_hover = Transform("setacima.png", zoom = 0.33)

image setabaixo = Transform("setabaixo.png", zoom = 0.3)
image setabaixo_hover = Transform("setabaixo.png", zoom = 0.33)

# The game starts here.

label start:
    stop music
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    jump cena1_sonho
    #jump ct_fachada
    
    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # These display lines of dialogue.

    # This ends the game.

    return
