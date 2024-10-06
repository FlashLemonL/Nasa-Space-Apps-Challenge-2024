import pygame
import math
import random
import time
from sys import exit

pygame.init()
screen = pygame.display.set_mode((1280, 720), pygame.FULLSCREEN)
pygame.display.set_caption('NASA Game')
clock = pygame.time.Clock()

font1 = pygame.font.Font('font/Tiny5-Regular.ttf',(15))
font = pygame.font.Font('font/Tiny5-Regular.ttf',(20)) 
font2 = pygame.font.Font('font/Tiny5-Regular.ttf',(50)) 
font3 = pygame.font.Font('font/Tiny5-Regular.ttf',(125)) 
font4 = pygame.font.Font('font/Tiny5-Regular.ttf',(35)) 
font5 = pygame.font.Font('font/Tiny5-Regular.ttf',(45)) 

int(50)
#RigzAom
def main_menu():
    #pygame.image.load('images/Button.png')
    keys = pygame.key.get_pressed()
    fully = True
    if keys[pygame.K_TAB]:
        global credits_active
        credits_active=True
        #print('pochaco')
    else:
        credits_active=False
    if keys[pygame.K_SPACE]:
        global CharacterGo
        global Play_start
        global Airlock
        global Lab
        global Spacewalk
        global sample_fill
        global sample_empty
        global inv
        global windowinfo_blud
        global pipe 
        global pipeamt
        global pipegone
        global pipegone2
        global centri
        global windowinfo_press
        global windowinfo_blud
        global windowinfo_centri
        global windowclosed
        global closed
        global pipeshow1
        global pipeshow2
        global windowinfo_pipe

        sample_empty=True
        sample_fill=False
        pipe = True
        inv=True
        Play_start=True
        CharacterGo = True
        Airlock = False
        Lab = False
        Spacewalk = False
        windowinfo_blud=False
        closed = False
        windowclosed = False
        pipeamt=2
        pipegone=True
        pipegone2=True
        gocentri =True
        windowinfo_blud=False
        windowinfo_centri=False
        pipeshow1=False
        pipeshow2=False
        windowinfo_press=True
        windowinfo_pipe=True


        print('check')
    if keys[pygame.K_c]:
        global controls_appear
        controls_appear=True
    else:
        controls_appear=False

    if keys[pygame.K_ESCAPE]:
        pygame.quit()
        exit()
    
 
 
class Menu_player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.use = 'images/Player.jpg'
        self.original_image = pygame.image.load(self.use).convert_alpha()
        self.original_image = pygame.transform.smoothscale(self.original_image, (250, 250)).convert_alpha()
        self.image = self.original_image.convert_alpha()
        self.player_x_pos = 1000
        self.player_y_pos = 400
        self.rect = self.image.get_rect(center=(self.player_x_pos, self.player_y_pos))
        self.screen = pygame.display.set_mode((1280, 720),pygame.FULLSCREEN)

    def cursor_look(self,cursor_x,cursor_y):
        global stars_x
        global stars_y
        global stars_rect
        if cursor_x >  self.rect.centerx:
            self.use = 'images/Playermenu2.png'
            self.original_image = pygame.image.load(self.use).convert_alpha()
            self.original_image = pygame.transform.smoothscale(self.original_image, (400, 568.8)).convert_alpha()
            stars_x += 1
            #print('right')
        elif cursor_x < self.rect.centerx:
            self.use = 'images/Playermenu.png'
            self.original_image = pygame.image.load(self.use).convert_alpha()
            self.original_image = pygame.transform.smoothscale(self.original_image, (400, 568.8)).convert_alpha()
            stars_x -= 1
            #print('left')

        if cursor_x > stars_rect.centerx:
            stars_x = 3
        if cursor_x > stars_rect.centerx +100:
            stars_x = 5
        if cursor_x > stars_rect.centerx +200:
            stars_x = 10
            
        if cursor_x < stars_rect.centerx:
            stars_x = -3
        if cursor_x < stars_rect.centerx -100:
            stars_x = -5
        if cursor_x < stars_rect.centerx -200:
            stars_x = -10


        if cursor_y > stars_rect.centery:
            stars_y = 3
        if cursor_y > stars_rect.centery +100:
            stars_y = 5
        if cursor_y > stars_rect.centery +200:
            stars_y = 10
            
        if cursor_y < stars_rect.centery:
            stars_y = -3
        if cursor_y < stars_rect.centery -100:
            stars_y = -5
        if cursor_y < stars_rect.centery -200:
            stars_y = -10

        #so many if statements lil bro


    def update(self, cursor_pos):
        cursor_x, cursor_y = cursor_pos
        rel_x, rel_y = cursor_x - self.rect.centerx, cursor_y - self.rect.centery
        angle = (180 / math.pi) * -math.atan2(rel_y, rel_x)
        self.image = pygame.transform.rotate(self.original_image, angle)
        self.rect = self.image.get_rect(center=self.rect.center)
        self.leftrect = self.image.get_rect()
        self.cursor_look(cursor_x,cursor_y)



