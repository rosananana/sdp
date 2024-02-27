import numpy as np
import pygame
import time

# global variables
LS = []; LT = []; RS = []; RT = []
SCREEN_W = 600; SCREEN_H = 600
X_CENTER = SCREEN_W * 0.5; Y_CENTER = SCREEN_H * 0.5
LEG_LENGTH = 100;
SAMPLING = 15;
# one leg high knee 360 - just left leg doing high knees in a circle
# datarun = r"/Users/rosanacho/Desktop/school/sdp visual/one leg high knee 360/data.run"
# walk and turn - walks forward a bit and then 180 and walks back
datarun = r"/Users/rosanacho/Desktop/school/sdp visual/walk and turn/data.run"
# shoes = "shoe_2.png"

def reading():
    file = open(datarun, "r")
    file.readline()
    file.readline()
    for line in file:
        temp = line.split(",")
        LT.append([float(temp[0]), float(temp[1]), float(temp[2])])
        LS.append([float(temp[3]), float(temp[4]), float(temp[5])])
        RT.append([float(temp[6]), float(temp[7]), float(temp[8])])
        RS.append([float(temp[9]), float(temp[10]), float(temp[11])])
    
    file.close()


def get_knee_pos(iteration: float, leg: str, point: str):
    
    if leg == "L":
        rad_thigh = np.pi / -180 * LT[iteration][0]
        rad_shank = np.pi / -180 * LS[iteration][0]
    elif leg == "R":
        rad_thigh = np.pi / 180 * RT[iteration][0]
        rad_shank = np.pi / 180 * RS[iteration][0]
    
    knee_x = LEG_LENGTH * np.sin(rad_thigh)
    knee_y = LEG_LENGTH * np.cos(rad_thigh)

    if point == "K":
        return [X_CENTER + knee_x, Y_CENTER + knee_y]
    elif point == "S":
        shank_x = LEG_LENGTH * np.sin(rad_shank)
        shank_y = LEG_LENGTH * np.cos(rad_shank)
        return [X_CENTER + knee_x + shank_x, Y_CENTER + knee_y + shank_y]
    

def main():
    reading()

    pygame.init()
    pygame.display.init()
    window = pygame.display.set_mode((SCREEN_W, SCREEN_W))
    pygame.display.set_caption("2D Animation - Lateral Perspective")
    window.fill((0, 0, 0))

    # displaying text
    font_a = pygame.font.SysFont("Arial", 40)
    font_b = pygame.font.SysFont("Arial", 24)

    # initialize top of thigh position at center of screen
    l_thigh_pos = [X_CENTER, Y_CENTER]
    r_thigh_pos = [X_CENTER, Y_CENTER]

    iteration = 0
    running = True
    while running == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # left and right knee pos
        l_knee_pos = get_knee_pos(iteration, "L", "K")
        r_knee_pos = get_knee_pos(iteration, "R", "K")

        # left and right shank pos
        l_shank_pos = get_knee_pos(iteration, "L", "S")
        r_shank_pos = get_knee_pos(iteration, "R", "S")       

        # displaying knee angles of respective legs
        left = "Left: "; left_text = font_a.render(left, True, (0, 0, 255), (255, 0 , 0))
        l_angle = str(round(LT[iteration][0] - LS[iteration][0], 2))
        l_angle_text = font_a.render(l_angle, True, (255, 255, 255), (0, 0 , 0))

        right = "Right: "; right_text = font_a.render(right, True, (128, 0, 128), (0, 255, 0))
        r_angle = str(round(RS[iteration][0] - RT[iteration][0], 2))
        r_angle_text = font_a.render(r_angle, True, (255, 255, 255), (0, 0 , 0))

        window.blit(left_text, (50, 100)); window.blit(l_angle_text, (140, 100))
        window.blit(right_text, (50, 150)); window.blit(r_angle_text, (160, 150))

        pygame.draw.line(window, (0, 0, 255), l_thigh_pos, l_knee_pos) # blue = left thigh
        pygame.draw.line(window, (255, 0, 0), l_knee_pos, l_shank_pos) # red = left shank
        pygame.draw.line(window, (0, 255, 0), r_thigh_pos, r_knee_pos) # green = right thigh
        pygame.draw.line(window, (128, 0, 128), r_knee_pos, r_shank_pos) # yellow = right shank

        # adding shoes lol
        # shoe_l = pygame.image.load(shoes); shoe_r = pygame.image.load(shoes)
        # shoe_l = pygame.transform.scale(shoe_l, (40, 50)); shoe_r = pygame.transform.scale(shoe_r, (40, 50))
        # window.blit(shoe_l, (l_shank_pos[0]-30, l_shank_pos[1]-20)); window.blit(shoe_r, (r_shank_pos[0]-30, r_shank_pos[1]-20))

        # displaying length of activity
        activity = "Length of activity: " + str(round(iteration / SAMPLING, 2))
        activity_length = font_b.render(activity, True, (255, 255, 255), (0, 0, 0))
        window.blit(activity_length, (50, 50)) 

        time.sleep(1 / SAMPLING)
        # time.sleep(.2)
        pygame.display.flip()
        iteration += 1
        window.fill((0, 0, 0))

    pygame.quit()

    
if __name__ == "__main__":
    main()
