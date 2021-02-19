import os
import imageio

def makeGIF():
    png_dir = 'fig/'
    images = []
    for file_name in sorted(os.listdir(png_dir)):
        if file_name.endswith('.png'):
            file_path = os.path.join(png_dir, file_name)
            images.append(imageio.imread(file_path))
    imageio.mimsave('movie.gif', images,fps=10)

makeGIF()