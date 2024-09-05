import numpy as np
from PIL import Image


graph = Image.open("graph.png").convert('RGB')
width, height = graph.size
colors = graph.getdata()
np.set_printoptions(threshold=np.inf)
colorArray = np.array(colors)
colorMatrix = [[]]
row = 0
column = 0
blue = 0
yellow = 0
white = 0
for color in colorArray:
    if column == width:
        column = 0
        colorMatrix.append([])
        row += 1
    if list(color) == [251, 183, 54]:
        colorName = "🟨"
        yellow += 1
    elif list(color) == [10, 30, 112]:
        colorName = "🟦"
        blue += 1
    elif list(color) == [255, 255, 255]:
        colorName = "⬜"
        white += 1
    print(f"row = {row}, column = {column}")
    colorMatrix[row].append(colorName)
    column += 1

def diagonal_traversal(matrix):
    if not matrix:
        return []

    rows = len(matrix)
    cols = len(matrix[0])
    result = []
    # Traverse diagonals starting from the bottom right
    for k in range(rows + cols - 1):
        diagonal = []
        if k < cols:
            r, c = rows - 1, cols - 1 - k
        else:
            r, c = rows - 1 - (k - cols + 1), 0

        while r >= 0 and c < cols:
            diagonal.append(matrix[r][c])
            r -= 1
            c += 1
            
        # Append the collected diagonal to the result, alternating the direction
        if k % 2 == 0:
            result.append(diagonal[::-1])  # Reverse for the first diagonal in each pair
        else:
            result.append(diagonal)
    return result
result = diagonal_traversal(colorMatrix)

# Print the result diagonals
downleft = True   # 0 for ⭧, 1 for ⭩
number = 1
for diagonal in result:
    instruction = ""
    previousColor = "🟩"
    currentCount = 0
    for color in diagonal:
        if color != previousColor:
            if previousColor != "🟩":
                instruction += f"{currentCount}x{previousColor} "
                currentCount = 0
            previousColor = color
        currentCount += 1
    instruction += f"{currentCount}x{previousColor}"
    print(f"Row {number}: [{'Down Left' if downleft else 'Up Right'}] {len(diagonal)} Squares\n{instruction}\n")
    downleft = not downleft
    number += 1

print(f"{blue} Blue\n{yellow} Yellow\n{white} White")