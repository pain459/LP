import cv2
import numpy as np

# Load images
image1 = cv2.imread('image1.jpg')
image2 = cv2.imread('image2.jpg')

# Create a stitcher object
stitcher = cv2.Stitcher_create()

# Perform the stitching process
(status, stitched) = stitcher.stitch([image1, image2])

# Check if the stitching was successful
if status == cv2.Stitcher_OK:
    print("Stitching Successful")
    cv2.imshow("Stitched Image", stitched)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.imwrite('stitched_output.jpg', stitched)
    print("Stitched image saved.")
else:
    print("Stitching Failed: Error Code =", status)
