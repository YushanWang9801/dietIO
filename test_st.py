import numpy as np
from PIL import Image
import cv2

def canny_selfie(image):
    image_array = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    edges = cv2.Canny(image_array, 100, 200)
    return edges

def main():
    test_image = Image.open("./selfie_input.jpg")
    canny =  canny_selfie(test_image)
    cv2.imwrite('canny.png', canny)

if __name__ == "__main__":
    main()
