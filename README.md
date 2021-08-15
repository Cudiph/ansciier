# Ansciier
Mimic video or image to your terminal

## Overview
![demo](https://user-images.githubusercontent.com/59413417/129385066-df1d222b-9233-48fd-b193-4f8497341222.gif)

## How to use it
1. First you need [python 3][python], I reccomend the latest version but I think it would run on older version too.
2. Install the package with `$ pip install ansciier` or `pip3` if pip is point to python 2 version.
3. Run it with `$ ansciier /path/to/image-or-video.mp4`.
4. Type `$ ansciier -h` for help.

## Example usage
- `$ ansciier ~/Videos/rickroll.mp4 --aspect-ratio 20:9 --fps 24`  
Command above will draw frame from rickroll.mp4 in Videos folder with aspect ratio of 20:9 and max fps at 24

- `$ ansciier ~/Video/frame{0}.png --ascii --char @ --dim 200x50 --start-frame 59`  
This command will draw image with `@` character, 200x50 square block dimension from frame59.png, frame60.png, until it reaches the highest frame number. It'll automatically find the last frame when `--last-frame` is not specified, it'll still continue if a frame is missing.

- `$ ansciier camera` will use your camera

Note : Support only truecolor terminal (Because majority of terminals nowadays are truecolor I think you already have one).

[python]: https://www.python.org/downloads/release/python-396/