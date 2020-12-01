from PIL import Image
import os
import sys


def main():
    print(
        "+---------------------------------+\n" +
        "| Welcome to ImageOverlayMaker v1 |\n" +
        "+---------------------------------+"
    )
    print('First thing\'s first: what directory are we working in?')
    correct_dir = False
    old_dir = os.getcwd()
    while not correct_dir:
        dir_ = input('Enter directory: ')
        os.chdir(dir_)
        print(f'Set working directory to {os.getcwd()}')
        _correct_dir = input('Is this correct [Y/n]? ')
        if not _correct_dir or 'y' in _correct_dir:
            correct_dir = True
        else:
            os.chdir(old_dir)
            print('Whoops! Sorry about that, let\'s try again...')
    print('Great! Next, you\'ll need to select the image you want to put over your other images.')
    mask = None
    while not mask:
        mask = input('Enter image file name: ')
        print(f'Set image to {mask}')
        _correct_mask = input('Is this correct [Y/n]? ')
        if not _correct_mask or 'y' in _correct_mask:
            pass
        else:
            mask = None
            print('Whoops! Sorry about that, let\'s try again...')
    fore = Image.open(mask).convert('RGBA')
    print('Now, we\'re going to need the file(s) you plan to put this image on.')
    _images = input('Input image names: ')
    images = _images.split(',')
    for image in images:
        bg = Image.open(image).convert('RGBA')
        bg.paste(fore, (0, 0), fore)
        bg.save(image)
    print('All done!')
    input('Press any key to continue...')


def fast():
    dir_ = input('Enter directory: ')
    os.chdir(dir_)
    fore = Image.open('mask.png').convert('RGBA')
    for image in [f for f in os.listdir() if not f == 'mask.png']:
        bg = Image.open(image).convert('RGBA')
        bg.paste(fore, (0, 0), fore)
        bg.save(image)


if __name__ == '__main__':
    if 'fast' in sys.argv:
        fast()
    else:
        main()
