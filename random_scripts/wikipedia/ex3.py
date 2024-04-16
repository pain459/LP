import wikipedia
import requests


def download_images(image_url):
    img_bytes = requests.get(image_url).content
    image_name = image_url.split('/')[-1]
    image_name = f'{image_name}'
    with open(image_name, 'wb') as img_file:
        img_file.write(img_bytes)
        print(f'{image_name} was downloaded...')


def main():
    image_urls = wikipedia.page('Visakapatnam').images
    image_url = image_urls[0] # forcefully downloading the first image
    download_images(image_url=image_url)
    print('Program completed.')


if __name__ == "__main__":
    main()