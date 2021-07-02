# ASCII bad apple
Yet another bad apple script

## Prerequisite
- [Python 3.x](https://www.python.org/downloads/)
- [ffmpeg](https://ffmpeg.org/download.html)

## How to run it
1. Extract all the frames in [frames](./frames) folder with ffmpeg:  
  `$ ffmpeg -i ./video.mkv -s 480x360 -sws_flags neighbor ./frames/%0d.jpg`
2. Install pipenv if you don't have it: `$ python -m pip install pipenv`
3. Install required dependencies with pipenv: `$ pipenv install`
4. Run the script with python: `$ pipenv run python ./src/main.py`


