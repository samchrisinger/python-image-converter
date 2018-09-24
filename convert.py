import os
import sys
import rawpy
import imageio
from glob import glob

def convert():
  path = sys.argv[1].strip('\'').strip('"')
  targets = glob(path + '*.nef') + glob(path + '*.raf') + glob(path + '*.NEF') + glob(path + '*.RAF')
  i = 0
  total = len(targets)
  for target in targets:
    print('Attempting to convert {} ({} of {})'.format(target, i, total))
    with rawpy.imread(target) as raw:
      rgb = raw.postprocess()
    base = os.path.splitext(target)[0]
    print('Saving converted verison of {}'.format(target))
    imageio.imsave(base + '.jp2', rgb)

if __name__ == "__main__":
  convert()
