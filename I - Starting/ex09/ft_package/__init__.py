def count_in_list(lst: list, item: any) -> int:
    """This function checks the exist of an item in list,
    then returns the size of it.

    :params:
        - lst: list - the iterable to seach in
        - item: any - what to search for

    :return: int how many item in list"""

    in_list = [s for s in lst if s == item]
    size = len(in_list)
    return size
