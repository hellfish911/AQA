"""This module processes data and downloads photo."""
import os

import requests

url = 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos'

para = {
    'sol': 1000,
    'camera': 'fhaz',
    'api_key': 'DEMO_KEY',
}

output_folder = 'mars_photos'
os.makedirs(output_folder, exist_ok=True)

try:
    response = requests.get(url, params=para, timeout=10)
    response.raise_for_status()
    data_received = response.json()
    photos = data_received.get('photos', [])

    if not photos:
        print('Photo is not found.')
    else:
        for elem, photo in enumerate(photos[:2], start=1):
            img_url = photo['img_src']
            img_data = requests.get(img_url, params=para, timeout=10).content
            filename = os.path.join(output_folder, f'mars_photo{elem}.jpg')
            with open(filename, 'wb') as img_file:
                img_file.write(img_data)

            print(f'Photo saved: {filename}')

except requests.exceptions.RequestException as except_req:
    print(f'Exception occurred: {except_req}')
