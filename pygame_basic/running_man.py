import pygame
import random

pygame.init() #초기화(반드시 필요)

# 화면 크기 설정
screen_width = 480 # 가로 크기
screen_height = 640 # 세로 크기
screen = pygame.display.set_mode((screen_width,screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Kkongchi Game") #게임 이름

#FPS  = Frame Per Second 
clock = pygame.time.Clock()

# 배경 이미지 불러오기
background = pygame.image.load("C:\\Users\\rhd05\\OneDrive\\바탕 화면\\파이썬 프로젝트\\pygame_basic\\background.png")

character_to_x_LEFT=0
character_to_x_RIGHT=0

# 캐릭터 불러오기
character = pygame.image.load("C:\\Users\\rhd05\\OneDrive\\바탕 화면\\파이썬 프로젝트\\pygame_basic\\character.png")
character_size = character.get_rect().size # 이미지의 크기를 가져옴
character_width = character_size[0] # 캐릭터의 가로 크기
character_height = character_size[1] # 캐릭터의 세로 크기
character_x_pos = screen_width/2 -character_width/2# 화면 가로의 절반 크기에 위치
character_y_pos = screen_height - character_height  # 화면 세로의 가장 아래에 위치

# 폰트 정의
game_font = pygame.font.Font(None, 40) # 폰트 객체 생성(폰트, 크기)

# ddong 불러오기
ddong = pygame.image.load("C:\\Users\\rhd05\\OneDrive\\바탕 화면\\파이썬 프로젝트\\pygame_basic\\poop.png")
ddong_size = ddong.get_rect().size              # 이미지의 크기를 가져옴
ddong_width = ddong_size[0]                     # 캐릭터의 가로 크기
ddong_height = ddong_size[1]                    # 캐릭터의 세로 크기
ddong_x_pos = random.randint(0, screen_width - ddong_width)   # 화면 가로의 절반 크기에 위치
ddong_y_pos = 0      # 화면 세로의 가장 아래에 위치
ddong_speed = 13


# 이동 속도
character_speed = 10

# 점수
point =0

# 이벤트 루프
running = True # 게임이 진행 중인가?
while running:
    dt = clock.tick(60)                  # 게임 화면의 초당 프레임 수 설정 
    for event in pygame.event.get():     # 어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT:    # 창이 닫히는 이벤트가 발생하였는가?
            running = False              # 게임이 진행중이 아님
        if event.type == pygame.KEYDOWN: # 방향키 누를경우 움직임
            if event.key == pygame.K_LEFT:
                character_to_x_LEFT -= character_speed
            elif event.key == pygame.K_RIGHT:
                character_to_x_RIGHT += character_speed
        
        if event.type == pygame.KEYUP: # 방향키를 떼면 멈춤
            if event.key == pygame.K_LEFT:
                character_to_x_LEFT = 0 
            elif event.key == pygame.K_RIGHT:
                character_to_x_RIGHT = 0 
        
    
    character_x_pos += (character_to_x_LEFT+character_to_x_RIGHT)            

    # 가로 경계값 처리
    if character_x_pos<0:
        character_x_pos=0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    ddong_y_pos += ddong_speed
    
    if ddong_y_pos >=screen_height:
        ddong_y_pos = 0
        ddong_x_pos = random.randint(0, screen_width - ddong_width)  
        ddong_speed += 0.3
        point += 1

    # 충돌 처리
    character_rect = character.get_rect()  # 캐릭터 객체 생성
    character_rect.left = character_x_pos  # 캐릭터의 실제 위치 부여
    character_rect.top = character_y_pos

    ddong_rect = ddong.get_rect()  # 똥 객체 생성
    ddong_rect.left = ddong_x_pos  # 똥의 실제 위치 부여
    ddong_rect.top = ddong_y_pos


    # 충돌 체크
    if character_rect.colliderect(ddong_rect):
        print("충돌했습니다.")
        running=False

    screen.blit(background, (0,0)) # 배경그리기   // screen.fill((r,g,b)) : 색으로 배경 채우기(이미지x)
    screen.blit(character, (character_x_pos,character_y_pos)) 
    screen.blit(ddong, (ddong_x_pos, ddong_y_pos)) 
    points = game_font.render(str(point),True, (0,0,0))
    screen.blit(points,(10,10))

    pygame.display.update() #게임화면을 다시 그리기

# 잠시 대기
pygame.time.delay(2000)  # 2초 정도 대기(ms)

# pygame 종료
pygame.quit()


