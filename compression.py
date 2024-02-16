import sys
import os
from PIL import Image

def gen_image(value_matrix, n, time_matrix):
    i = 0
    imgdata = []
    while i < n:
        j = 0
        while j < len(time_matrix):            
            imgdata.append(value_matrix[j][i])
            j += 1
        i += 1
    img = Image.new('L', ( len(time_matrix), n))
    img.putdata(imgdata)
    img.save('EEG-file.JPEG')
    return os.path.join(os.getcwd(), 'EEG-file.JPEG' )

def compress(image_file):

    filepath = os.path.join(os.getcwd(), image_file)

    image = Image.open(filepath)

    image.save("EEG-file-compressed.JPEG",
                 "JPEG",
                 optimize = True,
                 quality = 100)
    return os.path.join(os.getcwd(), "EEG-file-compressed.JPEG")
