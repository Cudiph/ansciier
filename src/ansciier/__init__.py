import mimetypes
import os
from pathlib import Path

from .Ansciier import Ansciier
from .options import parse_args

__version__ = '1.0.0'

def main():
    def exists(path: Path, start_frame: int) -> bool:
        if '{0}' not in str(path):
            return os.path.exists(path)
        
        return os.path.exists(str(path).format(start_frame))

    def truthy(res: str) -> bool:
        lower_res = res.lower()
        truth_list = ['yes',  'y', 'yup', 'ya', 'yeah']
        if lower_res in truth_list:
            return True
        else:
            return False
    args = parse_args()

    # constant
    PIC_PATH = Path(args.path).absolute()
    ASCII = args.ascii
    START_FRAME = args.start_frame
    LAST_FRAME = args.last_frame or Ansciier.get_last_frame(
        PIC_PATH, START_FRAME)
    ASPECT_RATIO = [int(x) for x in args.aspect_ratio.split(':', 1)
                    ] if args.aspect_ratio else None
    DIMENSION = [int(x) for x in args.dim.lower().split('x', 1)
                 ] if args.dim else None
    VERBOSE = args.verbose
    CHARACTER = args.char
    MAX_FPS = args.fps

    params = {
        'pic_path': PIC_PATH,
        'ascii': ASCII,
        'start_frame': START_FRAME,
        'last_frame': LAST_FRAME,
        'aspect_ratio': ASPECT_RATIO,
        'dimension': DIMENSION,
        'verbose': VERBOSE,
        'char': CHARACTER,
        'max_fps': MAX_FPS,
    }

    ansciier = Ansciier(params)

    if START_FRAME >= LAST_FRAME:
        print('Bad expression for start_frame and last_frame')
        return

    if os.path.basename(PIC_PATH).lower() == 'camera':
        ansciier.draw_from_vid(True)

    elif not exists(PIC_PATH, START_FRAME):
        print('File doesn\'t exist')

        if truthy(input('Do you want to use camera? ')):
            ansciier.draw_from_vid(True)
        else:
            print('OK.')
            return

    elif 'image' in mimetypes.guess_type(PIC_PATH.__str__())[0]:
        ansciier.draw_from_img()
    elif 'video' in mimetypes.guess_type(PIC_PATH.__str__())[0]:
        ansciier.draw_from_vid(False)
    else:
        print('File is not supported')

    
    if VERBOSE:
        ansciier.stats()
    
    print('Done.')
