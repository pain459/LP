import cv2
import numpy as np

# Load images
images = []
for i in range(1, 5):  # Assuming you have 4 images to stitch
    img = cv2.imread(f'image{i}.jpg')
    images.append(img)

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

# Apply multi-band blending
stitched_image = multi_band_blend(stitched_image, images[-1])

# Save and display the final stitched image
cv2.imwrite('advanced_stitched_output.jpg', stitched_image)
cv2.imshow("Advanced Stitched Image", stitched_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
