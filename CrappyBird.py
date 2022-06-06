# -*- coding: utf-8 -*-
"""
@authors: Weronika Bizoń 261652, Kacper Możdżeń 261831, Adam Ciszyński 261784
"""

import pygame, random
from pygame.locals import *
from configparser import ConfigParser

pygame.init()

config = ConfigParser()
config.read('config.ini')

screen_height = int(config.get('MAIN', 'screen_height'))
screen_width = int(config.get('MAIN', 'screen_width'))
screen = pygame.display.set_mode([screen_width, screen_height])
pygame.display.set_caption('Crappy Bird')
vec = pygame.math.Vector2
map_speed = 5
gravity = 0.675
player_character = random.choices(population = ['mummy', 'eagle', 'skeleton', 'sus', 'steve', 'mario', 'thanos', 'gg'], weights = [0.25, 0.25, 0.25, 0.05, 0.05, 0.05, 0.05, 0.05])
new_hiscore = 0
mario_jump = 1

# Czestotliwosc spawnowania chmur
spawn_cloud = 0
spawn_cloud_max = 500

# Animacja fruwania modelu
float_timer = 0
up_down = - 1

# Czestotliwosc spawnowania rur oraz punktów
spawn_PipeandPoint = 50
spawn_PipeandPoint_max = 95

# Ogranicznik FPS
FPS = 60
FramePerSec = pygame.time.Clock()

# Parametry rozgrywki
start = 0
began = 0
in_menu = 1
in_settings = 0

# Tekstury
pipe_texture_top = pygame.image.load(r'textures\pipe_top.png').convert_alpha()
pipe_texture_bot = pygame.image.load(r'textures\pipe_bot.png').convert_alpha()
ground_texture = pygame.image.load(r'textures\ground.png').convert_alpha() 
background_tx = pygame.image.load(r'textures\background.png').convert_alpha()

sfx_on_tx = pygame.image.load(r'textures\sfx_on.png').convert_alpha()
sfx_on_active_tx = pygame.image.load(r'textures\sfx_on_active.png').convert_alpha()

sfx_off_tx = pygame.image.load(r'textures\sfx_off.png').convert_alpha()
sfx_off_active_tx = pygame.image.load(r'textures\sfx_off_active.png').convert_alpha()

settings_tx = pygame.image.load(r'textures\settings.png').convert_alpha()
settings_active_tx = pygame.image.load(r'textures\settings_active.png').convert_alpha()

music_on_tx = pygame.image.load(r'textures\music_on.png').convert_alpha()
music_on_active_tx = pygame.image.load(r'textures\music_on_active.png').convert_alpha()

music_off_tx = pygame.image.load(r'textures\music_off.png').convert_alpha()
music_off_active_tx = pygame.image.load(r'textures\music_off_active.png').convert_alpha()

back_tx = pygame.image.load(r'textures\back.png').convert_alpha()
back_active_tx = pygame.image.load(r'textures\back_active.png').convert_alpha()

play_tx = pygame.image.load(r'textures\play.png').convert_alpha()
play_active_tx = pygame.image.load(r'textures\play_active.png').convert_alpha()

# Tekstury gracza
mummy = pygame.image.load(r'textures\mummy.png').convert_alpha()
mummy_dead = pygame.image.load(r'textures\mummy_dead.png').convert_alpha()

eagle = pygame.image.load(r'textures\eagle.png').convert_alpha()
eagle_dead = pygame.image.load(r'textures\eagle_dead.png').convert_alpha()

skeleton = pygame.image.load(r'textures\skeleton.png').convert_alpha()
skeleton_dead = pygame.image.load(r'textures\skeleton_dead.png').convert_alpha()

sus = pygame.image.load(r'textures\sus.png').convert_alpha()
sus_dead = pygame.image.load(r'textures\sus_dead.png').convert_alpha()

steve = pygame.image.load(r'textures\steve.png').convert_alpha()
steve_dead = pygame.image.load(r'textures\steve_dead.png').convert_alpha()

