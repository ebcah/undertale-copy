import pygame 
import math
import time
import keyboard
import random
pygame.init() #
frame=0
t=0
class GameSprite:
    def __init__(self, img, x, y, width, height, speed):
        self.image=pygame.transform.scale(pygame.image.load(img),(width,height))
        self.width=width
        self.height=height
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
        self.speed=speed
        
    def reset(self):
        screen.blit(self.image,(self.rect.x,self.rect.y))
left=0
right=0
up=0
down=0
class Player(GameSprite):
    
    
    def control(self,walls):
        keys = pygame.key.get_pressed()
        global frame,right,left,up,down
        
        
        if keys[pygame.K_LEFT]:
            frame+=1
            if frame%10==0:
            
                self.image=pygame.transform.scale(pygame.image.load("5/0.png"), (self.width,self.height))
                left+=1
            if frame%20==0:
                self.image=pygame.transform.scale(pygame.image.load("5/1.png"), (self.width,self.height))
                left+=1



            self.rect.x-=self.speed
            
            for i in walls:
                if pygame.sprite.collide_rect(self,i):
                    self.rect.x+=self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x+=self.speed
            frame+=1
            if frame%10==0:
            
                self.image=pygame.transform.scale(pygame.image.load("6/0.png"), (self.width,self.height))
                right+=1
            if frame%20==0:
                self.image=pygame.transform.scale(pygame.image.load("6/1.png"), (self.width,self.height))
                right+=1
            for i in walls:
                if pygame.sprite.collide_rect(self,i):
                    self.rect.x-=self.speed
        
        elif keys[pygame.K_UP]:
            self.rect.y-=self.speed
            frame+=1
            
            
            self.image=pygame.transform.scale(pygame.image.load("back.png"), (self.width,self.height))
                
            


            for i in walls:
                if pygame.sprite.collide_rect(self,i):
                    self.rect.y+=self.speed
        elif keys[pygame.K_DOWN]:
            self.rect.y+=self.speed

            frame+=1
            if frame%10==0:
            
                self.image=pygame.transform.scale(pygame.image.load("7/0.png"), (self.width,self.height))
                down+=1
            if frame%20==0:
                self.image=pygame.transform.scale(pygame.image.load("7/1.png"), (self.width,self.height))
                down+=1
            if frame%30==0:
            
                self.image=pygame.transform.scale(pygame.image.load("7/2.png"), (self.width,self.height))
                down+=1
            if frame%40==0:
                self.image=pygame.transform.scale(pygame.image.load("7/3.png"), (self.width,self.height))
                down+=1
            if self.image=="5/0.png":
                self.image=pygame.transform.scale(pygame.image.load("5/1.png"), (self.width,self.height))
            elif self.image=="6/0.png":
                self.image=pygame.transform.scale(pygame.image.load("6/1.png"), (self.width,self.height))
            elif self.image=="7/0.png" or self.image=="7/3.png":
                self.image=pygame.transform.scale(pygame.image.load("7/1.png"), (self.width,self.height))

            for i in walls:
                if pygame.sprite.collide_rect(self,i):
                    self.rect.y-=self.speed
        

        camera.center = self.rect.center
    

# задаем размеры окна
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
camera = pygame.Rect(0, 0, WINDOW_WIDTH, WINDOW_HEIGHT)
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
titles=25
background_color = (0, 0, 0)

font_path = 'DTM-Mono.otf' 
font_size = 35
font = pygame.font.Font(font_path, font_size)

text_to_type = "Long ago, two races"
text = ''
typing_speed = 100 
typing_delay = 1000 

list_wall=[
    '000000000000000000000000000000000000',
    '000000000000000000000000000000000000',
    '000666666666600000000000000000000000',
    '066211111111566000000000000000000000',# 0 стена
    '021111111111115000000000000000000000',# 1 стена
    '011111111111111000000000000000000000',# 2 блоки с заворотом на право вверх
    '011111111111111000000000000000000000',#3 блоки с заворотом налево вниз
    '011111111111111666666666666666666660',
    '031111111111111111111111111111111110',
    '003111111111111111111111111111111110',
    '000311111111140000000000000000000000',
    '000031111111400000000000000000000000',
    '000000000000000000000000000000000000',


    
]




titles=60


walls=[]
floors=[]

