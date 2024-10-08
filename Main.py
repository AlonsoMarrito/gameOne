import pygame
import Constantes
from Personajes import Player_one
from Personajes import Player_two
from Personajes import Player_cpu
from Personajes import LineLife

pygame.init()  # inicializa la libreria para juegos

# datos de la ventana
window = pygame.display.set_mode((Constantes.WIDTH, Constantes.HEIGTH))
pygame.display.set_caption("Mi primer juego")  # se define el nombre de la ventana

# funcion para modificar la escala de la imagen
def scaleForImage(image, scale):
    w = image.get_width()
    h = image.get_height()
    nueva_image = pygame.transform.scale(image, (int(w * scale), int(h * scale)))
    return nueva_image

# Warrior no 1 animacion
animaciones_caminar = []  # array de imagenes
for i in range(8):
    img = pygame.image.load(f"assets//accions//characters//warrior1//walking//walker_{i}.png")
    img = scaleForImage(img, Constantes.SCALA_PERSONAJE)  # importar la funcion de la escala
    animaciones_caminar.append(img)  # mandar el array

animaciones_ataque = []
for i in range(4):
    img = pygame.image.load(f"assets//accions//characters//warrior1//atack1//attack{i}.png")
    img = scaleForImage(img, Constantes.SCALA_PERSONAJE)
    animaciones_ataque.append(img)

animaciones_ataque2 = []
for i in range(4):
    img = pygame.image.load(f"assets//accions//characters//warrior1//atack2//attack{i}.png")
    img = scaleForImage(img, Constantes.SCALA_PERSONAJE)
    animaciones_ataque2.append(img)

animaciones_defends = []
for i in range(2):
    img = pygame.image.load(f"assets//accions//characters//warrior1//defends//defend{i}.png")
    img = scaleForImage(img, Constantes.SCALA_PERSONAJE)
    animaciones_defends.append(img)

animaciones_stand_up = []
for i in range(2):
    img = pygame.image.load(f"assets//accions//characters//warrior1//stand_up//stand_up{i}.png")
    img = scaleForImage(img, Constantes.SCALA_PERSONAJE)
    animaciones_stand_up.append(img)

#############################################################################################

# craneWarrior
animaciones_caminarCraneo = []
for i in range(7):
    img = pygame.image.load(f"assets//accions//characters//craneWarrior//walking//walk{i}.png")
    img = scaleForImage(img, Constantes.SCALA_PERSONAJE)
    animaciones_caminarCraneo.append(img)

animaciones_DeadCraneo = []
for i in range(5):
    if i == 4:
        i = 3
    img = pygame.image.load(f"assets//accions//characters//craneWarrior//dead//dead{i}.png")
    img = scaleForImage(img, Constantes.SCALA_PERSONAJE)
    animaciones_DeadCraneo.append(img)

# importar a los jugadores posicion así como animación inicial
player1 = Player_one(20, 180, animaciones_stand_up)
player2 = Player_two(780, 180, animaciones_caminarCraneo, "")
lineLife1 = LineLife(500, 20, "")
lineLife2 = LineLife(20, 20, "")
lineLife1DañoDeVida = LineLife(500, 20, Constantes.DAÑO_EN_BARRA_DE_VIDA)
lineLife2DañoDeVida = LineLife(20, 20, Constantes.DAÑO_EN_BARRA_DE_VIDA)

# se definen las variables de movimiento
mover_arriba = False
mover_abajo = False
mover_izquierda = False
mover_derecha = False

reloj = pygame.time.Clock()
run = True  # variable de ejecución

