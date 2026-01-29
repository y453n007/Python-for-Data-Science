def ft_filter(func, iterable):
    """
    [0, 2, 4]
    [1, 2, 3, 4]
    filter(function or None, iterable) --> filter object

    Return an iterator yielding those items of iterable for which function(item)
    is true. If function is None, return the items that are true.
    """

    for item in iterable:
        if func is None:
            if item:
                yield item
        else:
            if func(item):
                yield item