mario = pygame.image.load(r'textures\mario.png').convert_alpha()
mario_dead = pygame.image.load(r'textures\mario_dead.png').convert_alpha()

thanos = pygame.image.load(r'textures\thanos.png').convert_alpha()
thanos_dead = pygame.image.load(r'textures\thanos_dead.png').convert_alpha()

gg = pygame.image.load(r'textures\gg.png').convert_alpha()
gg_dead = pygame.image.load(r'textures\gg_dead.png').convert_alpha()

# Tekstury chmur
cloud1 = pygame.image.load(r'textures\cloud1.png').convert_alpha()
cloud2 = pygame.image.load(r'textures\cloud2.png').convert_alpha()
cloud3 = pygame.image.load(r'textures\cloud3.png').convert_alpha()
cloud4 = pygame.image.load(r'textures\cloud4.png').convert_alpha()
cloud5 = pygame.image.load(r'textures\cloud5.png').convert_alpha()
cloud6 = pygame.image.load(r'textures\cloud6.png').convert_alpha()
cloud7 = pygame.image.load(r'textures\cloud7.png').convert_alpha()
cloud8 = pygame.image.load(r'textures\cloud8.png').convert_alpha()
cloud9 = pygame.image.load(r'textures\cloud9.png').convert_alpha()
cloud10 = pygame.image.load(r'textures\cloud10.png').convert_alpha()
cloud11 = pygame.image.load(r'textures\cloud11.png').convert_alpha()
cloud12 = pygame.image.load(r'textures\cloud12.png').convert_alpha()
cloud13 = pygame.image.load(r'textures\cloud13.png').convert_alpha()
cloud14 = pygame.image.load(r'textures\cloud14.png').convert_alpha()


# Muzyka    
pygame.mixer.music.load(r"sounds\soundtrack.mp3")
pygame.mixer.music.set_volume(0.4)   

# SFX
point_sound = pygame.mixer.Sound(r"sounds\point.mp3")
flap_sound = pygame.mixer.Sound(r"sounds\flap.mp3")
crash_sound = pygame.mixer.Sound(r"sounds\crash.mp3")
sus_crash_sound = pygame.mixer.Sound(r"sounds\sus_crash.mp3")
steve_crash_sound = pygame.mixer.Sound(r"sounds\steve_crash.mp3")
mario_crash_sound = pygame.mixer.Sound(r"sounds\mario_crash.mp3")
thanos_crash_sound = pygame.mixer.Sound(r"sounds\thanos_crash.mp3")
gg_crash_sound = pygame.mixer.Sound(r"sounds\gg_crash.mp3")
reset_sound = pygame.mixer.Sound(r"sounds\reset.mp3")
mario_jump_1_sound = pygame.mixer.Sound(r"sounds\mario_jump_1_sound.mp3")
mario_jump_2_sound = pygame.mixer.Sound(r"sounds\mario_jump_2_sound.mp3")
mario_jump_3_sound = pygame.mixer.Sound(r"sounds\mario_jump_3_sound.mp3")

# Parametry dzwieku [0 = OFF / 1 = ON]
music_value = int(config.get('MAIN', 'music'))
sfx_value = int(config.get('MAIN', 'sfx'))
pygame.display.set_icon(eagle)

# Ustawienia muzyki
if music_value == 0:
    pygame.mixer.music.stop()
