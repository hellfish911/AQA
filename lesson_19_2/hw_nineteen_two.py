"""This module interacts with a server for processing images."""

import requests

BASE_URL = 'http://127.0.0.1:8080'


def upload_image(image_path):
    """
    Upload an image to the server.

    Args:
        image_path (str): The file path of the image to upload.

    Returns:
        str or None: The URL of the uploaded image if successful.
    """
    url = f'{BASE_URL}/upload'
    try:
        with open(image_path, 'rb') as image_file:
            files = {'image': image_file}
            response = requests.post(url, files=files, timeout=10)
            if response.status_code == 201:
                print('Image uploaded successfully.')
                return response.json()['image_url']
            else:
                print(f'Upload error: {response.status_code}')
                print(response.text)
                return None
    except FileNotFoundError:
        print(f'File not found: {image_path}')
        return None


def get_image_url(filename):
    """
    Retrieve the URL of an uploaded image from the server.

    Args:
        filename (str): The filename of the image on the server.

    Returns:
        str or None: The URL of the image if successful, otherwise None.
    """
    url = f'{BASE_URL}/image/{filename}'
    headers = {'Content-Type': 'text'}
    response = requests.get(url, headers=headers, timeout=10)
    if response.status_code == 200:
        print('Image URL retrieved successfully.')
        return response.json()['image_url']
    else:
        print(f'Error retrieving image URL: {response.status_code}')
        print(response.text)
        return None


def delete_image(filename):
    """
    Delete an image from the server.

    Args:
        filename (str): The filename of the image to delete on the server.

    Returns:
        dict or None: The server's response message if successful.
    """
    url = f'{BASE_URL}/delete/{filename}'
    response = requests.delete(url, timeout=10)
    if response.status_code == 200:
        print('Image deleted successfully.')
        return response.json()
    else:
        print(f'Error deleting image: {response.status_code}')
        print(response.text)
        return None


def main():
    """
    Demonstrate the usage of the module.

    It uploads an image, retrieves its URL, and then deletes it.
    """
    image_path = 'Python_logo.svg'

    # Upload the image
    uploaded_image_url = upload_image(image_path)
    if uploaded_image_url:
        print('Uploaded image URL:', uploaded_image_url)

        # Extract the filename from the uploaded image URL
        filename = uploaded_image_url.split('/')[-1]

        # Retrieve the image URL
        image_url = get_image_url(filename)
        if image_url:
            print('Image URL confirmed:', image_url)

        # Delete the image
        delete_response = delete_image(filename)
        if delete_response:
            print('Deletion result:', delete_response)


if __name__ == '__main__':
    main()
