from PIL import Image
from math import sqrt, ceil

# this takes a pixel * pixel region of the image and averages
# the colours to an (r,g,b) tuple.
def average_colour(x: int, y: int, pixel: int, image):

    img = image.load()
    width, height = image.size
    r, g, b = 0, 0, 0
    counter = 0

    # boundary conditions.
    if x + pixel >= width or y + pixel >= height:
        if x >= width - 1 or y >= height - 1:
            r, g, b = img[x,y]
            return (r, g, b)
        pixel = min(abs(width - x) - 1, abs(height - y) - 1)
    for i in range(x, x + pixel + 1):
        for j in range(y, y + pixel + 1):
            temp_r, temp_g, temp_b = img[i, j]
            r += temp_r
            g += temp_g
            b += temp_b
            counter += 1
    return (r / counter, g / counter, b / counter)

def average_image(pixel: int, filename: str):

    image = Image.open(filename).convert("RGB")
    width, height = image.size
    rgb_chart = []
    x_pixels = ceil(width / pixel)
    y_pixels = ceil(height / pixel)

    for x in range(x_pixels):
        column = []
        for y in range(y_pixels):
            column.append(average_colour(x * pixel, y * pixel, pixel, image))
        rgb_chart.append(column)
    return {"rgb": rgb_chart, "width": width, "height": height}

def rms_greyscale(r: int, g: int, b: int):
    rms = sqrt(1/3 * (r**2 + g**2 + b**2) )
    return round(rms)

# higher powers increase contrast. not used by default.
def n_greyscale(n: int, r: int, g: int, b: int):
    power = (1/3 * (abs(r**n) + abs(g**n) + abs(b**n)) )**(1/n)
    return round(power)

def make_ascii(charset: list, pixel: int, filename: str):

    data = average_image(pixel, filename)
    rgb = data["rgb"]
    LoD = len(charset) - 1
    width = len(rgb)
    height = len(rgb[0])

    with open("ascii_art.txt", "w") as over:
        over.write("")
    with open("ascii_art.txt", "a") as file:
        for y in range(height):
            for x in range(width):
                entry = rgb[x][y]
                brightness = int(round(rms_greyscale(entry[0], entry[1], entry[2]) * (LoD / 255)))
                file.write(charset[brightness] + " ")
            file.write("\n")

if __name__ == "__main__":

    # customise your character set here (light to dark)
    # you can have arbitrarily many characters in it.
    charset = [" ", "`", ".", "-", "=", "+", "e", "m", "#", "@"]
        
    while True:
        filename = input("Enter the filename of the image to be converted\n>> ")
        pixel = input("Enter how the size of each pixel. Smaller means\na more detailed end-result.\n>> ")
        try:
            make_ascii(charset, int(pixel), filename)
            break
        except:
            print("No such file found / invalid pixel size.")