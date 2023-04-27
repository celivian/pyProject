from PIL import Image, ImageDraw


def wayward(name, size, width, color):
    im = Image.open(name)
    x, y = im.size
    im2 = im.crop((x // 2 - size // 2, y // 2 - size // 2, x // 2 + size // 2, y // 2 + size // 2))
    x2, y2 = im2.size
    im3 = Image.new('RGB', (x2 * 2 + width * 2, y2 + width * 2), color)
    x3, y3 = im3.size
    im3.paste(im2, (width, width))
    im4 = im2.transpose(Image.FLIP_LEFT_RIGHT)
    im3.paste(im4, (width + size, width))
    im3.save('reflection.png')


wayward('img_4.png', 300, 20, '#760606')