else:
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.4) 


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        if player_character[0] == 'mummy':
            self.texture = mummy
        if player_character[0] == 'eagle':
            self.texture = eagle
        if player_character[0] == 'skeleton':
            self.texture = skeleton
        if player_character[0] == 'sus':
            self.texture = sus
        if player_character[0] == 'steve':
            self.texture = steve
        if player_character[0] == 'mario':
            self.texture = mario
        if player_character[0] == 'thanos':   
            self.texture = thanos
        if player_character[0] == 'gg':
            self.texture = gg
        self.rect = self.texture.get_rect()
        self.jump_power = 16 # Moc skoku
        self.dead = False
        
        # Losowa postać gracza
        self.pos = vec(screen_width / 2, screen_height / 2)
        self.vel = vec(0,0)
        
        self.score = 0 # Licznik wyniku
         
    def update(self):
        self.acc = vec(0, gravity)
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        
        # Blokada wyjscia z dolu
        if self.pos.y > screen_height - 180:
            self.pos.y = screen_height - 180           
        
        # Blokada wyjscia z gory
        if self.pos.y < 70:
            self.pos.y = 70
            self.vel.y += 1.5
            
        # Zaktualizowanie pozycji gracza 
        self.rect.midbottom = self.pos
        
    def jump(self):
        global mario_jump
        if player.dead == False:
            self.vel.y = -self.jump_power
            if player_character[0] == 'mario':
                if mario_jump == 1:
                    pygame.mixer.Sound.play(mario_jump_1_sound)
                if mario_jump == 2:
                    pygame.mixer.Sound.play(mario_jump_2_sound)
                if mario_jump == 3:
                    pygame.mixer.Sound.play(mario_jump_3_sound)
                    mario_jump = 0
                mario_jump += 1
            else:       
                pygame.mixer.Sound.play(flap_sound)
        
        
class Pipe(pygame.sprite.Sprite):
    def __init__(self):
        super(Pipe, self).__init__()
        self.speed = map_speed
        self.gap_begin = random.randint(200, screen_height - 575) # Położenie szpary
        self.gap = random.randint(255, 275) # Wielkosc szpary
        
        # Górna rura
        self.texture_top = pipe_texture_top
        self.pos_top = vec(screen_width, self.gap_begin)
        self.rect_top = self.texture_top.get_rect()
        
        # Dolna rura
        self.texture_bot = pipe_texture_bot
        self.pos_bot = vec(screen_width, self.gap_begin + self.gap)
        self.rect_bot = self.texture_bot.get_rect()
        
        
    def update(self):
        # Przemieszczenie rur
        self.pos_top.x -= self.speed
        self.pos_bot.x -= self.speed
        
        # Zaktualizowanie pozycji rur
        self.rect_bot.topleft = self.pos_bot
        self.rect_top.bottomleft = self.pos_top
        
        # Zabijanie rury, kiedy opusci ekran z lewej strony
        if self.pos_bot.x + self.rect_bot.width < 0:
            self.kill()
              
     
class Point(pygame.sprite.Sprite):
    def __init__(self):
        super(Point, self).__init__()
        self.width = 10
        self.speed = map_speed
        self.height = screen_height
        self.surf = pygame.Surface([self.width, self.height])
        self.surf.set_colorkey([0, 0, 0])
        self.pos = vec(screen_width + 200, screen_height / 2)
        self.rect = self.surf.get_rect()

    def update(self):
        # Zabijanie punktu, jak opusci ekran z lewej strony
        self.pos.x -= self.speed
        if self.pos.x < 0:
            self.kill()
            
        # Zaktualizowanie puzycji punktu
        self.rect.center = self.pos
   
        
class Ground(pygame.sprite.Sprite):
    def __init__(self):
        super(Ground, self).__init__()
        self.texture = ground_texture
        self.rect1 = self.texture.get_rect()
        self.rect2 = self.texture.get_rect()
        self.speed = map_speed
        self.pos1 = vec(0, screen_height + 100)
        self.pos2 = vec(1280, screen_height + 100)
             
    def update(self):
        self.pos1.x -= self.speed
        self.pos2.x -= self.speed
        
        if self.pos1.x + 1280 == 0:
            self.pos1.x = 1280  
        if self.pos2.x + 1280 == 0:
            self.pos2.x = 1280

        self.rect1.bottomleft = self.pos1
        self.rect2.bottomleft = self.pos2
        

class Background(pygame.sprite.Sprite):
    def __init__(self):
        super(Background, self).__init__()
        self.texture = background_tx
        self.rect1 = self.texture.get_rect()
        self.rect2 = self.texture.get_rect()
        self.speed = 0.25
        self.pos1 = vec(0, screen_height - 180)
        self.pos2 = vec(1000, screen_height +- 180)
        
    def update(self):
        self.pos1.x -= self.speed
        self.pos2.x -= self.speed
        
        if self.pos1.x + 1000 == 0:
            self.pos1.x = 1000 
        if self.pos2.x + 1000 == 0:
            self.pos2.x = 1000

        self.rect1.bottomleft = self.pos1
        self.rect2.bottomleft = self.pos2
        

