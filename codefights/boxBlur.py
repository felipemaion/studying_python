# https://codefights.com/arcade/intro/level-5/5xPitc3yT3dqS7XkP
# Last night you partied a little too hard. Now there's a black and white photo of
#  you that's about to go viral! You can't let this ruin your reputation,
# so you want to apply the box blur algorithm to the photo to hide its content.
#
# The pixels in the input image are represented as integers. The algorithm distorts the
# input image in the following way: Every pixel x in the output image has a value equal to
# the average value of the pixel values from the 3 × 3 square that has its center at x,
# including x itself. All the pixels on the border of x are then removed.
#
# Return the blurred image as an integer, with the fractions rounded down.
#
# Example
#
# For
#
image = [[1, 1, 1],
         [1, 7, 1],
         [1, 1, 1]]
# the output should be boxBlur(image) = [[1]].
#
# To get the value of the middle pixel in the input 3 × 3 square:
# (1 + 1 + 1 + 1 + 7 + 1 + 1 + 1 + 1) = 15 / 9 = 1.66666 = 1.
# The border pixels are cropped from the final result.
#
# For
#
# image = [[7, 4, 0, 1],
#          [5, 6, 2, 2],
#          [6, 10, 7, 8],
#          [1, 4, 2, 0]]
# the output should be
#
# boxBlur(image) = [[5, 4],
#                   [4, 4]]
# There are four 3 × 3 squares in the input image, so there should be four integers in the blurred output.
#  To get the first value: (7 + 4 + 0 + 5 + 6 + 2 + 6 + 10 + 7) = 47 / 9 = 5.2222 = 5.
# The other three integers are obtained the same way, then the surrounding integers are cropped from the final result.

def boxBlur(image):
    # Get dimensions:
    rows, columms = len(image), len(image[0])
    # Create a new image same size, but all None:
    new_image = [[None for x in range(columms)] for y in range(rows)]
    # Scan the image
    for row in range(rows):
        for columm in range(columms):
            # and only change if there are neighbors surrounding:
            if row > 0 and columm > 0 and row < rows - 1 and columm < columms - 1:
                # Get the avg:
                new_image[row][columm] = get_average(row,columm,image)
            else: # Just let it None (I will set none anyway), could be pass here...
                new_image[row][columm] = None
    # Crop the unused part of the image!
    return crop_image(new_image)

def crop_image(image):
    new_img = []
    for row in image:
        # Remove the Nones
        clean = [x for x in row if x is not None]
        # If still has something inside, add it... to avoid empty lines.
        if len(clean):
            new_img.append(clean)
    return new_img

def get_average(row,columm,image):
    avg = 0
    for i in range(-1,2):
        for j in range(-1,2):
            avg += image[row+i][columm+j]
    avg /= 9
    return int(avg)



mat=  [[1, 2, 3, 4, 5],
        [1, 2, 3, 4, 5],
        [1, 2, 3, 4, 5],
        [1, 2, 3, 4, 5],
        [1, 2, 3, 4, 5]]

print(*boxBlur(image), sep="\n")