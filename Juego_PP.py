# !/usr/bin/env-python
# -*- coding: utf-8 -*-

"""
    CÓDIGO HECHO POR JD 100% REAL NO FAKE
    Puedes modificarlo a gusto y diviertete
"""
from random import random, randint
import pygame, sys

pygame.init()

# -COLORES
negro    = ( 0   , 0   , 0   )
blanco   = ( 255 , 255 , 255 )
rojo     = ( 200 , 0   , 0   )
verde    = ( 0   , 200 , 00  )
azul     = ( 0   , 0   , 200 )
amarillo = ( 255 , 255 , 0   )

# -VENTANA
tamaño    = ancho,alto = 1000,500            # Tamaño de la pantalla
pantalla  = pygame.display.set_mode(tamaño) # Se cre una pantall con pygame con el tamaño prediseñado
pygame.display.set_caption("Pinpong -solo-")      # Se le pone un nombre al borde de la pantalla

# -CLASES
class Pelota:

    def __init__ ( self, x , y , radio , color ):
        self.x                = x
        self.y                = y
        self.LI               = x-radio
        self.LD               = x+radio
        self.radio            = radio
        self.color            = color
        self.grosor           = 0
        # Medidas de contorno
        self.x_c              = x-radio
        self.y_c              = y-radio
        self.diam             = radio*2
        #self.collideRect      = pygame.draw.rect ( pantalla , rojo , ( self.x_c , self.y_c , self.diam , self.diam) , 1 )


    def mostrar(self):
        pygame.draw.circle ( pantalla , self.color , (  self.x , self.y ) , self.radio , self.grosor )

    def perimetro(self):
        #collideRect = pygame.draw.rect ( pantalla , rojo , ( self.x_c , self.y_c , self.diam , self.diam) , 1 )
        pass

    


class Rectangulo:

    def __init__ ( self, x , y , anchura , altura , color ):
        self.x                  = x
        self.y                  = y
        self.anchura            = anchura
        self.altura             = altura
        self.color              = color
        self.grosor             = 0
        # Extremos de la figura
        self.xc                 = self.x + anchura
        self.yc                 = self.y + altura
        #self.collideRect        = pygame.draw.rect ( pantalla , rojo, ( self.x , self.y , self.anchura, self.altura ) , 1 )
 
    def mostrar(self):
        pygame.draw.rect ( pantalla , self.color , ( self.x , self.y , self.anchura, self.altura ) , self.grosor )
        #collideRect        = pygame.draw.rect ( pantalla , rojo, ( self.x , self.y , self.anchura, self.altura ) , 1 )



    def update(self):
        
        # Obtenemos la tecla presionada
        keys = pygame.key.get_pressed()

        # Manejo de las teclas
            # Movimiento hacia arriba y condición para no rebasar el techo
        if keys[pygame.K_UP]:
            movimiento_AB_rectangulo = -20
            return movimiento_AB_rectangulo
        if keys[pygame.K_DOWN]:
            movimiento_AB_rectangulo =  20
            return movimiento_AB_rectangulo
        

# -DATOS
movimiento_AB_circulo = 0                            # Movimiento de arriba - abajo
movimiento_ID_circulo = 0                            # Movimiento de izquierda - derecha
velocidad             = 15
largo_rec             = 120
fuente_predeterminada = pygame.font.Font( None , 30) # Datos de salida de texto
fuente_grande         = pygame.font.Font( None, 80)
limite                = 21                           # Intentos o puntaje
toque_j_b             = 0
contador              = 0
oportunidades         = limite
centro_j              = (alto/2)-(largo_rec/2)       # El jugador aparece en el centro
condicion_pause       = True 


# -OBJETOS
balon     = Pelota     ( 500, 250 , 20 , blanco)
jugador_1 = Rectangulo ( 50  , centro_j , 10 , largo_rec , blanco )
#jugador_2 = Rectangulo ( 980 , 50 , 10 , 50 , blanco )