class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        global playerxpos
        global playerypos
        global wall_y
        global wall2_y
        playerxpos=640
        playerypos=360
        wall_y = 50
        wall2_y = 645
        self.original_image = pygame.image.load('images/Player2.png').convert_alpha()
        self.original_image = pygame.transform.smoothscale(self.original_image, (100, 142)).convert_alpha()
        self.image = self.original_image.convert_alpha()
        self.player_x_pos = playerxpos
        self.player_y_pos = playerypos
        self.rect = self.image.get_rect(center=(self.player_x_pos, self.player_y_pos))
        self.acc = 0.1
        self.mov_x = 0
        self.mov_y = 0 

    def player_input(self, cursor_x, cursor_y):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_BACKSPACE]: #add map
            global CharacterGo
            global Play_start
            global Airlock
            global Lab
            global Spacewalk
            global sample_fill
            global sample_empty
            global inv
            global windowinfo_blud
            global pipe 
            global pipeamt
            global pipegone
            global pipegone2
            global gocentri
            global centri
            global windowinfo_blud
            global windowinfo_centri
            global closed
            global windowclosed
            global pipeshow1
            global pipeshow2
            global windowinfo_press
            global windowinfo_pipe

            pipeshow1=False
            windowinfo_press=True
            pipeshow2=False
            sample_empty=False
            sample_fill=False
            pipe = False
            inv=False
            Play_start=False
            CharacterGo = False
            Airlock = False
            Lab = False
            Spacewalk = False
            windowinfo_blud=False
            windowinfo_pipe=True
            closed = False
            windowclosed = False
            pipeamt=2
            pipegone=True
            pipegone2=True
            gocentri =True
            windowinfo_blud=False
            windowinfo_centri=False


            self.player_x_pos = 10000
            print('falsify')

        if keys[pygame.K_b] and sample_empty:
            windowinfo_blud = True
            sample_empty = False
            sample_fill = True

        if keys[pygame.K_MINUS] and sample_fill:
            windowinfo_blud = False

        if keys[pygame.K_MINUS] and windowclosed:
            windowclosed=False
            windowinfo_centri = False

        if keys[pygame.K_MINUS] and Spacewalk:
            windowinfo_pipe = False

        if keys[pygame.K_r]:  #REMOVEEEEEEEEEEEEEEEE WHEN GAME DONE
            self.player_y_pos = 360
            self.player_x_pos = 640
            self.mov_x = 0
            self.mov_y = 0


        if keys[pygame.K_ESCAPE]:
            pygame.quit()
            exit()


        if cursor_x > self.rect.centerx:
            self.use = 'images/Player2.png'
            self.original_image = pygame.image.load(self.use).convert_alpha()
            self.original_image = pygame.transform.smoothscale(self.original_image, (100, 142)).convert_alpha()
            #print('right')
        elif cursor_x < self.rect.centerx:
            self.use = 'images/Player.png'
            self.original_image = pygame.image.load(self.use).convert_alpha()
            self.original_image = pygame.transform.smoothscale(self.original_image, (100, 142)).convert_alpha()



        if keys[pygame.K_SPACE] and cursor_x >  self.rect.centerx:
            self.mov_x -= self.acc
        elif keys[pygame.K_SPACE] and cursor_x < self.rect.centerx:
            self.mov_x += self.acc
        if keys[pygame.K_SPACE] and cursor_y > self.rect.centery:
            self.mov_y -= self.acc
        elif keys[pygame.K_SPACE] and cursor_y < self.rect.centery:
            self.mov_y += self.acc
        else:
            self.mov_x *= 0.99
            self.mov_y *= 0.99


    def collisions(self):
        global wall_x
        global wall_y
        global Airlock
        global Play_start
        global Spacewalk
        global wall2_y
        global Lab
        if self.rect.right >= 1280 and Play_start: #right
            #self.mov_x = -3
            Play_start = False
            Airlock = True
            Spacewalk = False
            Lab =False
            playerxpos = 200
            playerypos = 500
            wall_y = 50
            wall2_y = 645
            self.player_y_pos = playerypos
            self.player_x_pos = playerxpos

        if self.rect.right >= 1280 and Lab: #right
            #self.mov_x = -3
            Play_start = True
            Airlock = False
            Spacewalk = False
            Lab =False
            playerxpos = 100
            playerypos = 500
            wall_y = 50
            wall2_y = 645
            self.player_y_pos = playerypos
            self.player_x_pos = playerxpos

        elif self.rect.right >= 1280 and Play_start != True:
            self.mov_x = -3
        elif self.rect.left <= 0 and Play_start != True:
            self.mov_x = 3

        if self.rect.left <= 0 and Play_start: #left
            Play_start = False
            Lab = True
            Airlock = False
            Spacewalk = False
            playerxpos = 1100
            playerypos = 500
            wall_y = 50
            wall2_y = 645
            self.player_y_pos = playerypos
            self.player_x_pos = playerxpos

 
        if self.rect.left <= 0 and Airlock: #left
            Play_start = True
            Airlock = False
            Spacewalk = False
            Lab = False
            playerxpos = 1100
            playerypos = 500
            wall_y = 50
            wall2_y = 645
            self.player_y_pos = playerypos
            self.player_x_pos = playerxpos

        if self.rect.top <=50 and Airlock and self.rect.centerx>550 and self.rect.centerx<950:
            Play_start = False
            Airlock = False
            Lab = False
            Spacewalk = True
            playerxpos = 640
            playerypos = 250
            wall_y = 0
            wall2_y = 700
            self.player_y_pos = playerypos
            self.player_x_pos = playerxpos

        if self.rect.bottom >= 645 and Spacewalk and self.rect.centerx>500 and self.rect.centerx<950: #left
            Play_start = False
            Airlock = True
            Lab = False
            Spacewalk = False
            playerxpos = 640
            playerypos = 360
            wall_y = 50
            wall2_y = 645
            self.player_y_pos = playerypos
            self.player_x_pos = playerxpos




        if self.rect.top <= wall_y: self.mov_y = 3
        if self.rect.bottom >= wall2_y: self.mov_y = -3

        self.player_x_pos += self.mov_x
        self.player_y_pos += self.mov_y
        self.rect.centerx = self.player_x_pos
        self.rect.centery = self.player_y_pos



    def update(self, cursor_pos):
        global playerxpos
        global playerypos
        playerxpos = self.player_x_pos
        playerypos = self.player_y_pos
        cursor_x, cursor_y = cursor_pos
        rel_x, rel_y = cursor_x - self.rect.centerx, cursor_y - self.rect.centery
        angle = (180 / math.pi) * -math.atan2(rel_y, rel_x)
        self.image = pygame.transform.rotate(self.original_image, angle)
        self.rect = self.image.get_rect(center=self.rect.center)
        self.leftrect = self.image.get_rect()
        self.player_input(cursor_x, cursor_y)
        self.collisions()
        #print(self.mov_x)





