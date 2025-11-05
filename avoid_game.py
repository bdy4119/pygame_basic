# 떨어지는 물체 피하기 게임

import pygame
import random

pygame.init()

pygame.display.set_caption("Soda Avoid Game")

clock = pygame.time.Clock()

# 화면 크기
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

background = pygame.image.load("C:\\Users\\PC\\Desktop\\_study\\_python\\_study\\pygame_basic\\background.png")

# 캐릭터
cat = pygame.image.load("C:\\Users\\PC\\Desktop\\_study\\_python\\_study\\pygame_basic\\soda.png")
cat_size = cat.get_rect().size
cat_width = cat_size[0]
cat_height = cat_size[1]

cat_x_pos = (screen_width / 2) - (cat_width / 2)
cat_y_pos = screen_height - cat_height

cat_speed = 10


# 떨어지는 물체
fall = pygame.image.load("C:\\Users\\PC\\Desktop\\_study\\_python\\_study\\pygame_basic\\enemy_soda.png")
fall_size = fall.get_rect().size
fall_width = fall_size[0]
fall_height = fall_size[1]

fall_x_pos = 0
fall_y_pos = 0

fall_speed = 30

# 이동 좌표
to_x = 0

running = True
while(running) :
    dt = clock.tick(30)

    fall_y_pos += fall_speed * dt / 100
    
    # 떨어지는 물체가 사라지면 떨어지는 물체의 세로 위치 다시 초기화
    if fall_y_pos > screen_height :
        fall_y_pos = 0
        fall_x_pos += random.randint(0, screen_width - fall_width)

    # 가로 화면 넘어가는 거 방지
    if fall_x_pos < 0 :
        fall_x_pos = 0
    elif fall_x_pos > screen_width - fall_width :   # 가로 화면을 벗어날 경우, 가로 화면 위치 초기화 한 뒤, 랜덤한 값 다시 더하기
        fall_x_pos -= random.randint(0, screen_width - fall_width)


    for active in pygame.event.get() :
        if active.type == pygame.QUIT :
            running = False
        
        if active.type == pygame.KEYDOWN :
            if active.key == pygame.K_LEFT :
                to_x -= cat_speed
            elif active.key == pygame.K_RIGHT :
                to_x += cat_speed
        
        if active.type == pygame.KEYUP :
            if active.key == pygame.K_LEFT or active.key == pygame.K_RIGHT :
                to_x = 0

    cat_x_pos += to_x * dt / 50

    if cat_x_pos < 0 :
        cat_x_pos = 0
    elif cat_x_pos > screen_width - cat_width :
        cat_x_pos = screen_width - cat_width


    screen.blit(background, (0, 0))
    screen.blit(cat, (cat_x_pos, cat_y_pos))
    screen.blit(fall, (fall_x_pos, fall_y_pos))

    pygame.display.update()


pygame.quit()