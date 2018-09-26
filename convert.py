import os
import shutil
import sys
import rawpy
import imageio
from glob import glob


def convert():
  path = sys.argv[1].strip('\'').strip('"')
  targets = os.listdir(path)#(path + '*.nef') + glob(path + '*.raf') + glob(path + '*.NEF') + glob(path + '*.RAF')
  i = 1
  total = len(targets)
  failed = []
  for target in targets:
    print("Attempting {} of {}".format(i, total))
    i += 1
    filename, file_extension = os.path.splitext(target)
    if not file_extension.lower() in ('.nef', '.raf'):
      print('Skipping {}'.format(target))
      continue
    if os.path.isfile(filename + '.jp2'):
      print('Skipping the already converted {}'.format(target))
      continue
    print('Attempting to convert {}'.format(target))
    try:
      with rawpy.imread(path + target) as raw:
        rgb = raw.postprocess()
      base = os.path.splitext(target)[0]
      print('Saving converted verison of {}'.format(target))
      imageio.imsave(path + filename + '.jp2', rgb)
    except Exception as e:
      print('Could not convert {}'.format(target))
      print('Reason: {}'.format(str(e)))
      failed.append(target)
      continue
  print("------FAILURES-----------")
  for failure in failed:
    print(failure)

if __name__ == "__main__":
  convert()
