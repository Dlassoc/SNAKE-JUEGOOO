from pickle import TRUE
from matplotlib.pyplot import draw
import pygame
import sys
import random
from pygame.math import Vector2


class SNAKE:    

    def __init__(self):

        pygame.display.set_caption("El jueguito de la serpiente pa chucho")
        self.body = [Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)]
        self.direction = Vector2(0, 0)
        self.new_block = False

        self.head_up = pygame.image.load(
            'Graphics/head_up.png').convert_alpha()
        self.head_down = pygame.image.load(
            'Graphics/head_down.png').convert_alpha()
        self.head_right = pygame.image.load(
            'Graphics/head_right.png').convert_alpha()
        self.head_left = pygame.image.load(
            'Graphics/head_left.png').convert_alpha()
        self.tail_up = pygame.image.load(
            'Graphics/tail_up.png').convert_alpha()
        self.tail_down = pygame.image.load(
            'Graphics/tail_down.png').convert_alpha()
        self.tail_right = pygame.image.load(
            'Graphics/tail_right.png').convert_alpha()
        self.tail_left = pygame.image.load(
            'Graphics/tail_left.png').convert_alpha()
        self.body_vertical = pygame.image.load(
            'Graphics/body_vertical.png').convert_alpha()
        self.body_horizontal = pygame.image.load(
            'Graphics/body_horizontal.png').convert_alpha()
        self.body_tr = pygame.image.load(
            'Graphics/body_tr.png').convert_alpha()
        self.body_tl = pygame.image.load(
            'Graphics/body_tl.png').convert_alpha()
        self.body_br = pygame.image.load(
            'Graphics/body_br.png').convert_alpha()
        self.body_bl = pygame.image.load(
            'Graphics/body_bl.png').convert_alpha()
        self.crunch_sound = pygame.mixer.Sound('Sound/Comer.mp3')
        print(type(self.crunch_sound))

    def draw_snake(self):
        self.update_head_graphics()
        self.update_tail_graphics()

        for index, block in enumerate(self.body):
            x_pos = int(block.x * cell_size)
            y_pos = int(block.y * cell_size)
            block_rect = pygame.Rect(x_pos, y_pos, cell_size, cell_size)

            if index == 0:
                screen.blit(self.head, block_rect)
            elif index == len(self.body) - 1:
                screen.blit(self.tail, block_rect)
            else:
                previous_block = self.body[index + 1] - block
                next_block = self.body[index - 1] - block
                if previous_block.x == next_block.x:
                    screen.blit(self.body_vertical, block_rect)
                elif previous_block.y == next_block.y:
                    screen.blit(self.body_horizontal, block_rect)
                else:
                    if previous_block.x == -1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == -1:
                        screen.blit(self.body_tl, block_rect)
                    elif previous_block.x == -1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == -1:
                        screen.blit(self.body_bl, block_rect)
                    elif previous_block.x == 1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == 1:
                        screen.blit(self.body_tr, block_rect)
                    elif previous_block.x == 1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == 1:
                        screen.blit(self.body_br, block_rect)

    def update_head_graphics(self):
        head_relation = self.body[1] - self.body[0]
        if head_relation == Vector2(1, 0):
            self.head = self.head_left
        elif head_relation == Vector2(-1, 0):
            self.head = self.head_right
        elif head_relation == Vector2(0, 1):
            self.head = self.head_up
        elif head_relation == Vector2(0, -1):
            self.head = self.head_down

    def update_tail_graphics(self):
        # El -1 es la ultima posici??n del vector, el -2 el ante penultimo
        tail_relation = self.body[-2] - self.body[-1]
        if tail_relation == Vector2(1, 0):
            self.tail = self.tail_left
        elif tail_relation == Vector2(-1, 0):
            self.tail = self.tail_right
        elif tail_relation == Vector2(0, 1):
            self.tail = self.tail_up
        elif tail_relation == Vector2(0, -1):
            self.tail = self.tail_down

    def move_snake(self):
        if self.new_block == True:
            body_copy = self.body[:]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]
            self.new_block = False
        else:
            body_copy = self.body[:-1]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]

    def add_block(self):
        self.new_block = True  # Bandera, es como un condicional implicito jeje

    def play_crunch_sound(self):
        self.crunch_sound.play()

    def reset(self):
        self.body = [Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)]
        self.direction = Vector2(0, 0)


