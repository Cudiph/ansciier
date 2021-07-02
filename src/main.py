import cv2 as cv
import os
from pathlib import Path
from random import randrange
import time

ROOT = Path(__file__).parent.parent

def get_last_frame() -> int:
    last_frame = 0
    for i in os.listdir(os.path.join(ROOT, 'frames')):
        frame_number = int(i.replace('.jpg', ''))
        if frame_number > last_frame:
            last_frame = frame_number

    return last_frame
            

def main():
    # SCALE = 1
    start_frame = 1
    last_frame = get_last_frame() + 1
    # delta_time = 0
    prev_time = 0

    for i in range(start_frame, last_frame):
        img_path = os.path.join(ROOT, 'frames', f'{i}.jpg')
        img = cv.imread(img_path)
        ascii_pixel = ''

        for row in range(img.shape[0]):
            for col in range(img.shape[1]):
                R, G, B = img[row, col]
                if R > 230 and G > 230 and B > 230:
                    ascii_pixel += chr(randrange(33, 127)) # random character
                else:
                    ascii_pixel += ' '
            ascii_pixel += '\n'


        # to gain "stable frame rate" you need to adjust the delay value
        # uncomment and print the delta_time and predict the highest value
        # bigger resolution is slower
        delay = 0
        while time.time() * 1000 < prev_time + delay:
            pass

        print(ascii_pixel)
        print(f'frame: {i}')
        
        # debugging purpose
        delta_time = time.time() * 1000 - prev_time
        # print(delta_time)
        fps = 1000 / delta_time
        print(f'fps: {fps}')

        
        prev_time = time.time() * 1000

        # os.system('cls' if os.name == 'nt' else 'clear')
        

if __name__ == '__main__':
    main()
