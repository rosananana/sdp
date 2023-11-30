import csv
import turtle
import numpy as np
import pygame
import time


LSx = []; LSy = []; LSz = []; LTx = []; LTy = []; LTz = []
RSx = []; RSy = []; RSz = []; RTx = []; RTy = []; RTz = []
screen_w = 500; screen_h = 500
x_center = screen_w * 0.5; y_center = screen_h * 0.5
leg_length = 100;

def reading():
    file = open("data.run", "r")
    file.readline()
    for line in file:
        temp = line.split(",")
        LTx.append(float(temp[0]))
        LTy.append(float(temp[1]))
        LTz.append(float(temp[2]))
        LSx.append(float(temp[3]))
        LSy.append(float(temp[4]))
        LSz.append(float(temp[5]))
        RTx.append(float(temp[6]))
        RTy.append(float(temp[7]))
        RTz.append(float(temp[8]))
        RSx.append(float(temp[9]))
        RSy.append(float(temp[10]))
        RSz.append(float(temp[11]))
    
    file.close()

# def thigh_knee(thigh, iteration):
#     return (thigh[0] - leg_length * np.sin(LTx[iteration]),
#             thigh[1] + leg_length * np.cos(LTx[iteration]))

# def shank(knee_pos, iteration):
#     return (knee_pos[0] - leg_length * np.sin(LSx[iteration]),
#             knee_pos[1] + leg_length * np.cos(LSx[iteration]))

def main():
    reading()
    pygame.init()
    pygame.display.init()
    window = pygame.display.set_mode((screen_w, screen_h))
    pygame.display.set_caption("2D Animation - Lateral Perspective")
    window.fill((255, 255, 255))

    # initialize position
    l_knee_pos = [x_center, y_center]
    l_thigh_pos = [x_center, y_center]

    r_knee_pos = [x_center, y_center]
    r_thigh_pos = [x_center, y_center]
    
    # knee_angle = LSx[0] + (180 - LTx[0])

    # blue thigh, red shank
    iteration = 1
    running = True
    while running == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        """
        VIDEO GOES:
        LEFT LEG UP -> 
        RIGHT LEG UP -> 
        LEFT LEG UP -> 
        RIGHT LEG UP
        """
        
        # left leg
        l_rad_thigh = np.pi / 180 * LTx[iteration]
        l_rad_shank = np.pi / 180 * LSx[iteration]

        l_knee_x = leg_length * np.cos(l_rad_thigh)
        l_knee_y = leg_length * np.sin(l_rad_thigh)
        l_knee_pos = [x_center + l_knee_x, y_center + l_knee_y]

        l_shank_x = leg_length * np.cos(l_rad_shank)
        l_shank_y = leg_length *  np.sin(l_rad_shank)
        l_shank_pos = [x_center + l_knee_x + l_shank_x, y_center + l_knee_y + l_shank_y]

        # right leg
        r_rad_thigh = np.pi / -180 * RTx[iteration]
        r_rad_shank = np.pi / -180 * RSx[iteration]

        r_knee_x = leg_length * np.cos(r_rad_thigh)
        r_knee_y = leg_length * np.sin(r_rad_thigh)
        r_knee_pos = [x_center + r_knee_x, y_center + r_knee_y]

        r_shank_x = leg_length * np.cos(r_rad_shank)
        r_shank_y = leg_length *  np.sin(r_rad_shank)
        r_shank_pos = [x_center + r_knee_x + r_shank_x, y_center + r_knee_y + r_shank_y]

        # knee_angle = LSx[iteration] - LTx[iteration]
        # print(iteration, knee_angle)
        # print(iteration, "knee:", l_knee_pos)
        # pygame.draw.circle(window, (0, 0, 255), (l_thigh_pos[0], l_thigh_pos[1]), 6)
        # pygame.draw.circle(window, (0, 0, 255), (l_knee_pos[0], l_knee_pos[1]), 6)
        #     #   "shank:", round(shank_x, 2), round(shank_y, 2))

        pygame.draw.line(window, (0, 0, 255), l_thigh_pos, l_knee_pos) # blue = left thigh
        pygame.draw.line(window, (255, 0, 0), l_knee_pos, l_shank_pos) # red = left shank

        pygame.draw.line(window, (0, 255, 0), r_thigh_pos, r_knee_pos) # green = right thigh
        pygame.draw.line(window, (255, 165, 0), r_knee_pos, r_shank_pos) # yellow = right shank

        time.sleep(1 / 30)
        pygame.display.flip()
        iteration += 1
        window.fill((255, 255, 255))

    pygame.quit()
    # print("Length of Activity:", len(LTx) / 15)

    # print("Average Cadence:", )

    
if __name__ == "__main__":
    main()