#player variables


#wall_y = 50
#wall2_y = 645
Menu_music=pygame.mixer.Sound('audio/space_audio.mp3')
CharacterGo = False
Play_start = False
credits_active = False
Airlock = False
Spacewalk = False
Lab = False
pipeshow1=False
pipeshow2=False
windowclosed=False
closed = False
inv=False
sample_empty = False
sample_fill = False
pipe=False
pipeamt=2
pipegone=True
pipegone2=True
gocentri =True
windowinfo_press=True
windowinfo_pipe=True


#routine info
windowinfo_blud=False
windowinfo_centri=False

keys = pygame.key.get_pressed()

stars = pygame.image.load('images/stars.png').convert_alpha()
stars_rect = stars.get_rect()
stars_x = 0
stars_y = 0

#texts stuff
window_text = font.render('DarIntSys-NASA', False, (255,255,255))
title_text = font3.render('Spariz:ISS', False, (255,255,255))
start_text = font2.render('>Press SPACE to start', False, (255,255,255))
controls_text = font2.render('>Press C for controls', False, (255,255,255))
credit_text = font2.render('>Press TAB for credits', False, (255,255,255))
quit_text = font2.render('>Press ESC to quit', False, (255,255,255))
#credits texts
titlecred_text = font.render('Credits.txt', False, (255,255,255))
creddar_text = font2.render('Group: DarIntSys', False, (255,255,255))
cred1_text = font5.render('--Coding & Research--', False, (255,255,255))
cred2_text = font4.render('Rigo Amgao,Luke Madtha', False, (255,255,255))
cred3_text = font2.render('--Art Design--', False, (255,255,255))
cred4_text = font4.render('Hamza Faiz, Zayba Kader', False, (255,255,255))
cred5_text = font2.render('--Sound Design--', False, (255,255,255))
cred6_text = font4.render('Surabhi Sudheendra', False, (255,255,255))
#controls texts
titlecon_text = font.render('Controls.txt', False, (255,255,255))
con1_text = font5.render('--Movement--', False, (255,255,255))
con2_text = font4.render('Cursor and Space To Play:', False, (255,255,255))
con3_text = font4.render('Cursor Opposite Direction > Aim', False, (255,255,255))
con4_text = font4.render('Space > Move', False, (255,255,255))
con5_text = font5.render('--Others--', False, (255,255,255))
con6_text = font4.render('Backspace > Main Menu ', False, (255,255,255))
con7_text = font4.render('E > Interact ', False, (255,255,255))
con8_text = font4.render('B > Take Blood ', False, (255,255,255))
con9_text = font4.render('R > Reset Position ', False, (255,255,255))
#invtext
inv_title = font1.render('Inventory.txt', False, (255,255,255))