class FRUIT:

    contador_comida = 0  # La cantidad de veces que come :p

    def __init__(self):
        self.randomize()
        print(type(self.randomize))

    def draw_fruit(self):
        # Manzana
        fruit_rect = pygame.Rect(
            int(self.pos.x * cell_size), int(self.pos.y * cell_size), cell_size, cell_size)
        screen.blit(apple, fruit_rect)

    def draw_fruit2(self):
        # Sandia
        fruit_rect2 = pygame.Rect(
            int(self.pos.x * cell_size), int(self.pos.y * cell_size), cell_size, cell_size)
        screen.blit(sandia, fruit_rect2)

    def draw_fruit3(self):
        # Coco
        fruit_rect3 = pygame.Rect(
            int(self.pos.x * cell_size), int(self.pos.y * cell_size), cell_size, cell_size)
        screen.blit(coco, fruit_rect3)

    def draw_fruit4(self):
        # Pescado
        fruit_rect4 = pygame.Rect(
            int(self.pos.x * cell_size), int(self.pos.y * cell_size), cell_size, cell_size)
        screen.blit(pescado, fruit_rect4)

    def randomize(self):
        self.x = random.randint(0, cell_number - 1)
        self.y = random.randint(0, cell_number - 1)
        self.pos = Vector2(self.x, self.y)


class MAIN:

    def __init__(self):
        self.snake = SNAKE()
        self.fruit = FRUIT()
        print(type(self.snake))

    def update(self):
        self.snake.move_snake()
        self.check_collision()
        self.check_fail()

    def draw_elements(self):
        self.draw_grass()  # El draw_grass es para imprimir las frutas en pantalla

        if FRUIT.contador_comida % 6 == 1:
            self.fruit.draw_fruit3()

        elif FRUIT.contador_comida % 8 == 1:  # elif se usa para una secuancia como de preguntas, va evaluando
            self.fruit.draw_fruit2()

        elif FRUIT.contador_comida % 5 == 1:
            self.fruit.draw_fruit4()
        else:
            self.fruit.draw_fruit()  # else es un si no cumple nada, pues haga eso ultimo

        self.snake.draw_snake()
        self.draw_score()

    def check_collision(self):
        if self.fruit.pos == self.snake.body[0]:
            FRUIT.contador_comida += 1  # Si la cabeza de la serpiente es igual a la posici??n de la fruta, aumentar uno en el contador
            self.fruit.randomize()  # QUE APAREZCA UNA FRUTA EN UN LUGAR RANDOM
            self.snake.add_block()  # A??ADIR PARTE AL CUERPO DE LA SERPIENTE
            self.snake.play_crunch_sound()  # REPRODUCIR EL SONIDO DE COMER

    def check_fail(self):
        # si el cuerpo no es mayor o igual a 0
        if not 0 <= self.snake.body[0].x < cell_number or not 0 <= self.snake.body[0].y < cell_number:
            self.game_over()

        # el 1: es la excepcion de los array, no va a traer la primera posicion de los vectores
        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over()

    def game_over(self):
        self.snake.reset()

    def draw_grass(self):
        grass_color = (172, 201, 176)  # colores de fondo
        for row in range(cell_number):

            if row % 2 == 0:
                for col in range(cell_number):  # Si fuera par
                    if col % 2 == 0:
                        grass_rect = pygame.Rect(
                            col * cell_size, row * cell_size, cell_size, cell_size)
                        pygame.draw.rect(screen, grass_color, grass_rect)
            else:  # Si no es par
                for col in range(cell_number):
                    if col % 2 != 0:  # "!=" no es igual
                        grass_rect = pygame.Rect(
                            col * cell_size, row * cell_size, cell_size, cell_size)
                        pygame.draw.rect(screen, grass_color, grass_rect)

    def draw_score(self):
        # AC?? SE IMPRIME EL LARGO DE LA SERPIENTE
        score_text = str(len(self.snake.body) - 3)
        score_surface = game_font.render(score_text, True, (23, 32, 42))
        score_x = int(cell_size * cell_number - 40)
        score_y = int(cell_size * cell_number - 70)
        score_rect = score_surface.get_rect(center=(score_x, score_y))
        apple_rect = apple.get_rect(
            midright=(score_rect.left, score_rect.centery))
        bg_rect = pygame.Rect(apple_rect.left, apple_rect.top,
                              apple_rect.width + score_rect.width + 6, apple_rect.height)

        screen.blit(score_surface, score_rect)
        screen.blit(apple, apple_rect)
        screen.blit(apple, apple_rect)


