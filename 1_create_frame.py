import pygame

# 초기화 (반드시 해줘야함)

# 화면 크기 설정
screen_width = 480  # 가로
screen_height = 640 # 세로

screen = pygame.display.set_mode((screen_width, screen_height))


# 화면 타이틀
pygame.display.set_caption("My Game") # 게임 이름


# 이벤트 루프
running = True  # 게임 진행 여부
while running :
    # 사용자의 동작이 들어오는지 체크
    for event in pygame.event.get() :
        if event.type == pygame.QUIT : # 사용자가 창을 닫을 경우
            running = False
        


# pygame 종료
pygame.quit()
