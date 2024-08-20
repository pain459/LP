import cv2
import numpy as np
import os
from glob import glob

def load_images_from_folder(folder):
    images = []
    for filename in sorted(glob(os.path.join(folder, '*.jpg'))):  # You can change the extension to match your images
        img = cv2.imread(filename)
        if img is not None:
            images.append(img)
    return images

def detectAndDescribe(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    descriptor = cv2.SIFT_create()
    keypoints, features = descriptor.detectAndCompute(gray, None)
    return keypoints, features

def matchKeypoints(featuresA, featuresB, ratio=0.75, reprojThresh=4.0):
    matcher = cv2.BFMatcher()
    rawMatches = matcher.knnMatch(featuresA, featuresB, 2)
    matches = []

    for m, n in rawMatches:
        if m.distance < n.distance * ratio:
            matches.append(m)

    if len(matches) > 4:
        ptsA = np.float32([keypointsA[m.queryIdx].pt for m in matches])
        ptsB = np.float32([keypointsB[m.trainIdx].pt for m in matches])

        H, status = cv2.findHomography(ptsA, ptsB, cv2.RANSAC, reprojThresh)
        return matches, H, status

    return None, None, None

def stitchImages(imageA, imageB, H):
    width = imageA.shape[1] + imageB.shape[1]
    height = max(imageA.shape[0], imageB.shape[0])
    
    result = cv2.warpPerspective(imageB, H, (width, height))
    result[0:imageA.shape[0], 0:imageA.shape[1]] = imageA
    
    return result

def multi_band_blend(img1, img2):
    mask = np.zeros(img1.shape, dtype=np.float32)
    mask[:, :img1.shape[1]//2] = 1
    
    blended = img1 * mask + img2 * (1 - mask)
    return blended.astype(np.uint8)

def stitch_images_from_folder(input_folder, output_folder, output_filename='stitched_output.jpg'):
    # Load images from the specified input folder
    images = load_images_from_folder(input_folder)
    
    if len(images) < 2:
        print("Need at least two images to stitch")
        return
    
    # Start with the first image
    stitched_image = images[0]

    for i in range(1, len(images)):
        keypointsA, featuresA = detectAndDescribe(stitched_image)
        keypointsB, featuresB = detectAndDescribe(images[i])

        matches, H, status = matchKeypoints(featuresA, featuresB)
        
        if H is not None:
            stitched_image = stitchImages(stitched_image, images[i], H)
        else:
            print(f"Error: Could not compute homography for image {i + 1}.")

    # Apply multi-band blending on the final image
    stitched_image = multi_band_blend(stitched_image, images[-1])

    # Ensure the output directory exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Save the final stitched image
    output_path = os.path.join(output_folder, output_filename)
    cv2.imwrite(output_path, stitched_image)
    print(f"Stitched image saved at {output_path}")

    # Optionally, display the final stitched image
    cv2.imshow("Advanced Stitched Image", stitched_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    input_folder = 'path/to/your/images/folder'  # Replace with your images folder path
    output_folder = 'path/to/output/folder'      # Replace with your output folder path
    
    stitch_images_from_folder(input_folder, output_folder)
