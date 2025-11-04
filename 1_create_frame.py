import pygame

# 초기화 (반드시 해줘야함)

# 화면 크기 설정
screen_width = 480  # 가로
screen_height = 640 # 세로

screen = pygame.display.set_mode((screen_width, screen_height))


# 화면 타이틀
pygame.display.set_caption("My Game") # 게임 이름


# 배경 이미지
background = pygame.image.load("C:\\Users\\PC\\Desktop\\_study\\_python\\_study\\pygame_basic\\background.png")


# 캐릭터(스프라이트) 불러오기
character = pygame.image.load("C:\\Users\\PC\\Desktop\\_study\\_python\\_study\\pygame_basic\\soda2.png")

character_size = character.get_rect().size # 이미지 크기 구해옴
character_width = character_size[0] # 캐릭터 가로 크기
character_height= character_size[1] # 캐릭터 세로 크기

character_x_pos = (screen_width / 2) - (character_width / 2)                    # 화면 가로의 절반의 위치
character_y_pos = screen_height - character_height    # 화면 세로 크기의 맨 아래 위치


# 이동 좌표
to_x = 0
to_y = 0


# 이벤트 루프
running = True  # 게임 진행 여부
while running :
    # 사용자의 동작이 들어오는지 체크
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :      # 사용자가 창을 닫을 경우
            running = False

        if event.type == pygame.KEYDOWN :       # 키가 눌러졌는지
            if event.key == pygame.K_LEFT :     # 왼쪽
                to_x -= 1
            elif event.key == pygame.K_RIGHT :  # 오른쪽
                to_x += 1
            elif event.key == pygame.K_UP :     # 위
                to_y -= 1
            elif event.key == pygame.K_DOWN :   # 아래
                to_y += 1

        if event.type == pygame.KEYUP :         # 방향키를 떼면 멈춤
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT :
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN :
                to_y = 0

    character_x_pos += to_x
    character_y_pos += to_y

    if character_x_pos < 0 :
        character_x_pos = 0
    elif character_x_pos > screen_width -  character_width:
        character_x_pos = screen_width -  character_width
    elif character_y_pos < 0 :
        character_y_pos = 0
    elif character_y_pos > screen_height -  character_height:
        character_y_pos = screen_height -  character_height


    # 배경 위치 지정
    screen.blit(background, (0, 0))
    screen.blit(character, (character_x_pos, character_y_pos))

    # 게임 화면을 다시 그리기 (매 프레임마다 화면을 그려줘야함)
    pygame.display.update()
    """
    RGB값으로 배경 지정
    - screen.fill((0, 0, 255))
    """


# pygame 종료
pygame.quit()
