import pygame, sys
from pygame import*  
import time   
from random import randint


volume1 = 0.2
pygame.init()
pygame.mixer.music.load("Sounds/menu_sound.ogg")
pygame.mixer.music.set_volume(volume1)
s = pygame.mixer.Sound("Sounds/button_sound.wav")
s.set_volume(volume1)
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(volume1)
gs = pygame.mixer.Sound("Sounds/game_sound.ogg")
gs.set_volume(volume1-0.1)
icon = pygame.image.load('images/icon.jpg') 
pygame.display.set_icon(icon)

SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Симулятор Шмеля")

spravka1 = pygame.image.load('images/spavka1.jpg')
spravka2 = pygame.image.load('images/spavka2.png')
BG = pygame.image.load('images/Backgraund.png')
GAME_BG = pygame.image.load('images/game_bg.jpg')
LEFT = pygame.image.load('images/left.png')
RIGHT= pygame.image.load('images/right.png')

win_ground= pygame.image.load('images/win_ground.png')

lose1_ground= pygame.image.load('images/lose_ground.png')
lose2_ground= pygame.image.load('images/lose_ground2.png')

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("fonts/font.ttf", size)

class GameSprite(sprite.Sprite):
   #конструктор класса
   def __init__(self, player_image, player_x, player_y, player_speed):
       super().__init__()
       # каждый спрайт должен хранить свойство image - изображение
       self.image = transform.scale(image.load(player_image), (100, 75))
       self.speed = player_speed
       # каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
       self.rect = self.image.get_rect()
       self.rect.x = player_x
       self.rect.y = player_y

   def reset(self):
       SCREEN.blit(self.image, (self.rect.x, self.rect.y))

class GameSprite_for_hive(sprite.Sprite):
   #конструктор класса
   def __init__(self, player_image, player_x, player_y):
       super().__init__()
       # каждый спрайт должен хранить свойство image - изображение
       self.image = transform.scale(image.load(player_image), (200, 200))
       # каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
       self.rect = self.image.get_rect()
       self.rect.x = player_x
       self.rect.y = player_y

   def reset(self):
       SCREEN.blit(self.image, (self.rect.x, self.rect.y))
#класс-наследник для спрайта-игрока (управляется стрелками)
class Player(GameSprite):
   def update(self):
       keys = key.get_pressed()
       if keys[K_LEFT] and self.rect.x > 5:
           self.rect.x -= self.speed+1
       if keys[K_RIGHT] and self.rect.x < 1280 - 80:
           self.rect.x += self.speed+1
       if keys[K_UP] and self.rect.y > 5:
           self.rect.y -= self.speed+1
       if keys[K_DOWN] and self.rect.y < 720 - 80:
           self.rect.y += self.speed+1

clock = pygame.time.Clock()  

flowers_good =['images/kol.png','images/oduvan.png','images/romka.png']
flowers_bad = ['images/zlot_geo.png','images/zloy_narcis.png']

#health
hp_bar = GameSprite('images/hp5.png',35,100,0)
hp_bar.image=transform.scale(image.load('images/hp5.png'), (200, 40))

#Honey
honey_bar = GameSprite('images/honey0.png',1120,250,0)
honey_bar.image=transform.scale(image.load('images/honey0.png'), (150, 30))

#Flowers
flower1 = GameSprite('images/Kol.png',190,380,0)
flower2 = GameSprite('images/oduvan.png',320,450,0)
flower3 = GameSprite('images/romka.png',480,500,0)
flower4 = GameSprite('images/zlot_geo.png',620,380,0)
flower5 = GameSprite('images/oduvan.png',760,500,0)
flower6 = GameSprite('images/kol.png',910,470,0)
flower8 = GameSprite('images/zloy_narcis.png',1060,420,0)

#Hive
hive = GameSprite_for_hive('images/Hive.png',1100,50)
#hive.image=transform.scale(image.load('images/hive.png'), (10, 10))
#hive.image=transform.scale(image.load('images/hive.png'), (200, 200))
#nectarinkas
nectarinka1 = GameSprite('images/yellow.png',190,380,0)
nectarinka1.image=transform.scale(image.load('images/yellow.png'), (90, 45))

nectarinka2 = GameSprite('images/yellow.png',320,450,0)
nectarinka2.image=transform.scale(image.load('images/yellow.png'), (90, 45))

nectarinka3 = GameSprite('images/yellow.png',480,500,0)
nectarinka3.image=transform.scale(image.load('images/yellow.png'), (90, 45))