class Button(pygame.sprite.Sprite):
    def __init__(self, texture):
        super(Button, self).__init__()
        self.texture = texture
        self.rect = self.texture.get_rect()
        self.pos = vec(0, 0)
        self.width = self.texture.get_width()
        self.height = self.texture.get_height()
        
    def update(self):
        self.rect.bottomright = self.pos
        

class Cloud(pygame.sprite.Sprite):
    def __init__(self):
        super(Cloud, self).__init__()
        self.texture = random.choices([cloud1, cloud2, cloud3, cloud4, cloud5, cloud6, cloud7, cloud8, cloud9, cloud10, cloud11, cloud12, cloud13, cloud14])[0]
        self.rect = self.texture.get_rect()
        self.speed = random.uniform(0.4, 0.5)
        self.width = self.texture.get_width()
        self.height = self.texture.get_height()
        self.pos = vec(screen_width, random.randint(50, 450))
    
    def update(self):
        self.pos.x -= self.speed
        
        if self.pos.x + self.width  <= 0:
            self.kill()

        self.rect.bottomleft = self.pos

        
# Tworzenie sprite'ow i grup sprite'ow      
player = Player()
background = Background()
ground = Ground()
pipes = pygame.sprite.Group()
points = pygame.sprite.Group()
buttons = pygame.sprite.Group()
clouds = pygame.sprite.Group()

# Pojawianie się paru chmur od razu
start_cloud1 = Cloud()
start_cloud1.pos = vec(random.randint(-50, 200), random.randint(50, 150) + random.randint(-25, 25))
clouds.add(start_cloud1)

start_cloud2 = Cloud()
start_cloud2.pos = vec(random.randint(150, 400), random.randint(250, 300) + random.randint(-25, 25))
clouds.add(start_cloud2)

start_cloud3 = Cloud()
start_cloud3.pos = vec(random.randint(350, 600), random.randint(350, 450) + random.randint(-25, 25))
clouds.add(start_cloud3)



def update_sfx():
    if sfx_value == 0:
        point_sound.set_volume(0)
        flap_sound.set_volume(0)
        crash_sound.set_volume(0)
        sus_crash_sound.set_volume(0)
        steve_crash_sound.set_volume(0)
        mario_crash_sound.set_volume(0)
        thanos_crash_sound.set_volume(0)
        gg_crash_sound.set_volume(0)
        reset_sound.set_volume(0)
        mario_jump_1_sound.set_volume(0)
        mario_jump_2_sound.set_volume(0)
        mario_jump_3_sound.set_volume(0)
        
    else:
        flap_sound.set_volume(0.5)
        crash_sound.set_volume(0.4)
        point_sound.set_volume(1.5)
        sus_crash_sound.set_volume(0.5)
        steve_crash_sound.set_volume(0.7)
        mario_crash_sound.set_volume(1)
        thanos_crash_sound.set_volume(0.5)
        gg_crash_sound.set_volume(0.8)
        reset_sound.set_volume(1)
        mario_jump_1_sound.set_volume(0.5)
        mario_jump_2_sound.set_volume(0.5)
        mario_jump_3_sound.set_volume(0.3)

update_sfx()


