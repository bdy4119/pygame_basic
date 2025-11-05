import pygame

# 초기화 (반드시 해줘야함)
pygame.init()

# 화면 크기 설정
screen_width = 480  # 가로
screen_height = 640 # 세로

screen = pygame.display.set_mode((screen_width, screen_height))


# 화면 타이틀
pygame.display.set_caption("Soda Game") # 게임 이름


#FPS(frames per second) : 초당 프레임 수
clock = pygame.time.Clock()


# 배경 이미지
background = pygame.image.load("C:\\Users\\PC\\Desktop\\_study\\_python\\_study\\pygame_basic\\background.png")


# 캐릭터(스프라이트) 불러오기
character = pygame.image.load("C:\\Users\\PC\\Desktop\\_study\\_python\\_study\\pygame_basic\\soda.png")

character_size = character.get_rect().size  # 이미지 크기 구해옴
character_width = character_size[0]         # 캐릭터 가로 크기
character_height= character_size[1]         # 캐릭터 세로 크기

character_x_pos = (screen_width / 2) - (character_width / 2)                    # 화면 가로의 절반의 위치
character_y_pos = screen_height - character_height                              # 화면 세로 크기의 맨 아래 위치


# 이동 좌표
to_x = 0
to_y = 0


# 이동 속도
speed = 0.3


# 적 캐릭터
enemy = pygame.image.load("C:\\Users\\PC\\Desktop\\_study\\_python\\_study\\pygame_basic\\enemy_soda.png")

enemy_size = character.get_rect().size
enemy_width = character_size[0]
enemy_height= character_size[1]

enemy_x_pos = (screen_width / 2) - (enemy_width / 2)
enemy_y_pos = (screen_height / 2) - (enemy_height / 2)


# 폰트 정의
game_font = pygame.font.Font(None, 40)


# 총 시간
total_time = 10


# 시작 시간 정보
start_ticks = pygame.time.get_ticks()   # 시작 tick 받아오기


# 이벤트 루프
running = True  # 게임 진행 여부
while running :
    # 프레임 수 설정
    dt = clock.tick(60)

    # 사용자의 동작이 들어오는지 체크
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :      # 사용자가 창을 닫을 경우
            running = False

        if event.type == pygame.KEYDOWN :       # 키가 눌러졌는지
            if event.key == pygame.K_LEFT :     # 왼쪽
                to_x -= speed
            elif event.key == pygame.K_RIGHT :  # 오른쪽
                to_x += speed
            elif event.key == pygame.K_UP :     # 위
                to_y -= speed
            elif event.key == pygame.K_DOWN :   # 아래
                to_y += speed

        if event.type == pygame.KEYUP :         # 방향키를 떼면 멈춤
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT :
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN :
                to_y = 0

    character_x_pos += to_x * dt
    character_y_pos += to_y * dt

    # 화면 넘어가기 방지(가로)
    if character_x_pos < 0 :
        character_x_pos = 0
    elif character_x_pos > screen_width -  character_width:
        character_x_pos = screen_width -  character_width
    
    # 화면 넘어가기 방지(세로)
    if character_y_pos < 0 :
        character_y_pos = 0
    elif character_y_pos > screen_height -  character_height:
        character_y_pos = screen_height -  character_height


    # 충돌처리를 위한 rect 정보 업데이트
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos


    # 충돌 체크
    if character_rect.colliderect(enemy_rect) :   # 해당 사각형 위주로 충돌이 발생했는지
        print("충돌 발생")
        running = False


    # 타이머 넣기
    # 경과 시간
    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000   # 경과시간(ms)을 1000으로 나누어 초 단위로 표시

    timer = game_font.render(str(int(total_time - elapsed_time)), True, (0, 0, 0))
    if total_time - elapsed_time <= 0 :
        running = False


    # 배경 위치 지정
    screen.blit(background, (0, 0))

    screen.blit(character, (character_x_pos, character_y_pos))
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos))

    screen.blit(timer, (10, 10))

    # 게임 화면을 다시 그리기 (매 프레임마다 화면을 그려줘야함)
    pygame.display.update()
    """
    RGB값으로 배경 지정
    - screen.fill((0, 0, 255))
    """


# 대기
pygame.time.delay(500)


# pygame 종료
pygame.quit()