# -BUCLÉ 
while True:

    # Número aleatorio entre 0-3
    movimiento_aleatorio = randint(0,3)
    # Datos del marcador
    marcador               = fuente_predeterminada.render(f" Rebotes: {contador}", 0, blanco) # Salida de texto
    marcador_oportunidades = fuente_predeterminada.render(f"Oportunidades: {oportunidades}", 0 , blanco)
    pause                  = fuente_predeterminada.render("Presione 'ESPACIO' para iniciar y 'c' para pausar", 0, blanco)
    ganar                  = fuente_grande.render("¡ERES LO MEJOR!", 0, verde)
    perder                 = fuente_grande.render("¡INTENTALO DE NUEVO!", 0, rojo)
    jugar_de_nuevo         = fuente_predeterminada.render("Presiona 'y' para volver a intentarlo" , 0 , blanco)

    for accion in pygame.event.get():
        # Si se presiona el boton 'X' salimos
        if accion.type == pygame.QUIT:
            quit()

        # Si alguna tecla es presionada
        elif accion.type == pygame.KEYDOWN:

            # Movimiento de manera aleatorio al presionar ESPACIO
            if accion.key == pygame.K_SPACE:

                condicion_pause = False
                # ABAJO - DERECHA
                if movimiento_aleatorio == 0:
                    movimiento_AB_circulo = velocidad 
                    movimiento_ID_circulo = velocidad 

                # ABAJO - IZQUIERDA
                if movimiento_aleatorio == 1:
                    movimiento_AB_circulo =  velocidad 
                    movimiento_ID_circulo = -velocidad

                # ARRIBA - DERECHA
                if movimiento_aleatorio == 2:
                    movimiento_AB_circulo = -velocidad
                    movimiento_ID_circulo =  velocidad

                # ARRIBA - IZQUIERDA
                if movimiento_aleatorio == 3:
                    movimiento_AB_circulo = -velocidad
                    movimiento_ID_circulo = -velocidad

            # Se detiene el movimiento si se presiona C
            if accion.key == pygame.K_c:
                condicion_pause = True
                movimiento_AB_circulo = 0
                movimiento_ID_circulo = 0
            
            # Volver a jugar
            if accion.key == pygame.K_y:
                condicion_pause       = True
                oportunidades         = limite
                contador              = 0
                balon.x               = 500
                balon.y               = 250
                movimiento_AB_circulo = 0
                movimiento_ID_circulo = 0


    # ------------------------------------------------------
    # Muestra la pantalla con fondo de color
    # ------------------------------------------------------
    pantalla.fill(negro)
    pantalla.blit(marcador,(350, 10))
    pantalla.blit(marcador_oportunidades, (550, 10))
    if condicion_pause:
        pantalla.blit(pause,(250,150))
    # ------------------------------------------------------
    # Muestra la lina divisora
    # ------------------------------------------------------
    xi    = ancho/2
    yi    = 0
    xf    = xi
    yf    = alto
    medio = pygame.draw.line ( pantalla , blanco , ( xi , yi ) , ( xf , yf ) , 1 )


    # ------------------------------------------------------
    # Muestra los objetos 
    # ------------------------------------------------------
    balon.mostrar()
    # PERIMETRO DE LOS OBJETOS
    p  = pygame.draw.rect ( pantalla , negro , ( balon.x_c , balon.y_c , balon.diam , balon.diam) , 1 )
    j1 = pygame.draw.rect ( pantalla , negro , ( jugador_1.x , jugador_1.y , jugador_1.anchura, jugador_1.altura ) , 1 )
    jugador_1.mostrar()
    #jugador_2.mostrar()

    # ------------------------------------------------------
    # LÓGICA DEL JUGADOR
    # ------------------------------------------------------
    # Guarda el valor según el movimiento, pero si no recibe nada regresa None
    # None causa un probelma al sumar porque no es nada. Asi que si 'movimiento' 
    # es igual a None le daremos el valor de 0 para evitar ese error.
    # MIENTRAS ESTE DENTRO DE LA PANTALLA
    if jugador_1.y > 0 and jugador_1.yc < alto:
        movimiento = jugador_1.update()
        if movimiento == None:
            movimiento = 0
        jugador_1.y  += movimiento
        jugador_1.yc += movimiento
    # CUANDO ESTE FUERA DE LA PANTALLA
    else:
        # SI SUPERA EL TECHO, APARECE ABAJO
        if jugador_1.y < 0:
            jugador_1.y  = alto - largo_rec - 2
            jugador_1.yc = jugador_1.y + jugador_1.altura
        # SI SUPERA EL SUELO APARECE ARRIBA
        if jugador_1.yc > alto-1:
            jugador_1.y  = 2
            jugador_1.yc = jugador_1.y + jugador_1.altura


    # Movimiento en el eje Y
    balon.y += movimiento_AB_circulo
    # Movimiento en el eje X
    balon.x += movimiento_ID_circulo
    
    # MOVIMIENTO DE PERIMETRO DE PELOTA
    balon.y_c = balon.y - balon.radio
    balon.x_c = balon.x - balon.radio

    # Condición para no rebasar el suelo 
    if balon.y >= alto:
        movimiento_AB_circulo *= -1
    # Condición para no rebasar el techo
    if balon.y <= 0:
        movimiento_AB_circulo *= -1
    # Condición para no rebasar el lado izquierdo
    if balon.x <= 0:
        #movimiento_ID_circulo *= -1
        # Movimientos si el balon llega a tocar el lado izquierdo
        ran_x                = randint(700,999)
        ran_y                = randint(10,400)
        balon.y              = ran_y
        balon.x              = ran_x
        oportunidades -      = 1
        velocidad            = randint(10,30)   # La velocidad puede variar entre 10-30
        movimiento_aleatorio = randint(0,1)     # El movimiento puede cambiar

        # ABAJO - IZQUIERDA
        if movimiento_aleatorio == 0:
            movimiento_AB_circulo =  velocidad 
            movimiento_ID_circulo = -velocidad
        # ARRIBA - IZQUIERDA
        if movimiento_aleatorio == 1:
            movimiento_AB_circulo = -velocidad
            movimiento_ID_circulo = -velocidad
    # Condiciones para no rebasar el lado derecho
    if balon.x >= ancho:
        movimiento_ID_circulo *= -1

    # ------------------------------------------------------
    # Colisión jugador - balon 
    # ------------------------------------------------------
    if j1.colliderect(p):
        # Se suma uno por cada milesima de seg en que estan en contacto los objetos
        # No se puede usar como contador por tanto se usa lo sig
        toque_j_b += 1
        # Condición para un buen conteo
        if toque_j_b > 1:
            contador += 1
            toque_j_b = 0
        # El movimiento puede cambiar
        movimiento_aleatorio = randint(0,1)
        # La velocidad puede variar entre 10-30
        velocidad = randint(10,30)

        # ABAJO - DERECHA
        if movimiento_aleatorio == 0:
            movimiento_AB_circulo = velocidad 
            movimiento_ID_circulo = velocidad 

        # ARRIBA - DERECHA
        if movimiento_aleatorio == 1:
            movimiento_AB_circulo = -velocidad
            movimiento_ID_circulo =  velocidad

    # ------------------------------------------------------
    # GANAR O PERDER (FIN DE JUEGO) 
    # ------------------------------------------------------
    #if oportunidades <= 0 or marcador >= limite:
    # GANADOR
    if contador >= limite:
        movimiento_AB_circulo = 0
        movimiento_ID_circulo = 0
        pantalla.blit(ganar,(250,250))
        pantalla.blit(jugar_de_nuevo,(350,300))
    # PERDEDOR
    if oportunidades <= 0:
        movimiento_AB_circulo = 0
        movimiento_ID_circulo = 0
        pantalla.blit(perder,(200,200))
        pantalla.blit(jugar_de_nuevo,(350,300))

    # ------------------------------------------------------
    # Actualización de la pantalla
    # ------------------------------------------------------
    pygame.display.update()
    # FPS
    pygame.time.delay(15)
