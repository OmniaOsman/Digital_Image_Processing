import numpy
from cv2 import COLOR_BGR2GRAY, cvtColor, imread, imshow, waitKey
from numpy import ravel, zeros_like


def median_filter(gray_img, mask):
    # print(gray_img.shape) --> (291, 218)

    # set borders of gray image
    border = int(mask / 2)  # if mask = 3, border wil be 1

    # copy gray image size
    median_img = zeros_like(gray_img)  # Return an array of zeros with the same shape and type as a given array.

    for i in range(border, gray_img.shape[0] - border):  # 1 : 291-1, 1 : 290 so range will be 1 : 290 --> 288 row
        for j in range(border, gray_img.shape[1] - border):  # 1 : 217 --> 215 column
            # get mask according to mask
            kernel = ravel(gray_img[i - border: i + border + 1, j - border: j + border + 1])  # ravel change a 2-dimensional to contiguous flattened array

            # print(gray_img[i - border: i + border + 1, j - border: j + border + 1])
            # [[131 148 155]
            #  [133 150 154]
            # [133 149 153]
            # print(kernel)
            # [131 148 155 133 150 154 133 149 153]

            # calculate mask median
            median = numpy.median(kernel + 1)

            # print(median)
            # 150

            median_img[i, j] = median

    return median_img


if __name__ == "__main__":
    img = imread('C:/Users/C.M/PycharmProjects/Img processing project/images/Salt_Pepper_Noise.png')
    # turn image in gray scale value
    gray = cvtColor(img, COLOR_BGR2GRAY)

    # get values with two different mask size
    median3x3 = median_filter(gray, 3)
    median5x5 = median_filter(gray, 5)

    # show result images
    imshow("median filter with 3x3 mask", median3x3)
    imshow("median filter with 5x5 mask", median5x5)
    waitKey(0)
