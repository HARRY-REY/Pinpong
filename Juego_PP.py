# !/usr/bin/env-python
# -*- coding: utf-8 -*-

import pygame,sys

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
pygame.display.set_caption("Gravedad")      # Se le pone un nombre al borde de la pantalla

# -CLASES
class Pelota:

    def __init__ ( self, x , y , radio , color ):
        self.x      = x
        self.y      = y
        self.LI     = x-radio
        self.LD     = x+radio
        self.radio  = radio
        self.color  = color
        self.grosor = 0 

    def mostrar(self):
        pygame.draw.circle ( pantalla , self.color , (  self.x , self.y ) , self.radio , self.grosor )

class Rectangulo:

    def __init__ ( self, x , y , anchura , altura , color ):
        self.x       = x
        self.y       = y
        self.xc      = 0 
        self.yc      = 0 
        self.anchura = anchura
        self.altura  = altura
        self.color   = color
        self.grosor  = 0

    def mostrar(self):
        pygame.draw.rect ( pantalla , self.color , ( self.x , self.y , self.anchura, self.altura ) , self.grosor )


# -DATOS
movimiento_AB_circulo      = 0 # Movimiento de arriba - abajo
movimiento_ID_circulo      = 0 # Movimiento de izquierda - derecha
movimiento_AB_rectangulo   = 0 # Movimiento de arriba - abajo
movimiento_AB_rectangulo_2 = 0 # Movimiento de arriba - abajo


# -OBJETOS
balon     = Pelota     ( 150 , 20 , 20 , blanco)
jugador_1 = Rectangulo ( 20  , 50 , 10 , 50 , blanco )
jugador_2 = Rectangulo ( 980 , 50 , 10 , 50 , blanco )