WHITE = (255, 255, 255)  # color de la letra

def draw_text(surface, text, size, x, y):
    font = pygame.font.SysFont("serif", size)  # Serif es un tipo de letra
    text_surface = font.render(text, True, WHITE)  # Letra blanca
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)  # Que aparezca entre mid y top (posici??n)
    surface.blit(text_surface, text_rect)  # grenerar el recuadro de men??


def Pricipal():
    pygame.display.set_caption("El jueguito de la serpiente pa chucho")
    screen.blit(fondo, [0, 0])
    draw_text(screen, "Snake para chucho", 80, 340, 240)
    draw_text(screen, "Daniel Camilo Lasso Casta??eda", 30, 340, 320)
    draw_text(screen, "Santiago Quintero Grisales", 30, 340, 350)
    pygame.display.flip()  # nos muestra la interfaz completa
    waiting = TRUE  # con waiting, estamos diciendole al programa que espere a que cuando se pulse una tecla, inicie el juego, antes no
    while waiting:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.KEYUP:
                waiting = False


# Inicializa el modulo de mixer, el cual es el de sonido para poder aplicar los efectos del sonido
pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.init()
cell_size = 30  # tama??o de las celdas
cell_number = 23  # numero de celdas
screen = pygame.display.set_mode(
    (cell_number * cell_size, cell_number * cell_size))  # Tama??o en la pantalla

clock = pygame.time.Clock()  # clock hace referencia a los fps
apple = pygame.image.load('Comida/ManzanaMc.png').convert_alpha()
apple = pygame.transform.scale(apple, (40, 40))
sandia = pygame.image.load('Comida/SandiaMc.png').convert_alpha()
sandia = pygame.transform.scale(sandia, (40, 40))
coco = pygame.image.load('Comida/CocoMc.png').convert_alpha()
coco = pygame.transform.scale(coco, (40, 40))
pescado = pygame.image.load('Comida/PescadoMc.png').convert_alpha()
pescado = pygame.transform.scale(pescado, (40, 40))
# ac?? definimos el fondo de la pantalla emergente
fondo = pygame.image.load("Graphics/fondo_rojo.jpg")
# REDIMENSIONAMOS tama??o de la imagen
fondo = pygame.transform.scale(fondo, (1000, 800))
game_font = pygame.font.Font('Font/PoetsenOne-Regular.ttf', 25)
SCREEN_UPDATE = pygame.USEREVENT  # userevent es una funcion especial de pygame
# Hace referencia a la velocidad de la serpiente, entre mas valor mas lento, y entre mas bajo, mas rapido
pygame.time.set_timer(SCREEN_UPDATE, 85)

Pricipal()  # Llamamos a la funci??n pricipal para que salga la interf??z tipo men??
main_game = MAIN()

while True:
    for event in pygame.event.get():

        # Si el tipo de evento es igual a quitar, entonces que cierre el juego.
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == SCREEN_UPDATE:
            main_game.update()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if main_game.snake.direction.y != 1:
                    main_game.snake.direction = Vector2(0, -1)
            if event.key == pygame.K_RIGHT:
                if main_game.snake.direction.x != -1:
                    main_game.snake.direction = Vector2(1, 0)
            if event.key == pygame.K_DOWN:
                if main_game.snake.direction.y != -1:
                    main_game.snake.direction = Vector2(0, 1)
            if event.key == pygame.K_LEFT:
                if main_game.snake.direction.x != 1:
                    main_game.snake.direction = Vector2(-1, 0)

    screen.fill((26, 188, 156))  # COLORES DEL FONDO
    main_game.draw_elements()
    pygame.display.update()
    clock.tick(60)  # FPS A LOS QUE VA A CORRER EL JUEGO
