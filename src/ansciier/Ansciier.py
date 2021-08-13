import cv2 as cv
import os
from pathlib import Path
from random import randrange
import re
import time

class Ansciier:
    def __init__(self, params=None) -> None:
        if params is None:
            params = {}
        self.params = {}
        self.params.update(params)
        self.lowest_fps = 1000
        self.highest_fps = 0
        self.timer = 0
        self.frame_counter = 0

    @staticmethod
    def get_last_frame(path: Path, start_frame) -> int:
        if '{0}' not in str(path): return start_frame + 1

        basename = os.path.basename(path)

        # filter file based on basename path
        img_list = list(
            filter(
                lambda x: re.match(basename.format(r'\d+'), x),
                os.listdir(path.parent)))

        biggest_frame = 0
        print(img_list)
        for i in img_list:
            frame_number = int(re.findall(basename.format(r'(\d+)'), i)[0])
            if frame_number > biggest_frame: biggest_frame = frame_number

        return biggest_frame

    @staticmethod
    def colorize(text: str,
                 fgBGR: tuple[int, int, int] = None,
                 bgBGR: tuple[int, int, int] = None) -> str:
        # BGR is Blue, Green, Red
        colored_text = ''

        # colorize foreground (the text)
        if fgBGR is not None:
            fgB, fgG, fgR = fgBGR
            colored_text += f'\033[38;2;{fgR};{fgG};{fgB}m'

        # colorize background
        if bgBGR is not None:
            bgB, bgG, bgR = bgBGR
            colored_text += f'\033[48;2;{bgR};{bgG};{bgB}m'

        colored_text += f'{text}\x1b[0m' # close ansi sequence

        return colored_text

    def _debug(self, prev_time: int, curr_frame: int):
        delta_time = time.time() * 1000 - prev_time
        fps = 1000 / delta_time

        self.timer += delta_time
        self.frame_counter += 1

        if self.lowest_fps > fps: self.lowest_fps = fps
        if self.highest_fps < fps: self.highest_fps = fps

        print(f'frame: {curr_frame}')
        print(f'fps: {fps}')
        # print(delta_time)


    def _create_pixel(self, frame) -> str:
        tsize = os.get_terminal_size()

        aspect_ratio = self.params.get('aspect_ratio')
        dim = self.params.get('dimension')
        width = None
        height = tsize.lines

        if dim: # dimension
            width = dim[0]
            height = dim[1]
        elif aspect_ratio: # aspect ratio
            width = int(height * aspect_ratio[0] / aspect_ratio[1])
        else: # default terminal size
            width = int(height * frame.shape[1] / frame.shape[0])

        resized = cv.resize(frame, (width, height))
        pixel = '\n' * tsize.lines
        for row in range(resized.shape[0]):
            for col in range(resized.shape[1]):
                if self.params.get('ascii'):
                    char = self.params.get('char')
                    if char:
                        pixel += self.colorize(char[0], resized[row, col])
                    else:
                        pixel += self.colorize(chr(randrange(33, 127)),
                                           resized[row, col])
                else:
                    pixel += self.colorize(' ', bgBGR=resized[row, col])
            pixel += '\n'
        return pixel

    def draw_from_img(self):
        prev_time = time.time() * 1000
        try:
            for i in range(self.params.get('start_frame'),
                        self.params.get('last_frame')):
                img_path = self.params.get('pic_path').__str__().format(i)

                if not os.path.exists(img_path):
                    continue

                img = cv.imread(img_path)
                ascii_pixel = self._create_pixel(img)

                
                delay = 1000 / self.params.get('max_fps')
                while time.time() * 1000 < prev_time + delay:
                    pass

                print(ascii_pixel)

                # debugging purpose
                if self.params.get('verbose'):
                    self._debug(prev_time, i)
                    
                prev_time = time.time() * 1000
        except KeyboardInterrupt:
            return


    def draw_from_vid(self, camera: bool=False):
        cap = None
        if camera:
            cap = cv.VideoCapture(0)
        else:
            cap = cv.VideoCapture(self.params.get('pic_path').__str__())
            cap.set(1, self.params.get('start_frame'))

        prev_time = time.time() * 1000
        i = 1
        try:
            while cap.isOpened():
                ret, frame = cap.read()

                if not ret:
                    break

                ascii_pixel = self._create_pixel(frame)

                delay = 1000 / self.params.get('max_fps')
                while time.time() * 1000 < prev_time + delay:
                    pass

                print(ascii_pixel) # print to terminal

                # debugging purpose
                if self.params.get('verbose'):
                    self._debug(prev_time, i)
                    
                prev_time = time.time() * 1000
                i += 1
        except KeyboardInterrupt:
            return
    
    def stats(self) -> None:
        print(f'\nTime taken: {round(self.timer / 1000, 2)} seconds')
        print(f'Average fps: {round(self.frame_counter / self.timer * 1000, 2)}')
        print(f'Highest fps: {round(self.highest_fps, 2)}')
        print(f'Lowest fps: {round(self.lowest_fps, 2)}')
        print(f'Frame printed: {self.frame_counter}')
