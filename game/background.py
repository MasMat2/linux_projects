from PIL import Image
import os, sys


letters = []

print(os.listdir(os.getcwd()+'/frames'))
directory = os.getcwd()+'/frames'

for f in sorted(os.listdir(directory)):
    if f:
        frame = directory + '/' + f
        image = Image.open(frame)
        print(image.size)
        image_out = Image.new('RGBA',image.size)

        fn, fext = os.path.splitext(f)
        imrgb = image.convert('RGBA')
        pixels = list(imrgb.getdata())

        grey = []
        for pixel in range(len(pixels)):
            bong = pixels[pixel]

            if pixels[pixel] == (218, 229, 214, 255):
                try:
                    if pixels[pixel-1] == (218, 229, 214, 255) or pixels[pixel+1] == (218, 229, 214, 255):
                        bong = (255, 255, 255, 0)
                except IndexError:
                    print(pixel)
                    bong = (255, 255, 255, 0)
            grey.append(bong)

        image_out.putdata(grey)
        image_out.save(fn + '.png')
