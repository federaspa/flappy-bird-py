import pygame as pg
import sys

pg.init()
screen = pg.display.set_mode((288,512))
pg.display.set_caption('flappy_bird')
font = pg.font.Font(None, 30)
clock = pg.time.Clock()
game_active = 0



bg_surf = pg.image.load('flappy-bird-assets/sprites/background-day.png').convert_alpha()
floor_surf = pg.image.load('flappy-bird-assets/sprites/base.png').convert_alpha()
text_surf = font.render('Score', True, 'Black')
text_rect = text_surf.get_rect(center = (144,100))

# bird
bird_surf = pg.image.load('flappy-bird-assets/sprites/yellowbird-upflap.png').convert_alpha()
bird_rect = bird_surf.get_rect(center = (90, 256))

gravity = 0

# pipes
pipe_up_surf = pg.image.load('flappy-bird-assets/sprites/pipe-green.png').convert_alpha()
pipe_down_surf = pg.transform.flip(pipe_up_surf, 0,1)

pipe_up_rect = pipe_up_surf.get_rect(midtop = (300, 350))
pipe_down_rect = pipe_down_surf.get_rect(midbottom = (300 , 200))

pipe_rects = [pipe_up_rect, pipe_down_rect]

def reset_game():
    pipe_up_rect.midtop = (300, 350)
    pipe_down_rect.midbottom = (300, 200)

    bird_rect.center = (90, 256)

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()

        if game_active:
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    gravity = -15

        else:
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    reset_game()
                gravity = -15
                game_active = 1


    if game_active:
        for pipe in pipe_rects:
            pipe.left -= 3
            if pipe.right < 0:
                pipe.left = 288


        gravity += 1
        bird_rect.y += gravity
        if bird_rect.bottom > 450:
            bird_rect.bottom = 450

        if any(bird_rect.colliderect(pipe) for pipe in pipe_rects):
            game_active = 0

    screen.blit(bg_surf, (0,0))
    screen.blit(text_surf, text_rect)
    screen.blit(bird_surf, bird_rect)
    screen.blit(pipe_up_surf, pipe_up_rect)
    screen.blit(pipe_down_surf, pipe_down_rect)
    screen.blit(floor_surf, (0,450))

    pg.display.update()
    clock.tick(60)