for i in range(len(list_wall)):
    
    for g in range(len(list_wall[i])):
        if list_wall[i][g] == '2':
            
            floors.append(GameSprite('p_v.jpg',g*titles,i*titles,titles,titles,0))
        if list_wall[i][g] == '1':
            
            floors.append(GameSprite('def.png',g*titles,i*titles,titles,titles,0))
        if list_wall[i][g] == '3':
            
            floors.append(GameSprite('p_n.jpg',g*titles,i*titles,titles,titles,0))
        if list_wall[i][g] == '4':
            
            floors.append(GameSprite('n_n.jpg',g*titles,i*titles,titles,titles,0))
        if list_wall[i][g] == '5':
            
            floors.append(GameSprite('l_v.png',g*titles,i*titles,titles,titles,0))
        if list_wall[i][g] == '6':
            
            floors.append(GameSprite('floor.png',g*titles,i*titles,titles,titles,0))
        if list_wall[i][g] == '0':
            walls.append(GameSprite('floor.png',g*titles,i*titles,titles,titles,0))


flowers= GameSprite('flowers.png',titles*3-3,titles*6-4,590,177,0)





player=Player('6/1.png',titles*7+10,titles*6,48,83,5)



pygame.time.delay(1000)
def write(text_to_type,x,y):
    time.sleep(typing_delay / 1000)
   
    for i in range(len(text_to_type)):
        global text
        text += text_to_type[i]
        text_surface = font.render(text, True, (255, 255, 255), background_color)
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)

    
        screen.blit(text_surface, text_rect)
        pygame.display.update()

       
        pygame.time.delay(typing_speed)
    text=''
