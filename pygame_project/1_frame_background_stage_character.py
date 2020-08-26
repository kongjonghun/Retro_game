import os
import pygame
###################################################################
# 기본 초기화 
pygame.init() 

# 화면 크기 설정
screen_width=640 # 가로 크기
screen_height=480 # 세로 크기
screen = pygame.display.set_mode((screen_width,screen_height))

# 화면 타이틀 설정(게임 이름)
pygame.display.set_caption("Kkongchi Game2") 

#FPS  = Frame Per Second 
clock = pygame.time.Clock()
###################################################################
# 1. 사용자 게임 초기화
current_path = os.path.dirname(__file__) # 현재 파일 위치 반환
image_path = os.path.join(current_path, "images") # images 폴더 위치 반환

# 배경 만들기
background = pygame.image.load(os.path.join(image_path, "background.png"))

# 스테이지 만들기
stage = pygame.image.load(os.path.join(image_path,"stage.png"))
stage_size = stage.get_rect().size
stage_height = stage_size[1]

# 캐릭터 만들기
character = pygame.image.load(os.path.join(image_path, "character.png"))
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = screen_width/2 - character_width/2
character_y_pos = screen_height - character_height - stage_height


running = True # 게임이 진행 중인가?

while running:
# 2. 이벤트 처리 (키보드 , 마우스 등)
    dt = clock.tick(30)                     # 게임 화면의 초당 프레임 수 설정 
    for event in pygame.event.get():        # 어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT:       # 창이 닫히는 이벤트가 발생하였는가?
            running = False                 # 게임이 진행중이 아님
       

# 3. 게임 캐릭터 위치 정의
  
# 4. 충돌 처리
 
# 5. 화면에 그리기
    screen.blit(background,(0,0))                                                   
    screen.blit(stage,(0,screen_height - stage_height))                                                   
    screen.blit(character,(character_x_pos, character_y_pos))    

    pygame.display.update() # 게임화면을 다시 그리기
 
# pygame 종료
pygame.quit()


