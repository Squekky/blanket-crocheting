import os
from PIL import Image
from split_image import split_image

width = 80
height = 100
imagePath = ""
directory = "images"
split_image(imagePath, height, width, should_cleanup=False, should_square=False, should_quiet=True, output_dir=directory)
graph = Image.new('RGB', (width, height))
x = 0
y = 0
for filename in os.listdir(directory):
    file = os.path.join(directory, filename)
    newImage = Image.open(file).convert('RGB')
    colors = newImage.getcolors()
    domColor = ()
    domAmount = 0
    #print(f"{filename} - {colors}")
    for color in colors:
        if color[0] > domAmount:
            domAmount = color[0]
            domColor = color[1]
    if domColor == (0, 0, 0):
        domColor = (10, 30, 112)
    elif domColor == (255, 0, 0):
        domColor = (255, 255, 255)
    elif domColor == (255, 255, 255):
        domColor = (251, 183, 54)
    pixelNum = int(filename[4:-4])
    x = (pixelNum) % (width)
    y = (pixelNum - x) // (width)
    #print(f"x = {x}, y = {y}")
    graph.putpixel((x, y), domColor)

graph.show()
graph.save("graph.png")