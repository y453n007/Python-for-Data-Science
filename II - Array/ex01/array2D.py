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
    type_ = [isinstance(i, list) for i in family]
    dimontion = [len(i) == len(family[0]) for i in family]
    if False in dimontion or False in type_:
        print(AssertionError("AssertionError: arrays are not equal"))
        exit(1)
    print(f"My shape is : ({len(family)}, {len(family[1])})")
    new = family[start:end]
    print(f"My new shape is : ({len(new)}, {len(new[0])})")
    return new
