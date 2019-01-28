from argparse import ArgumentParser
from skimage.io import imsave
from skimage.transform import rescale
import skvideo.io

from pathlib import Path
from tqdm import tqdm
parser = ArgumentParser()
parser.add_argument('--input', type=str)
parser.add_argument('--output_folder', type=str, default='outputs')

opts = parser.parse_args()
output_path = Path(opts.output_folder)
# assert output_path.is_dir()
if not output_path.exists():
    output_path.mkdir()
videodata = skvideo.io.vread(opts.input)
for i, frame in enumerate(tqdm(videodata)):
    frame = rescale(frame, 0.5)
    print(f'frame.shape : {frame.shape}')
    imsave(output_path/f'{i}.png', frame)
