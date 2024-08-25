"""
Image processing logics are stored here

"""
import cv2
import os

# Get path for each logic to reuse
cwd_path = os.getcwd()  # returns entrypoint path
rel_img_path = r"res\target_img\target_img.JPG"
full_img_path = os.path.join(cwd_path, rel_img_path)


def DynamicThresholdLogic(input_img,
                          MeanImgKernelSize:list = [401, 401], DynamicThresholdConstant:int = 1,
                          DynamicThresholdOffset:int = 0, IsDark = True,  ErosionKernelSize = [20,20],
                          OpeningKernelSize = [2,2],):

    # img = cv2.imread(full_img_path, cv2.IMREAD_GRAYSCALE)

    img = input_img

    # cv2.imshow('After Reading', img)
    # cv2.waitKey(0)

    # Mean image & Dynamic Thresholding
    img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY,
                                MeanImgKernelSize[0], DynamicThresholdOffset)
    if (IsDark):
        img = cv2.bitwise_not(img)

    # img = cv2.add(img, DynamicThresholdOffset)
    # img = img + DynamicThresholdOffset
    # img[img<0] = 0
    # img[img>255] = 255


    # cv2.imshow('After Dynamic Threshold', img)
    # cv2.waitKey(0)

    # Erosion
    kernel_shape = cv2.MORPH_RECT
    erode_kernel = cv2.getStructuringElement(kernel_shape, (ErosionKernelSize[0], ErosionKernelSize[1]))
    img = cv2.erode(img, erode_kernel)

    # cv2.imshow('After Erosion', img)
    # cv2.waitKey(0)


    # Opening
    opening_kernel = cv2.getStructuringElement(kernel_shape, (OpeningKernelSize[0], OpeningKernelSize[1]))
    img = cv2.morphologyEx(img, cv2.MORPH_OPEN, opening_kernel)

    # cv2.imshow('After Opening', img)
    # cv2.waitKey(0)
    return img
    # Connection