#info blud
blud_title= font.render('BloodSamples.txt', False, (255,255,255))
bludtext1 = font4.render('>Blood samples are routinely', False, (255,255,255))
bludtext2 = font4.render('collected by astronauts for ', False, (255,255,255))
bludtext3 = font4.render('them to see changes in the ', False, (255,255,255))
bludtext4 = font4.render('immune system and see if ', False, (255,255,255))
bludtext5 = font4.render('latent viruses are activated', False, (255,255,255))
bludtext6 = font4.render('during space flight!', False, (255,255,255))
bludtext7 = font4.render('Place your blood sample', False, (255,255,255))
bludtext8 = font4.render('in the centrifuge.', False, (255,255,255))
bludtext9 = font4.render('>Press (-) to continue', False, (153,255,102))

centri_title= font.render('Centrifuge.txt', False, (255,255,255))
centritext1 = font4.render('>Now that you have checked', False, (255,255,255))
centritext2 = font4.render('your blood, you find out', False, (255,255,255))
centritext3 = font4.render('that you are completely', False, (255,255,255))
centritext4 = font4.render('healthy! ', False, (255,255,255))

centritext9 = font4.render('>Press (-) to continue', False, (153,255,102))

#info space
space_title= font.render('PipeFix.txt', False, (255,255,255))
spacetext1 = font4.render('>Astronauts have chores', False, (255,255,255))
spacetext2 = font4.render('to do when living on the ISS  ', False, (255,255,255))
spacetext3 = font4.render('one of which is going', False, (255,255,255))
spacetext4 = font4.render('on spacewalks and fixing ', False, (255,255,255))
spacetext5 = font4.render('things like solar panels', False, (255,255,255))
spacetext6 = font4.render('Place your pipes', False, (255,255,255))
spacetext7 = font4.render('on the solar panels.', False, (255,255,255))
spacetext8 = font4.render('>Press (-) to continue', False, (153,255,102))