# -BUCLÉ 
while True:


    """
    El efecto se efectua simpre que se presione la tecla,
    cuando deja de ser presionada el movimiento es 0 
    """

    for accion in pygame.event.get():
        # Si se presiona el boton 'X' salimos
        if accion.type == pygame.QUIT:
            quit()

        # Si alguna tecla es presionada 
        elif accion.type == pygame.KEYDOWN:

            """
            MOVIMIENTO DE LA PELOTA CON LAS FLECHAS
            """
            if accion.key == pygame.K_DOWN:
                movimiento_AB_circulo    = 10
                print("Tecla ABAJO presionada")
                # Movimiento en el eje Y
                balon.y += movimiento_AB_circulo
            
            elif accion.key == pygame.K_UP:
                movimiento_AB_circulo = -10
                print("Tecla ARRIBA presionada")
                # Movimiento en el eje Y
                balon.y += movimiento_AB_circulo

            elif accion.key == pygame.K_LEFT:
                movimiento_ID_circulo = -10
                print("Tecla IZQUIERDA presionada")
                # Movimiento en el eje Y
                balon.x += movimiento_ID_circulo

            elif accion.key == pygame.K_RIGHT:
                movimiento_ID_circulo = 10
                print("Tecla DERECHA presionada")
                # Movimiento en el eje Y
                balon.x += movimiento_ID_circulo

            # MOVIMIENTO DEL RECTANGULO
            elif accion.key == pygame.K_w:
                movimiento_AB_rectangulo = -20
                jugador_1.y += movimiento_AB_rectangulo
            elif accion.key == pygame.K_s:
                movimiento_AB_rectangulo = 20
                jugador_1.y += movimiento_AB_rectangulo
            elif accion.key == pygame.K_o:
                movimiento_AB_rectangulo_2 = -20
                jugador_2.y += movimiento_AB_rectangulo_2
            elif accion.key == pygame.K_l:
                movimiento_AB_rectangulo_2 =  20
                jugador_2.y += movimiento_AB_rectangulo_2
                

        # Si alguna tecla se deja de presionar
        elif accion.type == pygame.KEYUP:
            #if accion.key == pygame.K_DOWN:
             #   movimiento_AB_circulo = 0
           # if accion.key == pygame.K_UP:
            #    movimiento_AB_circulo = 0
           # if accion.key == pygame.K_LEFT:
            #    movimiento_ID_circulo = 0
           # if accion.key == pygame.K_RIGHT:
            #    movimiento_ID_circulo = 0
            if accion.key == pygame.K_w:
                movimiento_AB_rectangulo = 0
            if accion.key == pygame.K_s:
                movimiento_AB_rectangulo = 0
            if accion.key == pygame.K_o:
                movimiento_AB_rectangulo_2 = 0
            if accion.key == pygame.K_l:
                movimiento_AB_rectangulo_2 = 0
    # ------------------------------------------------------
    # Muestra la pantalla con fondo de color
    # ------------------------------------------------------
    pantalla.fill(negro)
    # ------------------------------------------------------
    # Muestra la lina divisora
    # ------------------------------------------------------
    xi = ancho/2
    yi = 0
    xf = xi
    yf = alto
    medio = pygame.draw.line ( pantalla , blanco , ( xi , yi ) , ( xf , yf ) , 1 )

    # ------------------------------------------------------
    # Movimiento en el eje Y
    # ------------------------------------------------------
    balon.y      += movimiento_AB_circulo
    balon.x      += movimiento_ID_circulo
    jugador_1.y  += movimiento_AB_rectangulo
    jugador_2.y  += movimiento_AB_rectangulo_2
    jugador_1.yc  = jugador_1.y + jugador_1.altura
    jugador_2.yc  = jugador_2.y + jugador_2.altura
    
    # Movimiento en el eje X
    balon.x += movimiento_ID_circulo

    # ------------------------------------------------------
    # Muestra los objetos 
    # ------------------------------------------------------
    balon.mostrar()
    jugador_1.mostrar()
    jugador_2.mostrar()
    # ------------------------------------------------------
    # Perimetro de la pelota en función de un cuadrado
    # ------------------------------------------------------
    x_contorno      = balon.x-balon.radio
    y_contorno      = balon.y-balon.radio
    tamaño_contorno = balon.radio*2
    contorno        = pygame.draw.rect ( pantalla , rojo , ( x_contorno , y_contorno , tamaño_contorno , tamaño_contorno ) , 1 )
    # ------------------------------------------------------
    # Perimetro del rectangulo
    # ------------------------------------------------------
    contorno_jugador_1 = pygame.draw.rect ( pantalla , rojo , ( jugador_1.x , jugador_1.y , jugador_1.anchura , jugador_1.altura ) , 1 )
    contorno_jugador_2 = pygame.draw.rect ( pantalla , rojo , ( jugador_2.x , jugador_2.y , jugador_2.anchura , jugador_2.altura ) , 1 )

    # ------------------------------------------------------
    # Condición para no rebasar el suelo
    # ------------------------------------------------------
    # CIRCULO
    if balon.y >= alto:
        movimiento_AB_circulo *= -1
    #RECTANGULO
    if jugador_1.yc >= alto:
        movimiento_AB_rectangulo  = 0 
    if jugador_2.yc >= alto:
        movimiento_AB_rectangulo_2  = 0 


    # ------------------------------------------------------
    # Condición para no rebasar el techo
    # ------------------------------------------------------
    # CIRCULO
    if balon.y <= 0:
        movimiento_AB_circulo *= -1
    # RECTANGULO
    if jugador_1.y <= 0:
        movimiento_AB_rectangulo = 0
    if jugador_2.y <= 0:
        movimiento_AB_rectangulo_2 = 0

    # ------------------------------------------------------
    # Condición para no rebasar el lado izquierdo 
    # ------------------------------------------------------
    if balon.x <= 0:
        movimiento_ID_circulo *= -1

    # ------------------------------------------------------
    # Condición para no rebasar el lado derecho 
    # ------------------------------------------------------
    if balon.x >= ancho:
        movimiento_ID_circulo *= -1
    """
    COLISIONES
    """
    if contorno.colliderect(contorno_jugador_1):
        movimiento_AB_circulo *= -1
        movimiento_ID_circulo *= -1

    if contorno.colliderect(contorno_jugador_2):
        movimiento_AB_circulo *= -1
        movimiento_ID_circulo *= -1

    # ------------------------------------------------------
    # Manejo de la pantalla
    # ------------------------------------------------------
    pygame.display.update()

    # ------------------------------------------------------
    # Actualización de la pantalla
    # ------------------------------------------------------
    pygame.time.delay(30)