def reset():
    for entity in pipes:
        entity.kill()
    for entity in points:
        entity.kill()
    
    global start, began, spawn_PipeandPoint, player_character, map_speed, new_hiscore
    
    spawn_PipeandPoint = 50
    player.dead = False
    player.score = 0
    if player.pos.y <= screen_height / 2 + 15:
        if player.pos.y >= screen_height / 2 - 15:
            player.pos = player.pos
        else:
            player.pos = vec(screen_width / 2, screen_height / 2)
    else:
        player.pos = vec(screen_width / 2, screen_height / 2)
    player.vel = vec(0, 0)
    
    map_speed = 5
    ground.speed = 5
    background.speed = 0.25
    
    pygame.mixer.music.set_volume(0.4)  
    
    # Losowa postać gracza
    player_character = random.choices(population = ['mummy', 'eagle', 'skeleton', 'sus', 'steve', 'mario', 'thanos', 'gg'], weights = [0.25, 0.25, 0.25, 0.05, 0.05, 0.05, 0.05, 0.05])
    if player_character[0] == 'mummy':
        player.texture = mummy
    if player_character[0] == 'eagle':
        player.texture = eagle
    if player_character[0] == 'skeleton':
        player.texture = skeleton
    if player_character[0] == 'sus':
        player.texture = sus
    if player_character[0] == 'steve':
        player.texture = steve
    if player_character[0] == 'mario':
        player.texture = mario
    if player_character[0] == 'thanos':   
        player.texture = thanos
    if player_character[0] == 'gg':
        player.texture = gg
        
    new_hiscore = 0
    start = 1
    began = 0 
        

def death():
    global new_hiscore, mario_jump
    mario_jump = 1
    player.dead = True
    print('Final score: ' + str(player.score))
    if player.score > int(config.get('MAIN', 'hiscore')):
        config.set('MAIN', 'hiscore', str(player.score))
        new_hiscore = 1

    if player_character[0] == 'mummy':
        player.texture = mummy_dead
        pygame.mixer.Sound.play(crash_sound)
    if player_character[0] == 'eagle':
        player.texture = eagle_dead
        pygame.mixer.Sound.play(crash_sound)
    if player_character[0] == 'skeleton':
        player.texture = skeleton_dead
        pygame.mixer.Sound.play(crash_sound)
    if player_character[0] == 'sus':
        player.texture = sus_dead
        pygame.mixer.Sound.play(sus_crash_sound)
    if player_character[0] == 'steve':
        player.texture = steve_dead
        pygame.mixer.Sound.play(steve_crash_sound)
    if player_character[0] == 'mario':
        player.texture = mario_dead
        pygame.mixer.Sound.play(mario_crash_sound)
    if player_character[0] == 'thanos':
        player.texture = thanos_dead
        pygame.mixer.Sound.play(thanos_crash_sound)
    if player_character[0] == 'gg':
        player.texture = gg_dead
        pygame.mixer.Sound.play(gg_crash_sound)

    global map_speed 
    map_speed = 0
    for entity in pipes:
        entity.speed = 0
    for entity in points:
        entity.speed = 0
    ground.speed = 0
    background.speed = 0
    
    pygame.mixer.music.set_volume(0)  
    

def TextWithOutline(text, fontname, size, colour_text, colour_outline, posx, posy):
    if size == 90:
        outline = 6
    elif size == 50:
        outline = 4
    elif size == 115:
        outline = 8
    elif size == 30:
        outline = 2.75
    else:
        outline = 0
        
    text_font = pygame.font.Font(fontname, size)
    text_outline_surf = text_font.render(text, True, colour_outline)
    text_outline_rect = text_outline_surf.get_rect(center = (posx + outline, posy + outline))
    text_outline_rect2 = text_outline_surf.get_rect(center = (posx - outline, posy - outline))
    text_outline_rect3 = text_outline_surf.get_rect(center = (posx + outline, posy - outline))
    text_outline_rect4 = text_outline_surf.get_rect(center = (posx - outline, posy + outline)) 
    
    text_surf = text_font.render(text, True, colour_text)
    text_rect = text_surf.get_rect(center = (posx, posy))
      
    screen.blit(text_outline_surf, text_outline_rect)
    screen.blit(text_outline_surf, text_outline_rect2)
    screen.blit(text_outline_surf, text_outline_rect3)
    screen.blit(text_outline_surf, text_outline_rect4)
    screen.blit(text_surf, text_rect)


''' GUZIKI '''

# Guzik ustawień
settings = Button(settings_tx)
settings.pos = (screen_width - 15, screen_height - 15)
buttons.add(settings)

