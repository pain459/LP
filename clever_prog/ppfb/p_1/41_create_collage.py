from PIL import Image
import numpy as np


def collage_maker(image1_path, image2_path, name, target_size=(800, 600)):
    # Open the files first
    image1 = Image.open(image1_path)
    image2 = Image.open(image2_path)

    # resize the files to handle any different size images
    image1 = image1.resize(target_size)
    image2 = image2.resize(target_size)

    # Convert the images to same number of channels so stacking wont return error.
    image1 = image1.convert("RGB")
    image2 = image2.convert("RGB")

    # Convert to array and stack the images vertically.
    i1 = np.array(image1)
    i2 = np.array(image2)
    collage = np.vstack([i1, i2])

    # save4 the collage
    collage_image = Image.fromarray(collage)
    collage_image.save(name)


# To Run The Above Function
collage_maker("img1.png", "img2.png", "new.png")
