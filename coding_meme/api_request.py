import glob
from PIL import Image
import os
count = 1
for filepath in glob.z('C:\\Users\\jabbe\\PycharmProjects\\MainProject\\program_memes/*png'):
    os.rename(filepath,f'C:\\Users\\jabbe\\PycharmProjects\\MainProject\\program_memes\\meme{count}.png')
    count += 1

