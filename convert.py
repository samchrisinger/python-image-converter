import os
import sys
import rawpy
import imageio
from glob import glob

def convert():
  path = sys.argv[1]
  targets = glob(path + '*.nef') + glob(path + '*.raf') + glob(path + '*.NEF') + glob(path + '*.RAF')
  for target in targets:
    with rawpy.imread(target) as raw:
      rgb = raw.postprocess()
    base = os.path.splitext(target)[0]
    imageio.imsave(base + '.jp2', rgb)

if __name__ == "__main__":
  convert()
