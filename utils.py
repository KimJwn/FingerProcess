import os, random
import cv2 as cv
import matplotlib.pyplot as plt
from skimage.morphology import medial_axis
import numpy as np
import math
import scipy.ndimage

from os.path import join, isdir

def save(keyPath, file_name, cv_img, type):
    
    '''
    save method need to save before image preprocessing.
    It has five arguments and requirement all.
    
    keyPath is root path of original image.
    file_name is original image file name
    cv_img is whole signal of the image
    rate is for scale value
    
    '''
    if os.path.isdir(keyPath) != True:
        os.mkdir(keyPath)
    
    saved_name = os.path.join(keyPath,"{}{}.{}".format(file_name.split('.')[0], type, 'jpg'))
    # print(saved_name)
    cv.imwrite(saved_name, cv_img)
    
    
def get_random_pixel(w, h, n, k):
    # 중앙 n*n 픽셀을 제외한 행과 열 범위 구하기
    row_range = list(range(n//2, w-n//2))
    col_range = list(range(n//2, h-n//2))
    # 각 모서리 k개 픽셀을 제외한 행과 열 범위 구하기
    row_range = [i for i in row_range if i < k or i >= w-k]
    col_range = [j for j in col_range if j < k or j >= h-k]
    # 랜덤하게 하나의 픽셀 선택하기
    random_pixel = (random.choice(row_range), random.choice(col_range))
    return random_pixel
get_random_pixel(9, 12, 2, 3 )


def plot_images(*images, cmap, sz = 8): #cmap='gray'
    images = list(images)
    n = len(images)
    fig, ax = plt.subplots(ncols=n, sharey=True, figsize = (sz, sz))
    for i, img in enumerate(images):
        ax[i].imshow(img, cmap)
        ax[i].axis('off')
    plt.subplots_adjust(left=0.03, bottom=0.03, right=0.97, top=0.97)
    plt.show()
    
    
def thinning_func(img):
    skel, distance = medial_axis(img, return_distance=True)
    dist_on_skel = (distance * skel).astype(np.uint8)
    dist_on_skel[dist_on_skel != 0] = 255
    return dist_on_skel



def normalise(img,mean,std):
    normed = (img - mean(img))/(std(img))    
    return(normed)


def np_normalise(img,mean,std):
    normed = (img - np.mean(img))/(np.std(img))    
    return(normed)
