import pygame
import Constantes

'''       -------------------                player 1                      --------------------- '''


class Player_one():
    def __init__(self, x , y, animation): # inicia al personaje
        self.flip = False #Define la direccion del movimiento 
        self.animation = animation # recibe el tipo de movimiento
        #animacion imagen de animacion que se muestra
        self.anim_index = 0
        self.update_time = pygame.time.get_ticks()# guardamos el tiempo de ejecucion desde que comenzo pygame
        self.image = animation[self.anim_index]
        self.shape = pygame.Rect(Constantes.TAMAÑO_PERSONAJE_NORMAL) #lugar posicion y tamaño definido en clase constantes
        self.shape.center = (x,y)
        
    def move(self, delta_x, delta_y):
        if (delta_x < 0 ): #define direccion a izquierda
            self.flip = True
        if (delta_x > 0): #define direccion a derecha
            self.flip = False
        self.shape.x = self.shape.x + delta_x
        self.shape.y = self.shape.y + delta_y
        #print(self.shape.x)       
        
    def change_animation(self, animaciones_ataque):
        self.animation = animaciones_ataque
        return self.animation
    
    def posX(self):
        return self.shape.x
    
    def posY(self):
        return self.shape.y
        
    def update(self):
        cooldown_animacion = Constantes.VELOCIDAD_ANIMACION
        self.image = self.animation[self.anim_index] 
        if pygame.time.get_ticks() - self.update_time >= cooldown_animacion:
            self.anim_index = self.anim_index + 1
            self.update_time = pygame.time.get_ticks() 
        if self.anim_index >= len(self.animation):
            self.anim_index = 0
        
    def paint (self, interfaze): # indica en donde se vera el objeto y el color
        image_flip = pygame.transform.flip(self.image, self.flip, False)
        interfaze.blit(image_flip, self.shape)
        #pygame.draw.rect(interfaze,  (Constantes.COLOR_AMARILLO), self.shape, 1)

'''       -------------------                player 2                     --------------------- '''
        
class Player_two():
    def __init__(self, x , y, animation, texto): # inicia al personaje
        self.flip = True #Define la direccion del movimiento 
        self.animation = animation # recibe el tipo de movimiento
        self.texto = texto
        #animacion imagen de animacion que se muestra
        self.anim_index = 0
        self.update_time = pygame.time.get_ticks()# guardamos el tiempo de ejecucion desde que comenzo pygame
        self.image = animation[self. anim_index]
        self.shape = pygame.Rect(Constantes.TAMAÑO_PERSONAJE_NORMAL) #lugar posicion y tamaño definido en clase constantes
        self.shape.center = (x,y)
     
    def move(self, delta_x, delta_y):
        if (delta_x < 0 ): #define direccion a izquierda
            self.flip = False
        if (delta_x > 0): #define direccion a derecha
            self.flip = True
        self.shape.x = self.shape.x + delta_x
        self.shape.y = self.shape.y + delta_y
        #print(self.shape.x)       
           
    def change_animation(self, animaciones_ataque):
        self.animation = animaciones_ataque
        return self.animation
    
    def posX(self):
        return self.shape.x
    
    def posY(self):
        return self.shape.y
        
    def update(self):
        cooldown_animacion = Constantes.VELOCIDAD_ANIMACION
        self.image = self.animation[self.anim_index] 
        if pygame.time.get_ticks() - self.update_time >= cooldown_animacion:
            self.anim_index = self.anim_index + 1
            self.update_time = pygame.time.get_ticks() 
        if self.anim_index >= len(self.animation):
            if self.texto == "muerte":
                self.anim_index = 3
            else: 
                self.anim_index = 0
              
    def paint (self, interfaze): # indica en donde se vera el objeto y el color
        image_flip = pygame.transform.flip(self.image, self.flip, False)
        interfaze.blit(image_flip, self.shape)
        #pygame.draw.rect(interfaze,  (Constantes.COLOR_AMARILLO), self.shape, 1)
        
'''       -------------------                player cpu                      --------------------- '''
        
class Player_cpu():
    def __init__(self, x , y): # inicia al personaje
        self.shape = pygame.Rect(Constantes.TAMAÑO_PERSONAJE_NORMAL) #lugar posicion y tamaño definido en clase constantes
        #self.shape.center = (x,y)
        
    def paint (self, interfaze): # indica en donde se vera el objeto y el color
        pygame.draw.rect(interfaze,  (Constantes.COLOR_AZUL), self.shape)
        
'''       -------------------                line life                      --------------------- '''
class LineLife():
    def __init__(self, x , y, nivelDañoENVida): # inicia al personaje
        if nivelDañoENVida == "":
            self.shape = pygame.Rect(Constantes.TAMAÑO_LINE_DE_VIDA) #lugar posicion y tamaño definido en clase constantes
            self.shape.center = (x+180,y)
            if x == 500:
                self.color = Constantes.COLOR_AZUL
            else:
                self.color = Constantes.COLOR_VERDE
        else: 
            self.shape = pygame.Rect(Constantes.LINEA_DE_VDIA_DAÑO) #lugar posicion y tamaño definido en clase constantes
            self.shape.center = (x+180,y)
            self.color = Constantes.COLOR_ROJO
        
    def paint (self, interfaze): # indica en donde se vera el objeto y el color
        pygame.draw.rect(interfaze,  (self.color), self.shape)
        
    def update(self):
        self.shape = pygame.Rect(Constantes.LINEA_DE_VDIA_DAÑO)
        
        
        
        
        