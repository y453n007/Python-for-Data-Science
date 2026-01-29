import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """
    'slice_me' takes as parameters a 2D array, prints its shape,
    and returns a truncated version of the array based on the provided
    start and end arguments (with slicing method)

    :param family: 2D array to be sliced
    :type family: list
    :param start: The index where the slice begins
    :type start: int
    :param end: The index where the slice ends
    :type end: int
    :return: new sliced list
    :rtype: list
    """
    arr = np.array(family)
    dim = arr.shape
    if dim[0] * dim[1] != arr.size or arr.dtype.type != np.float64:
        print(AssertionError("AssertionError: arrays are not equal"))
        exit(1)
    print(f"My shape is : {dim}")
    new = family[start:end]
    print(f"My new shape is : {np.shape(new)}")
    return new
