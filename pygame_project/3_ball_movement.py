import os
import pygame
###################################################################
# 기본 초기화 
pygame.init() 

# 화면 크기 설정
screen_width=640 # 가로 크기
screen_height=480 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

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

# 캐릭터 이동
character_to_right = 0 
character_to_left = 0 

# 캐릭터 속도
character_speed = 5

# 무기 만들기
weapon = pygame.image.load(os.path.join(image_path, "weapon.png"))
weapon_size = weapon.get_rect().size
weapon_width = weapon_size[0]
weapon_height = weapon_size[1]

# 무기 여러번 발사
weapons = []

# 무기 이동 속도
weapon_speed = 10

# 공 만들기(4개 크기에 대해 따로 처리)
ball_images = [
    pygame.image.load(os.path.join(image_path, "ballon1.png")),
    pygame.image.load(os.path.join(image_path, "ballon2.png")),
    pygame.image.load(os.path.join(image_path, "ballon3.png")),
    pygame.image.load(os.path.join(image_path, "ballon4.png")),
]

# 공 크기에 따른 최초 스피드
ball_speed_y = [-18, -15, -12, -9]

balls =[]

# 최초 발생하는 큰 공 추가
balls.append({
    "pos_x": 50,  # 공의 x 좌표 
    "pos_y": 50,  # 공의 y 좌표
    "img_idx": 0, # 공의 이미지 인덱스
    "to_x": 3,    # x축 이동방향 
    "to_y": -6,   # y축 이동방향   
    "init_spd_y": ball_speed_y[0] #y 최초 속도
})
 

running = True # 게임이 진행 중인가?

while running:
# 2. 이벤트 처리 (키보드 , 마우스 등)
    dt = clock.tick(30)                     # 게임 화면의 초당 프레임 수 설정 
    for event in pygame.event.get():        # 어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT:       # 창이 닫히는 이벤트가 발생하였는가?
            running = False                 # 게임이 진행중이 아님
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                character_to_left -= character_speed
            elif event.key == pygame.K_RIGHT:
                character_to_right += character_speed
            elif event.key == pygame.K_SPACE:
                weapon_x_pos = character_x_pos + (character_width/2) - (weapon_width/2)
                weapon_y_pos = character_y_pos
                weapons.append([weapon_x_pos, weapon_y_pos])

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT: 
                character_to_left = 0
            elif event.key == pygame.K_RIGHT:    
                character_to_right = 0                


# 3. 게임 캐릭터 위치 정의
    character_x_pos += (character_to_right + character_to_left)

    if character_x_pos<0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width
    
    # 무기 위치 조정
    weapons =[[ w[0], w[1] - weapon_speed ] for w in weapons]

    # 천장에 닿은 무기 없애기
    weapons = [[w[0], w[1]] for w in weapons if w[1]>0 ]


    # 공 위치 정의
    for ball_idx, ball_val in enumerate(balls):
        ball_pos_x = ball_val["pos_x"]
        ball_pos_y = ball_val["pos_y"]
        ball_img_idx = ball_val["img_idx"]

        ball_size = ball_images[ball_img_idx].get_rect().size
        ball_width = ball_size[0]
        ball_height = ball_size[1]

        # 가로벽에 닿았을 때 공 이동 위치 변경(튕겨 나오는 효과)
        if ball_pos_x <= 0 or ball_pos_x >= screen_width - ball_width:
            ball_val["to_x"] = ball_val["to_x"] * (-1)
        
        # 세로 위치 (스테이지에 튀기는 효과)
        if ball_pos_y >= screen_height - stage_height - ball_height:
            ball_val["to_y"] = ball_val["init_spd_y"]
        else: # 그 외에는 속도를 늘림
            ball_val["to_y"] += 0.5

        ball_val["pos_x"] += ball_val["to_x"]
        ball_val["pos_y"] += ball_val["to_y"]



# 4. 충돌 처리

 
# 5. 화면에 그리기
    screen.blit(background,(0,0))                                                   

    for weapon_x_pos, weapon_y_pos in weapons:
        screen.blit(weapon,(weapon_x_pos, weapon_y_pos))

    for idx, val in enumerate(balls):
        ball_pos_x = val["pos_x"]
        ball_pos_y = val["pos_y"]
        ball_img_idx = val["img_idx"]
        screen.blit(ball_images[ball_img_idx],(ball_pos_x,ball_pos_y))

    screen.blit(stage,(0, screen_height - stage_height))                                                   
    screen.blit(character,(character_x_pos, character_y_pos))    

    

    pygame.display.update()  # 게임화면을 다시 그리기
 
# pygame 종료
pygame.quit()


