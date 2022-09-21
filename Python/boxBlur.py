#!/usr/bin/env python
# -*- coding: utf-8 -*-

def surrounding_frame_sum(pixel_coords, image) -> int:
    pixels_value_sum = 0
    for row in range(pixel_coords[0] - 1, pixel_coords[0] + 2):
        for col in range(pixel_coords[1] - 1, pixel_coords[1] + 2):
            pixels_value_sum += image[row][col]
    return pixels_value_sum


def solution(image):
    blurred_image = []
    last_row = len(image) - 1
    last_col = len(image[0]) - 1
    for row in range(1, last_row):
        blurred_row = []
        for col in range(1, last_col):
            current_pixel_coords = (row, col)
            average = surrounding_frame_sum(current_pixel_coords, image) // 9
            blurred_row.append(average)
        blurred_image.append(blurred_row)
    return blurred_image


def main():
    image = [[1,2,3],
             [4,5,6],
             [7,8,9]]
    print(solution(image))

if __name__ == "__main__":
    main()

