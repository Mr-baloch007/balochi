import os, platform
os.system('git pull')

import requests

bit = platform.architecture()[0]

if bit == '64bit':
    from SKB64 import fia
    fia()

elif bit == '32bit':

    from SKB32 import fia

    fia()