def titres():
    background=GameSprite("first_image.png", 195, 10, 890, 480, 0)

    music = pygame.mixer.Sound("01.mp3")
    music.set_volume(0.75)
    music.play(1)
    background.reset()
    write('Long ago, two races',WINDOW_WIDTH//2,550)
    write('ruled over earth:',WINDOW_WIDTH//2,600)
    write('HUMANS and MONSTERS.',WINDOW_WIDTH//2,650)
    text_to_type='ruled over earth:'
    screen.fill((0, 0, 0))
    time.sleep(1)

    background=GameSprite("2.png", 200, 10, 880, 480, 0)
    background.reset()
    write('One day, war broke',WINDOW_WIDTH//2,550)
    write('out between the two',WINDOW_WIDTH//2,600)
    write('races.',WINDOW_WIDTH//2,650)
    screen.fill((0, 0, 0))
    time.sleep(1)


    background=GameSprite("3.png", 200, 10, 880, 480, 0)
    background.reset()
    write('After a long battle,',WINDOW_WIDTH//2,550)
    write('the humans were',WINDOW_WIDTH//2,600)
    write('victorious.',WINDOW_WIDTH//2,650)
    screen.fill((0, 0, 0))
    time.sleep(1)


    background=GameSprite("3.png", 200, 10, 880, 480, 0)
    background.reset()
    write('They sealed the monsters',WINDOW_WIDTH//2,550)
    write('underground with a magic',WINDOW_WIDTH//2,600)
    write('spell.',WINDOW_WIDTH//2,650)
    screen.fill((0, 0, 0))
    time.sleep(1)


    write('Many years later',WINDOW_WIDTH//2,600)
    write('.',WINDOW_WIDTH//2+5*35,600)
    write('.',WINDOW_WIDTH//2+5*35+25,600)
    write('.',WINDOW_WIDTH//2+5*35+50,600)

    screen.fill((0, 0, 0))
    time.sleep(1)






    background=GameSprite("4.png", 200, 10, 880, 480, 0)
    background.reset()
    write('MT. EBBOT',WINDOW_WIDTH//2,550)
    write('201X',WINDOW_WIDTH//2,600)

    screen.fill((0, 0, 0))
    time.sleep(1)



    background=GameSprite("5.png", 200, 10, 880, 480, 0)
    background.reset()
    write('Legends say that those ',WINDOW_WIDTH//2,550)
    write('who climb the mountain',WINDOW_WIDTH//2,600)
    write('never return.',WINDOW_WIDTH//2,650)
    screen.fill((0, 0, 0))
    time.sleep(1)

    background=GameSprite("6.png", 200, 10, 880, 480, 0)
    background.reset()
    write(' ',WINDOW_WIDTH//2,550)
    time.sleep(1)
    screen.fill((0, 0, 0))
    time.sleep(1)





    background=GameSprite("7.png", 200, 10, 880, 480, 0)
    background.reset()
    write(' ',WINDOW_WIDTH//2,550)
    time.sleep(1)
    screen.fill((0, 0, 0))
    time.sleep(1)


    background=GameSprite("8.png", 200, 10, 880, 480, 0)
    background.reset()
    write(' ',WINDOW_WIDTH//2,550)
    time.sleep(1)
    screen.fill((0, 0, 0))
    time.sleep(1)

    for i in range(87):
   
        background=GameSprite(f"video/{str(i)}.gif", 200, 10, 880, 480, 0)
        background.reset()
        pygame.display.update()
        time.sleep(0.1)
    screen.fill((0, 0, 0))
    background=GameSprite("undertale.png", 0, 0, 1024, 1024, 0)
    background.reset()
    pygame.display.update()
    time.sleep(1)
    screen.fill((0, 0, 0))





keys=pygame.key.get_pressed()


name=''

def Menu():

    screen.fill((0, 0, 0))


    background1=GameSprite("12.png", 260, 0, 760, 210, 0)
    background1.reset()
    pygame.display.update()


    background2=GameSprite("11.png", 130, 300, 1020, 440, 0)
    background2.reset()
    pygame.display.update()
    font_size = 15
    font = pygame.font.Font(font_path, font_size)
    text_surface = font.render('Created by Bohdan Bielieush', True, (255, 255, 255), background_color)

    text_rect = text_surface.get_rect()
    text_rect.center = (200, 700)










    font_size = 30
    font = pygame.font.Font(font_path, font_size)
    text_surface = font.render('New game', True, (255, 255, 0), background_color)

    text_rect = text_surface.get_rect()
    text_rect.center = (WINDOW_WIDTH//2-10, WINDOW_HEIGHT//2-50)


    screen.blit(text_surface, text_rect)
    pygame.display.update()
    keyboard.wait('enter')
    
    name()





class Player(GameSprite):
    def control(self):
        keys=pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x-=self.speed
            self.rect.x-=self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x+=self.speed
            self.rect.x+=self.speed
        if keys[pygame.K_UP]:
            self.rect.x+=self.speed
            self.rect.x+=self.speed
        if keys[pygame.K_DOWN]:
            self.rect.x+=self.speed
            self.rect.x+=self.speed
#player=Player("11.png",400,500,100,100,5)






list_wall1=['00000000000000000',
'01111111111111110',
'01111111111111110',
'01111111111111110',
'01111111111111110',
'01111111111111110',
'01111111111111110',
'01111111111111110',
'01111111111111110',
'01111111111111110',
'01111111111111110',
'01111111111111110',
'00000000000000000',]

walls1=[]
floor1=[]
for i in range(len(list_wall)):
    
    for g in range(len(list_wall[i])):
        
            
            
        if list_wall[i][g] == '1':
            floor1.append(GameSprite('floor.png',g*titles,i*titles,titles,titles,0))
        if list_wall[i][g] == '0':
            walls1.append(GameSprite('floor.png',g*titles,i*titles,titles,titles,0))


















gameov=GameSprite("over.webp", 0, 0, 1280, 720, 0)

gate=GameSprite("gate0.png", titles*30, titles*3.5, 315, 264, 0)
#473 396

flowy=GameSprite("flowey_grass.png", titles*5, titles*6, 637, 175, 0)





def write2(text_to_type,x,y,images):
    time.sleep(typing_delay / 1000)
    asd=0
    for i in range(len(text_to_type)):
        global text
        text += text_to_type[i]
        text_surface = font.render(text, True, (255, 255, 255), background_color)
        text_rect = text_surface.get_rect()
        text_rect.x=x
        text_rect.y=y
        if i% 4 == 0:
            flowy=GameSprite(images[0], 50, 20, 150, 200, 0)
        else:
            flowy=GameSprite(images[1], 50, 20, 150, 200, 0)
        flowy.reset()
        screen.blit(text_surface, text_rect)
        pygame.display.update()

       
        pygame.time.delay(typing_speed)
    text=''




def say():#picture, text
    #
    
    pygame.draw.rect(screen, (255, 255, 255),(40, 1, 1200, 300))
    pygame.draw.rect(screen, (0, 0, 0),(45, 6, 1190, 290))
    write2('*Howdy!',250,50,['flowey/0.gif','flowey/11.gif'])
    
    write2('''*I'm flowey''',250,100,['flowey/0.gif','flowey/11.gif'])
    
    write2('''*Flowey the flower!''',250,150,['flowey/0.gif','flowey/11.gif'])
    #time.sleep(1)
    pygame.draw.rect(screen, (255, 255, 255),(40, 1, 1200, 300))
    pygame.draw.rect(screen, (0, 0, 0),(45, 6, 1190, 290))
    write2('''*hee hee hee...''',250,50,['flowey/0.gif','flowey/11.gif'])
    time.sleep(1)
    pygame.draw.rect(screen, (255, 255, 255),(40, 1, 1200, 300))
    pygame.draw.rect(screen, (0, 0, 0),(45, 6, 1190, 290))
    
    write2('''*Why'd you make me introdunce myself.''',250,50,['flowey/0.gif','flowey/11.gif'])
    time.sleep(1)
    pygame.draw.rect(screen, (255, 255, 255),(40, 1, 1200, 300))
    pygame.draw.rect(screen, (0, 0, 0),(45, 6, 1190, 290))
    

    write2('''*It's rude to act like you don't know who''',250,50,['flowey/0.gif','flowey/11.gif'])#you don't know who I am.
    write2('''I am.''',250,100,['flowey/0.gif','flowey/11.gif'])
    time.sleep(1)
    pygame.draw.rect(screen, (255, 255, 255),(40, 1, 1200, 300))
    pygame.draw.rect(screen, (0, 0, 0),(45, 6, 1190, 290))

    write2('''*Someone ought to teach you proper manners.''',250,50,['flowey/0.gif','flowey/11.gif'])
    time.sleep(1)
    pygame.draw.rect(screen, (255, 255, 255),(40, 1, 1200, 300))
    pygame.draw.rect(screen, (0, 0, 0),(45, 6, 1190, 290))


    write2('''*I guess little old me will have to do.''',250,50,['flowey/0.gif','flowey/11.gif'])
    time.sleep(1)
    pygame.draw.rect(screen, (255, 255, 255),(40, 1, 1200, 300))
    pygame.draw.rect(screen, (0, 0, 0),(45, 6, 1190, 290))


    write2('''Ready?''',250,50,['flowey/0.gif','flowey/11.gif'])#you don't know who I am.
    write2('''Here we go.''',250,100,['flowey/0.gif','flowey/11.gif'])
    time.sleep(1)
    


































inventory=[]


#azxsdaaaaaaaaaaaaaaaaa

class hearts(GameSprite):
    
        
    def __init__(self,img, x, y, width, height, speed,health,inventory,damage,lvl,stadia):
        self.health=health
        self.inventory=inventory
        self.damage=damage
        self.lvl=lvl
        self.image=pygame.transform.scale(pygame.image.load(img),(width,height))
        self.width=width
        self.height=height
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
        self.speed=speed
        self.jump_height = 50
        self.stadia=stadia
        self.ground_y = 567
        self.jump_counter = 0
        self.max_jump_height = 100  # Максимальная высота прыжка
        self.jump_delay = 0.3  # Задержка перед падением
        self.jumping = False
        self.upalo=True
    def jump(self):
        self.jump_counter = 0
        self.jumping = True

    def update(self):
        if self.jumping and self.upalo:
            self.rect.y -= self.speed
            self.jump_counter += self.speed
            print(self.jump_counter)
            keyss = pygame.key.get_pressed()
            if self.rect.y < 450 or not keyss[pygame.K_UP]:
                self.jumping = False
                self.upalo = False
                self.jump_timer = pygame.time.get_ticks()  # Запоминаем время окончания прыжка
            
        elif self.stadia == "blue" and self.rect.y < self.ground_y:
            try:
                if current_time - self.jump_timer >= 600:
                    self.rect.y += self.speed
            except:
                self.rect.y += self.speed
        if not self.upalo:
            current_time = pygame.time.get_ticks()
            if current_time - self.jump_timer >= 300:  # Проверяем прошло ли 0.3 секунды
                self.upalo = False
        
        # Добавленный код для задержки на оси Y после прыжка
        if not self.jumping and not self.upalo and self.rect.y < self.ground_y:
            current_time = pygame.time.get_ticks()
            if current_time - self.jump_timer >= 300:  # Проверяем прошло ли 0.3 секунды
                keys = pygame.key.get_pressed()
                if keys[pygame.K_LEFT]:
                    self.rect.x -= self.speed
                if keys[pygame.K_RIGHT]:
                    self.rect.x += self.speed

    def control(self):
        keys = pygame.key.get_pressed()
        if self.rect.y == 569:
            self.upalo = True
        print(self.rect.y)
        if keys[pygame.K_LEFT] and self.rect.x > x_a + 137:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.x < x_a + Width_A + 113:
            self.rect.x += self.speed

        if keys[pygame.K_UP] and self.rect.y > 400 - 5 and self.stadia == "red":
            self.rect.y -= self.speed
        if keyboard.is_pressed('up') and self.stadia == "blue":
            self.jump()
            print("jump")

        if keys[pygame.K_DOWN] and self.rect.y < 600 - 31:
            self.rect.y += self.speed
        time.sleep(0.01)
            



coor=[]

uhel=0

bullets=[]

class Bullet(GameSprite):
    def __init__(self, img, x, y, width, height, speed, target_x, target_y, angle):
        super().__init__(img, x, y, width, height, speed)
        self.target_x = target_x
        self.target_y = target_y
        self.angle = angle
        self.initial_x = x  # Store the initial x position
        self.initial_y = y  # Store the initial y position
        self.passed_heart = False  # Flag to track if the bullet has passed through the heart

    def move(self):
        
        angle = math.atan2(self.target_y - self.rect.y, self.target_x - self.rect.x)  # Вычисляем угол к цели
        self.rect.x += math.cos(angle) * self.speed  # Движение по оси X с учетом угла
        self.rect.y += math.sin(angle) * self.speed  # Движение по оси Y с учетом угла
        if self.target_x==self.rect.x or self.target_y==self.rect.y:
            self.target_x=self.target_x*2
            self.target_y=self.target_y*2
heart=hearts("heart.png", player.rect.x+9, player.rect.y+30, 27, 36, 3,20,inventory,1,1,"red")

#bullets.append(bullet)




flowey_txt=True
#718 957

walk=True
def Game():
    
    



    player.rect.y=titles*10
    print(player.rect.y)
    print(player.rect.x)
    titres()
    Menu()
    
    
    
    #say()
    heart.health=10000
    atack()
    
    
def center():
     while heart.rect.x != 627 or heart.rect.y != 482:
        if heart.rect.y < 482:
            heart.rect.y += 1
        elif heart.rect.y > 482:
            heart.rect.y -= 1
            
        if heart.rect.x < 627:
            heart.rect.x += 1
        elif heart.rect.x > 627:#утт надо все
            heart.rect.x -= 1
        time.sleep(0.01)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                
        heart.control()
        heart.reset()
        pygame.display.update()
        screen.fill((0, 0, 0))

bullets=[]
Width_A=200

x_a=400

flowey=GameSprite("flowe.webp", WINDOW_WIDTH//2-58, 250, 117, 130, 0)
def menu_battle():
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255, 255, 255),(x_a+135, 395, Width_A+10, 210))
    pygame.draw.rect(screen, (0,0,0),(x_a+140, 400, Width_A, 200))
        
    font_size = 30
    font = pygame.font.Font(font_path, font_size)
    text_surface = font.render(f"lv {heart.lvl}", True, (255, 255, 255), background_color)
    text_rect = text_surface.get_rect()
    text_rect.center = (520, 630)
    font_size = 20
    screen.blit(text_surface, text_rect)
    font = pygame.font.Font(font_path, font_size)
    text_surface = font.render("HP", True, (255, 255, 0), background_color)
    text_rect = text_surface.get_rect()
    text_rect.center = (600, 630)
    screen.blit(text_surface, text_rect)
        
    pygame.draw.rect(screen, (0,255,255),(620, 615, 20*2, 30))
    pygame.draw.rect(screen, (255, 0, 0),(620, 615, heart.health*2, 30))

    flowey.reset()
    font = pygame.font.Font(font_path, font_size)
    text_surface = font.render(f"20/{heart.health}", True, (255, 255, 255), background_color)
    text_rect = text_surface.get_rect()
    text_rect.center = (700, 630)
    screen.blit(text_surface, text_rect)
    
    pygame.draw.rect(screen, (255,0,0),(620, 615, 20*2, 30))
    pygame.draw.rect(screen, (255, 255, 0),(620, 615, heart.health*2, 30))    

print(bullets)













#gsaudhgausidgasdhjagsdahgsdjgasdhagdsdasddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
heart=hearts("heart.png", player.rect.x+9, player.rect.y+30, 27, 36, 3,20,inventory,1,1,"red")
pict=0
haertss=0
bones=[]
def first_at():
    global bullets
    global haertss, heart
    bullets.append(Bullet("bullet.jpg", 500, 350, 20, 35, 2, heart.rect.x, heart.rect.y, 6))
    bullets.append(Bullet("bullet.jpg", 550, 340, 20, 35, 2, heart.rect.x, heart.rect.y, 6))
    bullets.append(Bullet("bullet.jpg", 600, 330, 20, 35, 2, heart.rect.x, heart.rect.y, 6))
    bullets.append(Bullet("bullet.jpg", 650, 330, 20, 35, 2, heart.rect.x, heart.rect.y, 6))
    bullets.append(Bullet("bullet.jpg", 700, 340, 20, 35, 2, heart.rect.x, heart.rect.y, 6))
    bullets.append(Bullet("bullet.jpg", 750, 350, 20, 35, 2, heart.rect.x, heart.rect.y, 6))
    
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        heart.control()
          # Update heart's position




        












        screen.fill((0, 0, 0))
        menu_battle()
        
        global first_atack
        player.rect.x=heart.rect.x
        player.rect.y=heart.rect.y
        print(heart.health)
        global pict
        
        for i in bullets:
            i.reset()  # Call reset() for each bullet
            i.move()  # Call move() for each bullet\
            if i.rect.x>1300 or i.rect.y>800:
                bullets.remove(i)
            
            if pygame.sprite.collide_rect(i,heart):
                heart.health=heart.health-2
                bullets.remove(i)
        if pict%2==0:
            
            for i in bullets:
                i.image=pygame.transform.scale(pygame.image.load("abullet.png"), (20,20))
        else:
            for i in bullets:
                i.image=pygame.transform.scale(pygame.image.load("bullet.png"), (20,20))
        if first_atack ==0:
            for i in bullets:
                i.move()  # Update bullet positions
                dx = heart.rect.x - i.rect.x
                dy = heart.rect.y - i.rect.y
                i.target_x=heart.rect.x
                i.target_y=heart.rect.y
                angle = math.atan2(dy, dx)
                i.angle = angle
                print(bullets)
            first_atack += 1
            
        
        
        pict+=1
        
    
        heart.reset()
        pygame.display.update()
        if len(bullets)==0:
            break



class bones_vertical(GameSprite):
    def __init__(self, img, x, y, width, height, speed, os,osob):
        super().__init__(img, x, y, width, height, speed)
        
        self.initial_x = x  
        self.initial_y = y  
        self.passed_heart = False  
        self.os=os
        self.osob=osob
    def move(self):
        
        if self.os=="x":
            self.rect.x+=self.speed
        elif self.os=="y":
            self.rect.x-=self.speed
            
            

bones=[]
def sec_atack():
    while True:
        #unnamed.png
        menu_battle()
       
        heart.control()
        heart.reset()
        pygame.display.update()
        screen.fill((0, 0, 0))
        print("ну типо да")

def atack():
    heart.rect.x=player.rect.x+9
    heart.rect.y=player.rect.y+30
    
    
        
        
    
    
    for i in range(5):
        screen.fill((0, 0, 0))
        player.reset()
        time.sleep(0.3)#0.2
        pygame.display.update()
        heart.reset()
        pygame.display.update()
        time.sleep(0.3)#0.4

    screen.fill((0, 0, 0))
   


    center()



    bon=4
    boness=True
    global bones
    global x_a,Width_A
    for i in range(1):
        for a in range(10):
            st1=0
            yss=random.randint(10,10)
            for b in range(2):
                if st1==0:
                    
                    bones.append(bones_vertical("bone.png", 235, 386, 20, 120, 3,"x","def"))
                    bones.append(bones_vertical("bone.png", 235, 600-24, 20, 20, 3,"x","def"))
                    st1+=1
                else:
                    bones.append(bones_vertical("bone.png", 1000, 386, 20, 120, 3,"y","def"))
                    bones.append(bones_vertical("bone.png", 1000, 600-24, 20, 20, 3,"y","def"))
    two_atack=[]
    for i in range(5):
        
        two_atack.append(bones_vertical("bone.png", 235, 386, 20, 20, 3,"x","blue"))
        two_atack.append(bones_vertical("BlueBone.png", 235, 386, 20, 200, 3,"x","def"))
    for i in range(5):
        two_atack.append(bones_vertical("BlueBone.png", 1000, 386, 20, 20, 3,"y","def"))
        two_atack.append(bones_vertical("bone.png", 1000, 386, 20, 200, 3,"y","blue"))
    visual_bones=bones 


    












   
    pygame.draw.rect(screen, (255, 255, 255),(535, 395, 210, 210))
    pygame.draw.rect(screen, (0,0,0),(540, 400, 200, 200))
        
    font_size = 30
    font = pygame.font.Font(font_path, font_size)
    text_surface = font.render(f"lv {heart.lvl}", True, (255, 255, 255), background_color)
    text_rect = text_surface.get_rect()
    text_rect.center = (520, 630)
    font_size = 20
    screen.blit(text_surface, text_rect)
    font = pygame.font.Font(font_path, font_size)
    text_surface = font.render("HP", True, (255, 255, 0), background_color)
    text_rect = text_surface.get_rect()
    text_rect.center = (600, 630)
    screen.blit(text_surface, text_rect)
        
    pygame.draw.rect(screen, (0,255,255),(620, 615, 20*2, 30))
    pygame.draw.rect(screen, (255, 0, 0),(620, 615, heart.health*2, 30))


    font = pygame.font.Font(font_path, font_size)
    text_surface = font.render(f"20/{heart.health}", True, (255, 255, 255), background_color)
    text_rect = text_surface.get_rect()
    text_rect.center = (700, 630)
    screen.blit(text_surface, text_rect)
        
    pygame.draw.rect(screen, (0,255,255),(620, 615, 20*2, 30))
    pygame.draw.rect(screen, (255, 0, 0),(620, 615, heart.health*2, 30))

    dialog=GameSprite("dialog.png", WINDOW_WIDTH//2, 200, 532, 230, 0)
    write2('''let me explain everything to you''',WINDOW_WIDTH//2-70,200,['flowey/0.gif','flowey/11.gif'])
        
    time.sleep(1)
    screen.fill((0, 0, 0))
    pygame.display.update()





    first_at()
    st1-=st1
    start_time = time.time()
    not_atack=[]
    while True:
        heart.image=pygame.transform.scale(pygame.image.load("asd.png"), (27,36))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        heart.stadia="blue"
        heart.control()
        current_timee = time.time()  # Получаем текущее время в секундах
    
        if current_timee - start_time >= 1.5 and len(bones)>bon:
            bon+=4
            start_time=time.time()
        if x_a>200:
            x_a-=5
            Width_A+=10
            print(Width_A)        
        heart.update()
          # Обновление позиции сердца
        screen.fill((0, 0, 0))
        menu_battle()
        heart.reset()
        for i in range(bon):
            
            
            bones[i].reset()
            bones[i].move()

            
            if pygame.sprite.collide_rect(bones[i], heart) and bones[i] not in not_atack:
                heart.health=heart.health-2
                
                not_atack.append(bones[i])
        
     
        if heart.health==0:
            while True:
                gameov.reset()
                pygame.display.update()    
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        exit()    

        if bon >= len(bones):
            break
                            
       

       
            
                
        pygame.display.update()
    start_time = time.time()    
    vt_at=1   
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        heart.update()
        heart.control()
        screen.fill((0, 0, 0))
        # Ваш код управления сердцем
        current_time=time.time()
        print(two_atack)
        if current_time - start_time >= 1 and vt_at < len(two_atack):
            vt_at += 1
            start_time = time.time()
        
        for i in range(vt_at):
            two_atack[i].move()
            two_atack[i].reset()
        if heart.health==0:
            while True:
                gameov.reset()
                pygame.display.update()    
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        exit()
            
        if pygame.sprite.collide_rect(two_atack[i], heart) and bones[i] not in not_atack:
            if two_atack[i].osob == "blue":
                if keys[pygame.K_LEFT] or keys[pygame.K_RIGHT] or keys[pygame.K_UP] or keys[pygame.K_DOWN]:
                    heart.health -= 2
                    not_atack.append(two_atack[i])
                else:
                        # Дополнительный код, если условие не выполняется
                     pass
            else:
                heart.health -= 2
                not_atack.append(two_atack[i])

        
        menu_battle()
        heart.reset()
        pygame.display.update()
        


        
        
    


        
        
        

    


























first_atack=0


def level2():
    player.rect.x=titles*10
    player.rect.y=titles*12
    player.image=pygame.transform.scale(pygame.image.load("back.png"), (48,83))
    global walk
    global game
    global flowey_txt
    
    while game:
        
        pygame.display.update()

        screen.fill((0, 0, 0))

        #say()
        pygame.time.Clock().tick(60)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False

        
        for wall in walls1:
            wall.reset()

        for floor in floor1:
            floor.reset()
        if flowey_txt:
            flowy.reset()
        player.reset()
        
        if player.rect.y>500:
            
            player.rect.y=player.rect.y-5
        
        else:
            
            
            say()
            atack()

                
                
        pygame.display.flip()
        pygame.display.update()
            
        
bullets=[] 
        















def level1():
    
    global game
    while game:
   
        screen.fill((0, 0, 0))

       
        pygame.time.Clock().tick(60)

      
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False

   
        for wall in walls:
            screen.blit(wall.image, wall.rect.move(-camera.x, -camera.y))

        for floor in floors:
            screen.blit(floor.image, floor.rect.move(-camera.x, -camera.y))

        
        player.control(walls)
        screen.blit(flowers.image, flowers.rect.move(-camera.x, -camera.y))
        
        screen.blit(gate.image, gate.rect.move(-camera.x, -camera.y))
        screen.blit(player.image, player.rect.move(-camera.x, -camera.y))
        

        pygame.display.flip()
        if player.rect.x>=titles*30+50 and player.rect.y>=titles*3.4:
            player.rect.x=titles*10
            player.rect.y=titles*12
            player.image=pygame.transform.scale(pygame.image.load("back.png"), (48,83))
            
            level2()
            break

    































alfavit_big=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
alfavit_small=[]

for i in alfavit_big:
    alfavit_small.append(i.lower())

Name=''

camera = pygame.Rect(0, 0, WINDOW_WIDTH, WINDOW_HEIGHT)
def name():
    selected_index = 0  
    selected_color = (255, 255, 0)  

    while True:
        
        selected_color = (255, 255, 255) 
        font_size = 30
        font = pygame.font.Font(font_path, font_size)
        text_surface = font.render('Name the fallen down human.', True, (255, 255, 255), background_color)
        text_rect = text_surface.get_rect()
        text_rect.center = (WINDOW_WIDTH//2-10, 100)

        screen.blit(text_surface, text_rect)
        
















        
        font_size = 30
        font = pygame.font.Font(font_path, font_size)
        if selected_index == len(alfavit_big) + len(alfavit_small) + 1:
            text_surface = font.render('Quit', True, (255,255,0), background_color)
        else:
            text_surface = font.render('Quit', True, (255,255,255), background_color)
        text_rect = text_surface.get_rect()
        text_rect.center = (100, 500)
        screen.blit(text_surface, text_rect)
        


        #print(selected_index)
        font_size = 30
        font = pygame.font.Font(font_path, font_size)
        if selected_index == len(alfavit_big) + len(alfavit_small) + 2:
            text_surface = font.render('Backspace', True, (255, 255, 0), background_color)
        else:
            text_surface = font.render('Backspace', True, (255, 255, 255), background_color)
        
        text_rect = text_surface.get_rect()
        text_rect.center = (400, 500)

        screen.blit(text_surface, text_rect)
        





        









        font_size = 30
        font = pygame.font.Font(font_path, font_size)
        if selected_index == len(alfavit_big) + len(alfavit_small) + 3:
            text_surface = font.render('Done', True, (255, 255, 0), background_color)
        else:
            text_surface = font.render('Done', True, (255, 255, 255), background_color)
        
        text_rect = text_surface.get_rect()
        text_rect.center = (700, 500)
        screen.blit(text_surface, text_rect)
        #name
        global Name
        font_size = 30
        font = pygame.font.Font(font_path, font_size)
        text_surface = font.render(Name, True, (255, 255, 255), background_color)
        
        text_rect = text_surface.get_rect()
        text_rect.center = (WINDOW_WIDTH//2, 150)
        screen.blit(text_surface, text_rect)
        pygame.display.update()



        selected_color = (255, 255, 0)  


        



        #print(Name)
        print(selected_index)






        
        for event in pygame.event.get():
            pygame.display.update()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    if selected_index==47:
                        selected_index -= 1 
                    elif selected_index==48:
                        selected_index -= 2
                    elif selected_index==49:
                        selected_index -= 3
                    else:
                        selected_index -=7
                elif event.key == pygame.K_DOWN:
                    
                        
                    selected_index +=7
                elif event.key == pygame.K_LEFT:
                    selected_index -= 1 
                elif event.key == pygame.K_RIGHT:
                    selected_index += 1 




                 
                if event.key == pygame.K_RETURN:
                    assd=0
                    for i in range(selected_index):
                        
                        if selected_index<26:
                            for a in range(len(alfavit_big)):   
                                if a==selected_index:
                                    if len(Name)<14:
                                        print(a)
                                        if assd ==0:
                                            Name=Name+alfavit_big[a]
                                            assd+=1
                                        
                                        break
                                        
                                        
                        elif i>24 and i<53:
                            for a in range(len(alfavit_small)):
                                if a+25==selected_index:
                                    if assd ==0:
                                        Name=Name+alfavit_big[a]
                                        assd+=1
                                    
                                    break
                                        
                        elif selected_index==53:
                            screen.fill((0, 0, 0))
                            Menu()
                            break
                        elif selected_index==54:
                            if len(Name)>0:
                                Name = Name[:-1]

                                break
                        elif selected_index==55:
                            if len(Name)>0:
                                player=Player('6/1.png',titles*7+10,titles*6,48,83,5)
                                
                                level1()
                                

            
            selected_index = max(0, min(selected_index, len(alfavit_big) + len(alfavit_small)+3))

            screen.fill((0, 0, 0))
            x=100
            y=200
            x1=500
            y1=200
            print(selected_index)
            for i in range(len(alfavit_big)):
                
                color = selected_color if i == selected_index else (255, 255, 255)

                text_surface = font.render(alfavit_big[i], True, color, background_color)
                text_rect = text_surface.get_rect()
                
                
                
                if x >=450:
                    x = 100
                    y += 50
                    text_rect.center = (x, y)
                else:
                    text_rect.center = (x, y)
                x += 50

                screen.blit(text_surface, text_rect)

            for i in range(len(alfavit_small)):
                
                color = selected_color if i + len(alfavit_big) == selected_index else (255, 255, 255)
                
                text_surface = font.render(alfavit_small[i], True, color, background_color)
                text_rect = text_surface.get_rect()

                
                if x1 >=850:
                    x1 = 500
                    y1 += 50
                    text_rect.center = (x1, y1)
                else:
                    text_rect.center = (x1, y1)
                x1 += 50
                
                screen.blit(text_surface, text_rect)
           
                        

   
        
        

            
























game=True
#убрать титрес
#titres()
Game()
#Menu()


while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()


    pygame.display.update()
