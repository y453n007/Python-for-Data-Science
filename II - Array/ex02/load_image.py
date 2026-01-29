from PIL import Image
import numpy as np


def ft_load(path: str) -> list:
    """
    'ft_load' loads an image, prints its format,
    and its pixels content in RGB format.

    :param path: the location o the image
    :type path: str
    :return: the pixels content in RGB format table
    :rtype: list
    """
    image = Image.open(path)
    print(f"The shape of image is: {np.shape(image)}")
    return np.array(image)
