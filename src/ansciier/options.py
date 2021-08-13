import argparse

def parse_args():
    parser = argparse.ArgumentParser(
        description='Mimic image or video in your terminal')
    parser.add_argument(
        'path',
        type=str,
        help=('the path of the picture/video use "{0}" like "frame{0}.jpg" if '
              'the images name is frame1.jpg, frame2.jpg, ...'))
    parser.add_argument('--ascii',
                        help='whether using ascii characters or ansi escape code',
                        action='store_true')
    parser.add_argument(
        '--char',
        help=('pass a character to get fixed character instead of some '
              'random text (must be used it with "--ascii" opt)'),
        type=str,
        default=None)
    parser.add_argument('--fps', type=int,help='maximum fps', default=60)
    parser.add_argument('--start-frame',
                        type=int,
                        default=1,
                        metavar='NUMBER',
                        help='set the first frame played')
    parser.add_argument('--last-frame',
                        type=int,
                        default=None,
                        metavar='NUMBER',
                        help='set the last frame played (not work for video)')
    parser.add_argument('-v',
                        '--verbose',
                        help='show some information',
                        action='store_true')

    dim_group = parser.add_mutually_exclusive_group()
    dim_group.add_argument(
        '--dim',
        help='fixed dimension to display in terminal (example: 480x360)',
        metavar='WIDTHxHEIGHT',
        type=str,
        default=None)
    dim_group.add_argument(
        '--aspect-ratio',
        help=
        ('preferred aspect ratio to fix stretched image while printing in terminal, '
         'result will change dynamically based on terminal size (usage: 16:9, 4:3, 10:5, ...). '
         'Try increasing the height value if the image stretched vertically and '
         'vice versa if streched horizontally.'),
        metavar='RATIO',
        type=str,
        default=None)

    return parser.parse_args()