nectarinka4 = GameSprite('images/yellow.png',760,500,0)
nectarinka4.image=transform.scale(image.load('images/yellow.png'), (90, 45))

nectarinka5 = GameSprite('images/yellow.png',910,470,0)
nectarinka5.image=transform.scale(image.load('images/yellow.png'), (90, 45))

nectarinki = sprite.Group()
nectarinki.add(nectarinka1)
nectarinki.add(nectarinka2)
nectarinki.add(nectarinka3)
nectarinki.add(nectarinka4)
nectarinki.add(nectarinka5)

class Button():
	def __init__(self, image, pos, text_input, font, base_color, hovering_color):
		self.image = image
		self.x_pos = pos[0]
		self.y_pos = pos[1]
		self.font = font
		self.base_color, self.hovering_color = base_color, hovering_color
		self.text_input = text_input
		self.text = self.font.render(self.text_input, True, self.base_color)
		if self.image is None:
			self.image = self.text
		self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
		self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

	def update(self, screen):
		if self.image is not None:
			screen.blit(self.image, self.rect)
		screen.blit(self.text, self.text_rect)

	def checkForInput(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			return True
		return False

	def changeColor(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			self.text = self.font.render(self.text_input, True, self.hovering_color)
		else:
			self.text = self.font.render(self.text_input, True, self.base_color)

def spavka1():
        while True:
            SCREEN.blit(spravka1,(0,0))
            SPRAVKA1_MOUSE_POS = pygame.mouse.get_pos()
       
            SPRAVKA1_BACK = Button(image=None, pos=(640, 700), 
                            text_input="BACK", font=get_font(30), base_color=(255,255,255), hovering_color=(245,225,7))

            SPRAVKA1_BACK.changeColor(SPRAVKA1_MOUSE_POS)
            SPRAVKA1_BACK.update(SCREEN)
   
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if SPRAVKA1_BACK.checkForInput(SPRAVKA1_MOUSE_POS):
                        spravka()
            pygame.display.update()
        
def spavka2():
        while True:
            SCREEN.blit(spravka2,(0,0))
            SPRAVKA2_MOUSE_POS = pygame.mouse.get_pos()
       
            SPRAVKA2_BACK = Button(image=None, pos=(640, 650), 
                            text_input="BACK", font=get_font(30), base_color=(255,255,255), hovering_color=(245,225,7))

            SPRAVKA2_BACK.changeColor(SPRAVKA2_MOUSE_POS)
            SPRAVKA2_BACK.update(SCREEN)
   
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if SPRAVKA2_BACK.checkForInput(SPRAVKA2_MOUSE_POS):
                        spravka()
            pygame.display.update()
                    
def spravka():
    while True:
        SCREEN.blit(BG,(0,0))
        SPRAVKA_MOUSE_POS = pygame.mouse.get_pos()
        SPRAVKA_BACK = Button(image=None, pos=(640, 650), 
                            text_input="BACK", font=get_font(65), base_color=(255,255,255), hovering_color=(245,225,7))
        SPRAVKA_1 = Button(image=pygame.image.load("images/Play Rect.png"), pos=(380, 300), 
                            text_input="Справка 1", font=get_font(45), base_color=(255,255,255), hovering_color=(245,225,7))
        SPRAVKA_2 = Button(image=pygame.image.load("images/Play Rect.png"), pos=(850, 300), 
                            text_input="Справка 2", font=get_font(45), base_color=(255,255,255), hovering_color=(245,225,7))
        
        for button in [SPRAVKA_BACK,SPRAVKA_1,SPRAVKA_2]:
            button.changeColor(SPRAVKA_MOUSE_POS)
            button.update(SCREEN)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if SPRAVKA_BACK.checkForInput(SPRAVKA_MOUSE_POS):
                    s.play()
                    main_menu()
                if SPRAVKA_1.checkForInput(SPRAVKA_MOUSE_POS):
                    s.play()
                    spavka1()
                if SPRAVKA_2.checkForInput(SPRAVKA_MOUSE_POS):
                    s.play()
                    spavka2()
        pygame.display.update()
                    
def play():
    shmel= sprite.Group()
    shmel_original = Player('images/shmel.png', 1000, 100, 2)
    shmel.add(shmel_original)
    proigrish= False
    finish = False
    pobeda=False
    pot_nectar=0
    pobeda=False
    nectar=18
    health=5
    golod=False
    health_bar = authors_text.render('Hp',False,(245,225,7))
    #nectar_bar = authors_text.render('Нектар в гнезде:'+str(nectar),False,(245,225,7))
    
    start_time=int(time.time())
    PLAY_BACK = Button(image=None, pos=(40, 20), 
                            text_input="BACK", font=get_font(25), base_color=(255,255,255), hovering_color=(255,0,0))
    gs.play()
    
    PLAY_MOUSE_POS = pygame.mouse.get_pos()
    PLAY_BACK.changeColor(PLAY_MOUSE_POS)
    PLAY_BACK.update(SCREEN)
    hit_True=True
    nectar_True=True
    hit_time=start_time
    honey_time=start_time
    pot_nectar_bar = authors_text.render('Семён несёт '+str(pot_nectar)+' нектара',True,(245,225,7))
    kushat = authors_text.render('Шмелята спят',True,(245,225,7))
    nov_nectar = authors_text.render('Нектар восстановился!',True,(245,225,7))
    edin=1
    nov_nectar_razr=False
    while True:
        #final = GameSprite('images/Backgraund.png', 1280 - 120, 720 - 80, 0)
        SCREEN.blit(GAME_BG,(0,0))
        pot_nectar_bar = authors_text.render('Семён несёт '+str(pot_nectar)+' нектара',True,(245,225,7))
        nectar_bar = authors_text.render('Нектар в гнезде:'+str(nectar),True,(245,225,7))
        SCREEN.blit(nectar_bar,(10,70))
        SCREEN.blit(pot_nectar_bar,(400,20))
        SCREEN.blit(kushat,(1000, 20))
        SCREEN.blit(health_bar,(0, 100))
        
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        
        new_time=int(time.time())
        if (new_time-start_time)>6:
            start_time+=6       
            if edin==1:
                kushat = authors_text.render('Шмелята поели',True,(245,225,7))
                if nectar>2:
                    nectar-=2
                    nectar_bar = authors_text.render('Нектар в гнезде:'+str(nectar),True,(245,225,7))
                else:
                    golod=True
                edin=0
            else:
                kushat = authors_text.render('Шмелята спят',True,(245,225,7))
                edin=1

        
        if (new_time-hit_time)>2:
            hit_time+=2
            hit_True=True
            nectar_True=True  
            nov_nectar_razr=False
        
        if (new_time-honey_time)>10:
            honey_time+=10
            nov_nectar_razr=True
            nectarinki.add(nectarinka1)
            nectarinki.add(nectarinka2)
            nectarinki.add(nectarinka3)
            nectarinki.add(nectarinka4)
            nectarinki.add(nectarinka5)

            
        #collides = sprite.groupcollide(shmel, nectarinki, True, True)
        for c in nectarinki:
            if sprite.collide_rect(shmel_original, c):
                c.kill()
                pot_nectar+=1
                #pot_nectar_bar = authors_text.render('Семён несёт '+str(pot_nectar)+' нектара',True,(245,225,7))
                nectar_True=False
        


        if hit_True and (sprite.collide_rect(shmel_original, flower4) or sprite.collide_rect(shmel_original, flower8)):
            if health>1:
                health-=1
            else:
                proigrish=True    
            if health==1:
                hp_bar.image=transform.scale(image.load('images/hp1.png'), (200, 40))
            elif health==2:
                hp_bar.image=transform.scale(image.load('images/hp2.png'), (200, 40))
            elif health==3:
                hp_bar.image=transform.scale(image.load('images/hp3.png'), (200, 40))
            elif health==4:
                hp_bar.image=transform.scale(image.load('images/hp4.png'), (200, 40))
            elif health==5:
                hp_bar.image=transform.scale(image.load('images/hp5.png'), (200, 40))

            hit_True=False

    
        '''if (sprite.collide_rect(shmel_original, nectarinka1) or sprite.collide_rect(shmel_original, nectarinka2) or sprite.collide_rect(shmel_original, nectarinka3) or sprite.collide_rect(shmel_original, nectarinka4) or sprite.collide_rect(shmel_original, nectarinka5)) and nectar_True:
            pot_nectar+=2
            pot_nectar_bar = authors_text.render('Семён несёт '+str(pot_nectar)+' нектара',True,'#f5e107')
            nectar_True=False'''
            
            
        if sprite.collide_rect(shmel_original, hive):
            nectar+=pot_nectar
            pot_nectar=0
            nectar_bar = authors_text.render('Нектар в гнезде:'+str(nectar),True,(245,225,7))
            #pot_nectar_bar = authors_text.render('Семён несёт 0 нектара',True,(245,225,7))
    
        if finish != True:
            flower1.reset()
            flower2.reset()
            flower3.reset()
            flower4.reset()
            flower5.reset()
            flower6.reset()
            flower8.reset()
            hive.reset()
            nectarinki.draw(SCREEN)
            hp_bar.reset()
            honey_bar.reset()
            shmel_original.update()
            shmel_original.reset()
            if nov_nectar_razr:
                SCREEN.blit(nov_nectar,(500,150))

            
            
            
            #final.reset()
            
        if proigrish:
            finish = True
            SCREEN.blit(lose1_ground, (0, 0))
            PLAY_BACK.update(SCREEN)
            gs.stop()
            
        if golod and not(proigrish) and not(nectar>=20):
            finish = True
            SCREEN.blit(lose2_ground, (0, 0))

            PLAY_BACK.update(SCREEN)
            gs.stop()
           
            
        if nectar>=20:
            pobeda=True
        if pobeda==True:
            finish = True
            SCREEN.blit(win_ground, (0, 0))
            PLAY_BACK.update(SCREEN)
            gs.stop()
            

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    gs.stop()
                    pygame.mixer.music.unpause()
                    main_menu()

        pygame.display.update()
        clock.tick(60)
#'#f5e107'
volume_text = get_font(80)
vol = volume_text.render('ГРОМКОСТЬ',True,(245,225,7))   
def options():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()
        RIGHTSTRELKA_MOUSE_POS = pygame.mouse.get_pos()
        LEFTSTRELKA_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.blit(BG,(0,0))
        SCREEN.blit(vol,(370,300))
        

        LEFTSTRELKA = Button(image=LEFT, pos=(340, 355), 
                            text_input= None, font=get_font(20), base_color=(255,255,255), hovering_color=(245,225,7))
        RIGHTSTRELKA = Button(image=RIGHT, pos=(960, 355), 
                            text_input= None, font=get_font(20), base_color=(255,255,255), hovering_color=(245,225,7))
        OPTIONS_BACK = Button(image=None, pos=(640, 650), 
                            text_input="BACK", font=get_font(65), base_color=(255,255,255), hovering_color=(245,225,7))

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)
        LEFTSTRELKA.update(SCREEN)
        RIGHTSTRELKA.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                global volume1
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    s.play()
                    main_menu()
                if LEFTSTRELKA.checkForInput(LEFTSTRELKA_MOUSE_POS):
                    volume1 = volume1-0.2
                    pygame.mixer.music.set_volume(volume1)
                    gs.set_volume(volume1-0.1)
                if RIGHTSTRELKA.checkForInput(RIGHTSTRELKA_MOUSE_POS):
                    volume1 = volume1+0.2
                    pygame.mixer.music.set_volume(volume1)
                    gs.set_volume(volume1-0.1)

        pygame.display.update()
        clock.tick(60)
        
        
#добавил текст авторов
authors_text = get_font(25)
authors = authors_text.render('Авторы:Акулов Данил, Аксенов Александр.',True,(245,225,7))
nastav = authors_text.render('Наставник: Анастасия Казаченко.',True,(245,225,7))

win = authors_text.render('YOU WIN!', True, (255, 215, 0))
lose = authors_text.render('YOU LOSE!', True, (180, 0, 0))

def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))
        SCREEN.blit(authors,(0,650))
        SCREEN.blit(nastav,(0,680))  

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("Симулятор шмеля", True, (245,225,7))
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        PLAY_BUTTON = Button(image=pygame.image.load("images/Play Rect.png"), pos=(640, 250), 
                            text_input="Играть", font=get_font(75), base_color=(245,225,7), hovering_color=(255,255,255))
        OPTIONS_BUTTON = Button(image=pygame.image.load("images/Options Rect.png"), pos=(640, 400), 
                            text_input="Настройки", font=get_font(75), base_color=(245,225,7), hovering_color=(255,255,255))
        QUIT_BUTTON = Button(image=pygame.image.load("images/Quit Rect.png"), pos=(640, 550), 
                            text_input="Выйти", font=get_font(75), base_color=(245,225,7), hovering_color=(255,255,255))
        SPRAVKA = Button(image=pygame.image.load("images/spravka.png"), pos=(1200,650), 
                            text_input=None, font=get_font(50), base_color=(245,225,7), hovering_color=(255,255,255))
        
        SCREEN.blit(MENU_TEXT, MENU_RECT)
        
        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON,SPRAVKA]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.mixer.music.pause()
                    s.play()
                    play()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    s.play()
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    s.play()
                    pygame.quit()
                    sys.exit()
                if SPRAVKA.checkForInput(MENU_MOUSE_POS):
                    spravka()
                    

        pygame.display.update()
        clock.tick(60)
        
main_menu()