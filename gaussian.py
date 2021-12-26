from itertools import product

from cv2 import COLOR_BGR2GRAY, cvtColor, imread, imshow, waitKey
from numpy import dot, exp, mgrid, pi, ravel, square, uint8, zeros


def gen_gaussian_kernel(kernelSize, sigma):
    center = kernelSize // 2  # center = 3 // 2 = 1

    # Gaussian Mask
    x, y = mgrid[0 - center: kernelSize - center, 0 - center: kernelSize - center]
    # print(x)                            print(y)
    # [[-1 -1 -1]                        [[-1  0  1]
    #  [0  0  0]                          [-1  0  1]
    #  [1  1  1]]                         [-1  0  1]]

    # Gaussian Form
    GaussianForm = (1 / (2 * pi * square(sigma))) * exp(-(square(x) + square(y)) / (2 * square(sigma)))

    return GaussianForm


def gaussian_filter(gray_image, kernelSize, sigma):
    height, width = gray_image.shape[0], gray_image.shape[1]

    # dst image height and width
    dst_height = height - kernelSize + 1   # = 385 - 3 + 1 --> 383
    dst_width = width - kernelSize + 1  # = 285 - 3 + 1 --> 283

    # im2col, turn the k_size * k_size pixels into a row and np.vstack all rows
    image_array = zeros((dst_height * dst_width, kernelSize * kernelSize))
    row = 0

    for i, j in product(range(dst_height), range(dst_width)):  # product --> arr1 = [10, 12], arr2 = [8, 9], Output : [(10, 8), (10, 9), (12, 8), (12, 9)]
        window = ravel(gray_image[i: i + kernelSize, j: j + kernelSize])  # 2-D to flat 1-D
        image_array[row, :] = window
        row += 1

    # turn the kernel into shape(k*k, 1)
    gaussian_kernel = gen_gaussian_kernel(kernelSize, sigma)
    filter_array = ravel(gaussian_kernel)

    # reshape and get the dst image
    dst = dot(image_array, filter_array).reshape(dst_height, dst_width).astype(uint8)

    return dst


if __name__ == "__main__":
    # read original image
    img = imread('images/gaussian.jpg')
    # turn image in gray scale value
    gray = cvtColor(img, COLOR_BGR2GRAY)

    # get values with two different kernelSize size
    gaussian3x3 = gaussian_filter(gray, 3, sigma=1)
    gaussian5x5 = gaussian_filter(gray, 5, sigma=0.8)

    # show result images
    imshow("Original image", gray)
    imshow("gaussian filter with 3x3 kernelSize", gaussian3x3)
    imshow("gaussian filter with 5x5 kernelSize", gaussian5x5)
    waitKey()