#info pressure
press_title= font.render('Pressure.txt', False, (255,255,255))
presstext1 = font4.render('>To help astronauts adjust', False, (255,255,255))
presstext2 = font4.render('to living on the ISS  ', False, (255,255,255))
presstext3 = font4.render('the pressure and concentration', False, (255,255,255))
presstext4 = font4.render('of the air in the ISS have to ', False, (255,255,255))
presstext5 = font4.render('be checked and maintained', False, (255,255,255))
presstext6 = font4.render('Check Pressure', False, (255,255,255))
presstext7 = font4.render('Concentration is 79% N 21%O2', False, (255,255,255))
presstext8 = font4.render('Pressure is 101kPa', False, (255,255,255))
window = pygame.image.load('images/window.png').convert_alpha()
window = pygame.transform.smoothscale(window,(499,599)).convert_alpha()

bg_surf = pygame.image.load('images/bg.png').convert()
bg_surf = pygame.transform.smoothscale(bg_surf, (1280, 720))
bg_airsurf = pygame.image.load('images/airlock.jpg').convert()
bg_airsurf = pygame.transform.smoothscale(bg_airsurf, (1280, 720))
bg_labsurf = pygame.image.load('images/lab.jpg').convert()
bg_labsurf = pygame.transform.smoothscale(bg_labsurf, (1280, 720))
bg_spacesurf = pygame.image.load('images/spacewalk.jpg')
bg_spacesurf = pygame.transform.smoothscale(bg_spacesurf, (1280, 720))


player = pygame.sprite.GroupSingle()
player.add(Player())

playermenu = pygame.sprite.GroupSingle()
playermenu.add(Menu_player())




