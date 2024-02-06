import glob
from PIL import Image
import os

def file_paths():
    filepaths = []
    for filepath in glob.iglob('C:\\Users\\jabbe\\PycharmProjects\\MainProject\\program_memes/*png'):
        filepaths.append(filepath)
    return filepaths