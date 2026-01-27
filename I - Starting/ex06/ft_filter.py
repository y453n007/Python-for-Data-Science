def ft_filter(func, iterable):
    """Filters elements from an iterable based on a function's logic.

    This function yielding items for which the provided function returns True.
    If the function is None, it yields items that are truthy.

    :params
        func: (callable or None) - A function that returns a boolean.
        iterable: (iterable) - A collection of items (list, range, etc.) 
            to be filtered.

    :yields:
        Any: The next item in the iterable that satisfies the condition.
    """

    for item in iterable:
        if func is None:
            if item:
                yield item
        else:
            if func(item):
                yield item