while run:  # Mantiene el programa corriendo
    # se indica el tiempo
    reloj.tick(Constantes.FPS)

    # recarga el fondo
    window.fill(Constantes.COLOR_DE_FONDO)

    # calcular el movimiento del jugador
    delta_x = 0
    delta_y = 0

    # recibe los movimientos de los jugadores
    if mover_derecha == True and posXp1 < 780:
        delta_x = Constantes.VELOCIDAD_JUGADORES
    if mover_izquierda == True and posXp1 > 15:
        delta_x = -Constantes.VELOCIDAD_JUGADORES
    if mover_arriba == True:
        delta_y = -Constantes.VELOCIDAD_JUGADORES
    if mover_abajo == True:
        delta_y = Constantes.VELOCIDAD_JUGADORES

    # se importa la funcion de movimiento
    player1.move(delta_x, delta_y)

    # actualiza la animacion
    player1.update()
    player2.update()

    player1.paint(window)  # pinta o permite la visualizacion de objetos en la ventana
    player2.paint(window)
    lineLife1.paint(window)
    lineLife2.paint(window)
    lineLife1DañoDeVida.paint(window)

    for event in pygame.event.get():  # da la opcion de cerrar o permitir siga el proyecto
        if event.type == pygame.QUIT:
            run = False

        posXp1 = player1.posX()  # se obtiene la posicion en el eje x del player 1
        posYp1 = player1.posY()
        posXp2 = player2.posX()
        posYp2 = player2.posY()

        # condiciones para realizar movimiento al presionar teclas
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                mover_izquierda = True
                animaciones_actual = player1.change_animation(animaciones_caminar)
                Constantes.VELOCIDAD_JUGADORES = 3
                Constantes.VELOCIDAD_ANIMACION = 100
                player1 = Player_one(posXp1 + 10, 180, animaciones_actual)
            if event.key == pygame.K_d:
                mover_derecha = True
                mover_izquierda = False
                animaciones_actual = player1.change_animation(animaciones_caminar)
                Constantes.VELOCIDAD_JUGADORES = 3
                Constantes.VELOCIDAD_ANIMACION = 100
                player1 = Player_one(posXp1 + 10, 180, animaciones_actual)
            # if event.key == pygame.K_w:
            #     mover_arriba = True
            # if event.key == pygame.K_s:
            #     mover_abajo = True
            if event.key == pygame.K_o:
                animaciones_actual = player1.change_animation(animaciones_ataque)
                if mover_izquierda == True:
                    Constantes.VELOCIDAD_JUGADORES = 1
                else:
                    mover_derecha = True
                    Constantes.VELOCIDAD_JUGADORES = 1
                if abs(posXp1 - posXp2) <= 115:
                    Constantes.VELOCIDAD_JUGADORES = 0.00000000000001
                    Constantes.VIDA -= 20
                    print(Constantes.VIDA)
                    # lineLife1DañoDeVida.update(window)
                    if Constantes.VIDA <= 0:
                        player2 = Player_two(posXp2 - 20, 180, animaciones_DeadCraneo, "muerte")
                else:
                    player1 = Player_one(posXp1 + 10, 180, animaciones_actual)
                    Constantes.VELOCIDAD_ANIMACION = 100
            if event.key == pygame.K_p:
                animaciones_actual = player1.change_animation(animaciones_ataque2)
                if mover_izquierda == True:
                    Constantes.VELOCIDAD_JUGADORES = 0.00000000000001
                else:
                    mover_derecha = True
                    Constantes.VELOCIDAD_JUGADORES = 0.00000000000001
                if abs(posXp1 - posXp2) <= 130:
                    Constantes.VELOCIDAD_JUGADORES = 0.00000000000001
                    Constantes.VIDA = Constantes.VIDA - 30
                    print(Constantes.VIDA)
                    if Constantes.VIDA <= 0:
                        player2 = Player_two(posXp2 - 20, 180, animaciones_DeadCraneo, "muerte")
                else:
                    player1 = Player_one(posXp1 + 10, 180, animaciones_actual)
                    Constantes.VELOCIDAD_ANIMACION = 100
            if event.key == pygame.K_k:
                animaciones_actual = player1.change_animation(animaciones_defends)
                Constantes.VELOCIDAD_JUGADORES = 0.0000000000001
                player1 = Player_one(posXp1 + 10, 180, animaciones_actual)

        # condiciones para realizar movimiento al levantar teclas
        if event.type == pygame.KEYUP:  # condiciones para detener movimiento
            if event.key == pygame.K_a:
                mover_izquierda = False
                animaciones_actual = player1.change_animation(animaciones_stand_up)
                Constantes.VELOCIDAD_ANIMACION = 165
                Constantes.VELOCIDAD_JUGADORES = 0.0000000000001
                player1 = Player_one(posXp1 + 10, 180, animaciones_actual)
            if event.key == pygame.K_d:
                mover_derecha = False
                animaciones_actual = player1.change_animation(animaciones_stand_up)
                Constantes.VELOCIDAD_ANIMACION = 165
                Constantes.VELOCIDAD_JUGADORES = 3
                player1 = Player_one(posXp1 + 10, 180, animaciones_actual)
            if event.key == pygame.K_w:
                mover_arriba = False
            if event.key == pygame.K_s:
                mover_abajo = False
            if event.key == pygame.K_o:
                mover_derecha = False
                animaciones_actual = player1.change_animation(animaciones_stand_up)
                Constantes.VELOCIDAD_ANIMACION = 165
                Constantes.VELOCIDAD_JUGADORES = 0.0000000001
                player1 = Player_one(posXp1 + 10, 180, animaciones_actual)
            if event.key == pygame.K_p:
                mover_derecha = False
                animaciones_actual = player1.change_animation(animaciones_stand_up)
                Constantes.VELOCIDAD_ANIMACION = 165
                Constantes.VELOCIDAD_JUGADORES = 0.0000000001
                player1 = Player_one(posXp1 + 10, 180, animaciones_actual)
            if event.key == pygame.K_k:
                animaciones_actual = player1.change_animation(animaciones_stand_up)
                Constantes.VELOCIDAD_JUGADORES = 0.0000000001
                player1 = Player_one(posXp1 + 10, 180, animaciones_actual)

    pygame.display.update()  # hace que se actualice la ventana lo que permite el cambio de vista y movimientos