#hitters.add(Hitters(random.randint(0,500),random.randint(0,500),75,75))
#hitters.add(Hitters(random.randint(0,500),random.randint(0,500),75,75))
#hitters.add(Hitters(random.randint(0,500),random.randint(0,500),75,75))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()


    if Play_start == False and Airlock == False and Spacewalk==False and Lab==False:
        if Play_start == False and Airlock == False and Spacewalk==False and Lab==False:
            main_menu()
        Menu_music.play(loops=-1)
        cursor_pos = pygame.mouse.get_pos()
        screen.fill(pygame.Color('#00011a'))
        screen.blit(stars,(stars_x,stars_y))
        screen.blit(window_text,(5,700))
        screen.blit(start_text,(75,100))
        screen.blit(controls_text,(75,250))
        screen.blit(credit_text,(75,400))
        screen.blit(quit_text,(75,550))
        #Start_button.draw()
        playermenu.draw(screen)
        playermenu.sprite.update(cursor_pos)
        screen.blit(title_text,(625,35))
        if credits_active:
            screen.blit(window,(1280/3,25))
            screen.blit(creddar_text,(495,135))
            screen.blit(titlecred_text,(450,40))
            screen.blit(cred1_text,(450,275))
            screen.blit(cred2_text,(485,325))
            screen.blit(cred3_text,(515,400))
            screen.blit(cred4_text,(482,450))
            screen.blit(cred5_text,(482,525))
            screen.blit(cred6_text,(525,575))
            #screen.blit(credits,(0,0))
            #print('summon unchariz')
        if controls_appear:
            screen.blit(window,(1280/3,25))
            screen.blit(titlecon_text,(450,40))
            screen.blit(con1_text,(538,75))
            screen.blit(con2_text,(435,125))
            screen.blit(con3_text,(435,155))
            screen.blit(con4_text,(435,185))
            screen.blit(con5_text,(538,250))
            screen.blit(con6_text,(435,300))
            screen.blit(con7_text,(435,330))
            screen.blit(con8_text,(435,360))
            screen.blit(con9_text,(435,390))

            

        #screen.fill('gray')


    if Play_start:
        cursor_pos = pygame.mouse.get_pos()
        screen.blit(bg_surf, (0, 0))


    if Airlock:
        screen.blit(bg_airsurf, (0, 0))
        if windowinfo_press:
            keys = pygame.key.get_pressed()
            screen.blit(window,(750,75))
            screen.blit(press_title,(775,90))
            screen.blit(presstext1,(775,160))
            screen.blit(presstext2,(775,195))
            screen.blit(presstext3,(775,230))
            screen.blit(presstext4,(775,265))
            screen.blit(presstext5,(775,300))
            screen.blit(presstext6,(775,335))
            
            screen.blit(spacetext8,(775,600))
            if keys[pygame.K_MINUS]:
                windowinfo_press =  False 
        if playerxpos > 970 and playerypos > 480:
            prompt=pygame.image.load('images/prompt.png').convert_alpha()
            prompt = pygame.transform.smoothscale(prompt,(75,75)).convert_alpha()
            screen.blit(prompt,(968,500))
            keys = pygame.key.get_pressed()
            if keys[pygame.K_e]:
                screen.blit(window,(750,75))
                screen.blit(press_title,(775,90))
                screen.blit(presstext7,(775,160))
                screen.blit(presstext8,(775,195))

        if playerxpos > 970 and playerypos > 480:
            prompt=pygame.image.load('images/prompt.png').convert_alpha()
            prompt = pygame.transform.smoothscale(prompt,(75,75)).convert_alpha()
            screen.blit(prompt,(968,500))
            keys = pygame.key.get_pressed()
            if keys[pygame.K_e]:
                screen.blit(window,(750,75))
                screen.blit(press_title,(775,90))
                screen.blit(presstext7,(775,160))
                screen.blit(presstext8,(775,195)) #REMEMBER TO CHANGE TO AIRLOCK SURF

    if Spacewalk:
        screen.blit(bg_spacesurf,(0,0))
        pygame.draw.line(screen,'Gray',(435,696),(playerxpos,playerypos),20)

        if pipeshow1:
            pipeimg1=pygame.image.load('images/pipe.png').convert_alpha()
            pipeimg1= pygame.transform.smoothscale(pipeimg1,(45,88)).convert_alpha()
            bg_spacesurf.blit(pipeimg1,(317,214))
        if pipeshow2:
            pipeimg2=pygame.image.load('images/pipeside.png').convert_alpha()
            pipeimg2= pygame.transform.smoothscale(pipeimg2,(45,88)).convert_alpha()
            bg_spacesurf.blit(pipeimg2,(915,380))

        if playerxpos > 320 and playerxpos < 440 and playerypos > 150 and playerypos < 320 and pipeamt>0 and pipegone:
            prompt=pygame.image.load('images/prompt.png').convert_alpha()
            prompt = pygame.transform.smoothscale(prompt,(75,75)).convert_alpha()
            screen.blit(prompt,(260,100))
            keys = pygame.key.get_pressed()
            if keys[pygame.K_e]:
                print('u prompt')
                pipeamt -=1
                pipeshow1 = True
                pipegone = False
        if playerxpos > 780 and playerxpos < 963 and playerypos > 315 and playerypos < 510 and pipeamt>0 and pipegone2:
            prompt=pygame.image.load('images/prompt.png').convert_alpha()
            prompt = pygame.transform.smoothscale(prompt,(75,75)).convert_alpha()
            screen.blit(prompt,(835,300))
            keys = pygame.key.get_pressed()
            if keys[pygame.K_e]:
                print('u prompt')
                pipeamt -=1
                pipeshow2 = True
                pipegone2 = False
        if pipeamt == 0:
            pipe != True

    
    if Lab: #add
        centri=pygame.image.load('images/centri.png')
        centri = pygame.transform.smoothscale(centri,(100,164)).convert_alpha()
        screen.blit(bg_labsurf,(0,0))
        if gocentri:
            screen.blit(centri,(475,270))
        elif closed:
            centrino=pygame.image.load('images/centri_close.png').convert_alpha()
            centrino= pygame.transform.smoothscale(centrino,(100,164)).convert_alpha()
            bg_labsurf.blit(centrino,(475,300))



        if playerxpos > 415 and playerxpos < 640 and playerypos > 255 and playerypos < 475 and sample_fill and gocentri:
            prompt=pygame.image.load('images/prompt.png').convert_alpha()
            prompt = pygame.transform.smoothscale(prompt,(75,75)).convert_alpha()
            screen.blit(prompt,(475,150))
            keys = pygame.key.get_pressed()
            if keys[pygame.K_e]:
                print('u prompt')
                gocentri = False
                windowinfo_centri=True
                sample_fill = False
                windowinfo_blud = False
                closed=True
                windowclosed=True


    if CharacterGo:
        cursor_pos = pygame.mouse.get_pos()
        player.sprite.update(cursor_pos)
        player.draw(screen)


    if inv:
        window2 = pygame.image.load('images/window2.png').convert_alpha()
        window2 = pygame.transform.smoothscale(window2,(350,148)).convert_alpha()
        screen.blit(window2,(15,565))
        screen.blit(inv_title,(30,575))


    if sample_empty:
        empty=pygame.image.load('images/Sample_empty.png')
        empty = pygame.transform.smoothscale(empty,(75,75)).convert_alpha()
        #filled_rect=filled.get_rect(center=(30,720-55))
        screen.blit(empty,(30,615))

    if pipe:
        #filled_rect=filled.get_rect(center=(30,720-55))
        if pipeamt==1:
            p1=pygame.image.load('images/pipe1.png')
            p1= pygame.transform.smoothscale(p1,(75,75)).convert_alpha()
            screen.blit(p1,(110,615))
        if pipeamt==2:
            p2=pygame.image.load('images/pipe2.png')
            p2= pygame.transform.smoothscale(p2,(75,75)).convert_alpha()
            screen.blit(p2,(110,615))

    if sample_fill:
        filled=pygame.image.load('images/Sample_filled.png')
        filled = pygame.transform.smoothscale(filled,(75,75)).convert_alpha()
        #filled_rect=filled.get_rect(center=(30,720-55))
        screen.blit(filled,(30,615))

    if windowinfo_blud:
        screen.blit(window,(750,75))
        screen.blit(blud_title,(775,90))
        screen.blit(bludtext1,(775,125))
        screen.blit(bludtext2,(775,160))
        screen.blit(bludtext3,(775,195))
        screen.blit(bludtext4,(775,230))
        screen.blit(bludtext5,(775,265))
        screen.blit(bludtext6,(775,300))
        screen.blit(bludtext7,(775,335))
        screen.blit(bludtext8,(775,370))
        screen.blit(bludtext9,(775,600))

    if windowinfo_centri:
        screen.blit(window,(750,75))
        screen.blit(centri_title,(775,90))
        screen.blit(centritext1,(775,125))
        screen.blit(centritext2,(775,160))
        screen.blit(centritext3,(775,195))
        screen.blit(centritext4,(775,230))
        screen.blit(centritext9,(775,600))

    if Spacewalk:
        if windowinfo_pipe:
            screen.blit(window,(750,75))
            screen.blit(space_title,(775,90))
            screen.blit(spacetext1,(775,160))
            screen.blit(spacetext2,(775,195))
            screen.blit(spacetext3,(775,230))
            screen.blit(spacetext4,(775,265))
            screen.blit(spacetext5,(775,300))
            screen.blit(spacetext6,(775,335))
            screen.blit(spacetext8,(775,600)) 





    pygame.display.update()
    clock.tick(60)