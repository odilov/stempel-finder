import cv2
import numpy as np
import math


def is_vertical(img_src, line):
    tolerance = 10
    coords = line[0]
    angle = math.atan2(coords[3] - coords[1], coords[2] - coords[0]) * 180.0 / math.pi
    edge = img_src.shape[0] * 0.66
    out_of_bounds = coords[0] < edge and coords[2] < edge
    return math.fabs(90 - math.fabs(angle)) <= tolerance and not out_of_bounds

def geraden_linien_finden( src ):
    polar = cv2.imread( src )

    sobel = cv2.Sobel(polar, cv2.CV_16S, 1, 0)
    kernel = cv2.getStructuringElement(shape=cv2.MORPH_RECT, ksize=(1, 5))
    img = cv2.convertScaleAbs(sobel)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    img = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
    img = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)


    lines = cv2.HoughLinesP(img, 1, math.pi / 180, 15, img.shape[0] / 5, 10)
    vertical = [line for line in lines if is_vertical(img, line)]
    correct_lines = len(vertical)

    return correct_lines

print( geraden_linien_finden( 'log_polar_kovertiert.bmp' ) )
print( geraden_linien_finden( 'log_polar_kovertiert_hls.jpeg' ) )

print( geraden_linien_finden( 'log_polar_kovertiert2.bmp' ) )
print( geraden_linien_finden( 'log_polar_kovertiert_hls2.jpeg' ) )