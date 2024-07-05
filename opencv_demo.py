import cv2
import numpy as np

def change_yellow_to_red(image_path, output_path):
    image = cv2.imread(image_path)

    lower_yellow = np.array([0, 100, 100]) # bgr values for lower yellow
    upper_yellow = np.array([100, 255, 255]) # bgr values for upper yellow

    mask_yellow = cv2.inRange(image, lower_yellow, upper_yellow)

    red_bgr = np.array([0, 0, 255]) # Define the red color in BGR space

    image[mask_yellow > 0] = red_bgr  # changing yellow to red

    cv2.imwrite(output_path, image)

    return image

input_image_path = '/Users/sidkduggal/Documents/Code/iKites/yellow-miniflora-rose-david-austin-roses.jpg'
output_image_path = '/Users/sidkduggal/Documents/Code/iKites/modified_image.jpg'  
original_image = cv2.imread(input_image_path)

modified_image = change_yellow_to_red(input_image_path, output_image_path)

cv2.imshow('Original Image', original_image)
cv2.imshow('Modified Image', modified_image)

cv2.waitKey(0)
cv2.destroyAllWindows()