# Guzik SFX
sfx = Button(sfx_on_tx)
sfx.pos = (screen_width - 15, screen_height - 15)
if sfx_value == 1:
    sfx.texture = sfx_on_tx
else:
    sfx.texture = sfx_off_tx
buttons.add(sfx)

# Guzik muzyki
music = Button(music_on_tx)
music.pos = (15 + music.width, screen_height - 15)
if music_value == 1:
    music.texture =  music_on_tx
else:
    music.texture = music_off_tx
buttons.add(music)

# Guzik back
back = Button(back_tx)
back.pos = (screen_width - 15, 15 + back.height)
buttons.add(back)

# Guzik play
play = Button(play_tx)
play.pos = ((screen_width + play.width) / 2, screen_height / 2 + 200)
buttons.add(play)

    
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        if event.type == pygame.KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
                
            if in_menu == 0 and (event.key == K_UP or event.key == K_SPACE):
                player.jump()
                began = 1
                gravity = 0.675
                
            if event.key == K_r and in_menu == 0:
                pygame.mixer.Sound.play(reset_sound)
                reset()
        
        
        if event.type == pygame.MOUSEMOTION:
            x, y = event.pos
            
            if in_settings == 0:
                if (x in range (settings.pos[0] - settings.width, settings.pos[0]) and y in range(settings.pos[1] - settings.height, settings.pos[1])):
                    settings.texture = settings_active_tx
                else:
                    settings.texture = settings_tx

                    if (x in range(int(play.pos[0]) - play.width, int(play.pos[0])) and y in range(int(play.pos[1] - play.height), int(play.pos[1]))):
                        play.texture = play_active_tx
                    else:
                        play.texture = play_tx
                   
            if in_settings == 1:
                if (x in range (sfx.pos[0] - sfx.width, sfx.pos[0]) and y in range(sfx.pos[1] - sfx.height, sfx.pos[1])):        
                    if sfx_value == 1:
                        sfx.texture = sfx_on_active_tx
                    else: 
                        sfx.texture = sfx_off_active_tx
                else:
                    if sfx_value == 1:
                        sfx.texture = sfx_on_tx
                    else:
                        sfx.texture = sfx_off_tx
                
                if (x in range(music.pos[0] - music.width, music.pos[0]) and y in range(music.pos[1] - music.height, music.pos[1])):
                    if music_value == 1:
                        music.texture = music_on_active_tx
                    else:
                        music.texture = music_off_active_tx
                else:
                    if music_value == 1:
                        music.texture = music_on_tx
                    else:
                        music.texture = music_off_tx
                
            if (x in range(back.pos[0] - back.width, back.pos[0]) and y in range(back.pos[1] - back.height, back.pos[1])):
                back.texture = back_active_tx
            else:
                back.texture = back_tx
                    

        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            
            if event.button == 1 and in_menu == 1: 
                if in_settings == 1:
                    if (x in range (sfx.pos[0] - settings.width, sfx.pos[0]) and y in range(sfx.pos[1] - settings.height, sfx.pos[1])):
                        if sfx_value == 1:
                            config.set('MAIN', 'sfx', '0')
                            sfx_value = 0
                            sfx.texture = sfx_off_active_tx
                            update_sfx()
                        else:
                            config.set('MAIN', 'sfx', '1')
                            sfx_value = 1
                            sfx.texture = sfx_on_active_tx
                            update_sfx()
                    
                    if (x in range(music.pos[0] - music.width, music.pos[0]) and y in range(music.pos[1] - music.height, music.pos[1])):
                        if music_value == 1:
                            config.set('MAIN', 'music', '0')
                            music_value = 0
                            music.texture = music_off_active_tx
                            pygame.mixer.music.stop()
                        else:
                            config.set('MAIN', 'music', '1')
                            music_value = 1
                            music.texture = music_on_active_tx
                            pygame.mixer.music.play(-1)
                        
                    if (x in range(back.pos[0] - back.width, back.pos[0]) and y in range(back.pos[1] - back.height, back.pos[1])):
                       in_settings = 0
                else: 
                    if (x in range (settings.pos[0] - settings.width, settings.pos[0]) and y in range(settings.pos[1] - settings.height, settings.pos[1])):
                       in_settings = 1
                    if (x in range(int(play.pos[0]) - play.width, int(play.pos[0])) and y in range(int(play.pos[1] - play.height), int(play.pos[1]))):
                        in_menu = 0
            if event.button == 1 and in_menu == 0 and began == 0:
                if (x in range(back.pos[0] - back.width, back.pos[0]) and y in range(back.pos[1] - back.height, back.pos[1])):
                       in_menu = 1
                         
            
    # Spawnowanie rur   
    if spawn_PipeandPoint == spawn_PipeandPoint_max and player.dead == False:
        new_pipe = Pipe()
        pipes.add(new_pipe)
        new_point = Point()
        points.add(new_point)
        spawn_PipeandPoint = -1
        
    spawn_PipeandPoint += 1
    
    
    # Spawnowanie chmur
    if spawn_cloud == spawn_cloud_max:
        new_cloud = Cloud()
        spawn_cloud_max = 2 * new_cloud.width
        clouds.add(new_cloud)
        spawn_cloud = -1
    spawn_cloud += 1
        
  
    
    if began == 0:
        player.vel.y = 0
        gravity = 0
        
        if player.pos.y >= screen_height / 2 + 10:
            up_down = 1
        if player.pos.y <= screen_height / 2 - 10:
            up_down = -1
        if up_down == -1:
            player.pos.y += 0.3
        if up_down == 1:
            player.pos.y -= 0.3
            
        spawn_PipeandPoint = 50
                   
        
    # Tło
    background.update()
   
    # Aktualizacja Sprite'ow    
    player.update()
    points.update()
    clouds.update()
    pipes.update()
    buttons.update()
    ground.update()
    
    # Rysowanie tła
    screen.blit(background.texture, background.rect1)
    screen.blit(background.texture, background.rect2)
    
    # Rysowanie chmur
    for entity in clouds:
        screen.blit(entity.texture, entity.rect)
    
    # Uderzenie o ziemię
    if player.pos.y == screen_height - 180 and player.dead == False:
        death()


    # Rysowanie i kolizje rur
    for entity in pipes:  
        #Rysowanie rur
        screen.blit(entity.texture_top, entity.rect_top)
        screen.blit(entity.texture_bot, entity.rect_bot)
        
        # Kolizje górnej rury
        if entity.rect_top.colliderect(player.rect) and player.dead == False:
            death()

        # Kolizje dolnej rury   
        if entity.rect_bot.colliderect(player.rect) and player.dead == False:
            death()
            
            
    # Rysowanie i kolizje punktów
    for entity in points:       
        # Rysowanie punktów
        screen.blit(entity.surf, entity.rect)
        
        # Kolizje punktów
        if entity.rect.colliderect(player.rect):
            entity.kill()
            player.score += 1
            pygame.mixer.Sound.play(point_sound)
            print('Current score: ' + str(player.score))
           
            
    # Rysowanie podłogi i gracza       
    screen.blit(ground.texture, ground.rect1)
    screen.blit(ground.texture, ground.rect2)
    screen.blit(player.texture, player.rect)
    
    
    # Licznik punktów
    if began == 1:
        TextWithOutline('score:', r'font\04B_19.ttf', 30, (255, 255, 235), (32, 32, 32), screen_width / 2, 50)
        TextWithOutline(str(player.score), r'font\04B_19.ttf', 90, (255, 255, 235), (32, 32, 32), screen_width / 2, 125)
        if new_hiscore == 1:
            TextWithOutline('NEW high score:', r'font\04B_19.ttf', 30, (245, 228, 82), (188, 140, 46), screen_width - 200, screen_height - 80)
            TextWithOutline(config.get('MAIN', 'hiscore'), r'font\04B_19.ttf', 30, (245, 228, 82), (188, 140, 46), screen_width - 45, screen_height - 80)
            
        else:
            TextWithOutline('high score:', r'font\04B_19.ttf', 30, (255, 255, 235), (32, 32, 32), screen_width - 160, screen_height - 80)
            TextWithOutline(config.get('MAIN', 'hiscore'), r'font\04B_19.ttf', 30, (255, 255, 235), (32, 32, 32), screen_width - 45, screen_height - 80)
    else:
        TextWithOutline('Crappy', r'font\04B_19.ttf', 115, (245, 228, 82), (188, 140, 46), screen_width / 2, 125)
        TextWithOutline('Bird', r'font\04B_19.ttf', 115, (245, 228, 82), (188, 140, 46), screen_width / 2, 235)
        
        if in_menu == 0:
            TextWithOutline('Tap UP or SPACE to begin', r'font\04B_19.ttf', 30, (255, 255, 235), (32, 32, 32), screen_width / 2, screen_height / 2 - 100)
            TextWithOutline('high score:', r'font\04B_19.ttf', 30, (255, 255, 235), (32, 32, 32), screen_width - 160, screen_height - 80)
            TextWithOutline(config.get('MAIN', 'hiscore'), r'font\04B_19.ttf', 30, (255, 255, 235), (32, 32, 32), screen_width - 45, screen_height - 80)
            screen.blit(back.texture, back.rect)
            
        elif in_menu == 1:
            if in_settings == 0:
                screen.blit(settings.texture, settings.rect)
                screen.blit(play.texture, play.rect)
            else:
                screen.blit(sfx.texture, sfx.rect)
                screen.blit(music.texture, music.rect)
                screen.blit(back.texture, back.rect)
                   
    
    # Game Over Screen
    if player.dead == True:
        if player_character[0] == 'sus':
            TextWithOutline('Red sus', r'font\04B_19.ttf', 90, (255, 255, 235), (32, 32, 32), screen_width / 2, screen_height / 2 - 90)
            TextWithOutline('Red is sus', r'font\04B_19.ttf', 50, (255, 255, 235), (32, 32, 32), screen_width / 2, screen_height / 2)
            TextWithOutline('I saw him vent', r'font\04B_19.ttf', 50, (255, 255, 235), (32, 32, 32), screen_width / 2, screen_height / 2 + 60)
        elif player_character[0] == 'mario':
            TextWithOutline('MAMMA MIA!', r'font\04B_19.ttf', 90, (255, 255, 235), (32, 32, 32), screen_width / 2, screen_height / 2 - 90)
            TextWithOutline('The princess is', r'font\04B_19.ttf', 50, (255, 255, 235), (32, 32, 32), screen_width / 2, screen_height / 2) 
            TextWithOutline('in another castle!', r'font\04B_19.ttf', 50, (255, 255, 235), (32, 32, 32), screen_width / 2, screen_height / 2 + 60)
        elif player_character[0] == 'thanos':
            TextWithOutline('I...', r'font\04B_19.ttf', 90, (255, 255, 235), (32, 32, 32), screen_width / 2, screen_height / 2 - 90)
            TextWithOutline('I dont feel so good...', r'font\04B_19.ttf', 50, (255, 255, 235), (32, 32, 32), screen_width / 2, screen_height / 2)     
        elif player_character[0] == 'gg':
            TextWithOutline('no hej :)', r'font\04B_19.ttf', 90, (255, 255, 235), (32, 32, 32), screen_width / 2, screen_height / 2 - 90)
            TextWithOutline('jestes???', r'font\04B_19.ttf', 50, (255, 255, 235), (32, 32, 32), screen_width / 2, screen_height / 2) 
        else:
            TextWithOutline('Game over', r'font\04B_19.ttf', 90, (255, 255, 235), (32, 32, 32), screen_width / 2, screen_height / 2 - 90)
            TextWithOutline("Press 'R' to restart", r'font\04B_19.ttf', 50, (255, 255, 235), (32, 32, 32), screen_width / 2, screen_height / 2)
            
           
    pygame.display.flip()
    FramePerSec.tick(FPS)
    
with open('config.ini', 'w') as configfile:
    config.write(configfile)
    
pygame.quit()