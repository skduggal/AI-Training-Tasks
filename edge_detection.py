import cv2
import numpy as np
import os

def detect_edges(image_path, output_path):
    image = cv2.imread(image_path)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # Convert  to grayscale
    edges = cv2.Canny(gray_image, 100, 200)  
    cv2.imwrite(output_path, edges)

    return edges

input_image_path = '/Users/sidkduggal/Documents/Code/iKites Training/yellow-miniflora-rose-david-austin-roses.jpg'
output_image_path = os.path.join(os.path.dirname(input_image_path), 'edges_image.jpg')

original_image = cv2.imread(input_image_path)
edges_image = detect_edges(input_image_path, output_image_path)

cv2.imshow('Original Image', original_image)
cv2.imshow('Edges Image', edges_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
