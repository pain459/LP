import pywhatkit as kit
import cv2


kit.text_to_handwriting("Test string", "test1.png")

img = cv2.imread("test1.png")
# Check the image dimensions
if img is not None and img.shape[0] > 0 and img.shape[1] > 0:
    # Display the image using OpenCV
    cv2.imshow("Text to handwriting", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Invalid image dimensions.")