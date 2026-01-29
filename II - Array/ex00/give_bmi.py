def type_check(x) -> bool:
    """
    'type_check' checks the type of an item (x),
    and it returns 'True' if the item is 'float' or 'int' and 'False' if not

    :param x: any type to check
    :return: 'True' or 'False'
    :rtype: bool
    """
    return isinstance(x, int) or isinstance(x, float)


def give_bmi(height: list[int | float], weight: list[int | float]) -> \
      list[int | float]:
    """
    'give_bmi' calculates the 'Body Mass Index' of a given 'lists'
    of 'float' and 'int' types

    cases to check:
        - empty list
        - type other than 'int' or 'float'

    :param height: a list of a height measures
    :type height: list[int | float]
    :param weight: a list of a weight measures
    :type weight: list[int | float]
    :return: list of calulated 'mbi'
    :rtype: list[int | float]
    """
    if height and weight and len(height) is len(weight):
        type_ = [type_check(h) for h in height]
        type_ += [type_check(w) for w in weight]
        if False in type_:
            print(AssertionError("AssertionError: arguments not compatible"))
            exit(1)
        bmi = [w / h**2 for h, w in zip(height, weight)]
        return bmi
    else:
        print(AssertionError("AssertionError: arguments not compatible"))
        exit(1)


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    'apply_limit' checks the reality of a list of a calculated 'mbi' over
    an int; a 'limit', true if it is above the limiter and false if it is under

    :param bmi: list of calculated 'mbi' to check
    :type bmi: list[int | float]
    :param limit: limter to check with
    :type limit: int
    :return: list of result (true or false)
    :rtype: list[bool]
    """
    type_ = [type_check(b) for b in bmi]
    type_ += [isinstance(limit, int)]
    if not bmi or False in type_:
        print(AssertionError("AssertionError: arguments not compatible"))
        exit(1)
    cases = [b > limit for b in bmi]
    return cases
