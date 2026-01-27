import sys


def get_text_specification(text: str) -> str:
    """Counting the sums of the text upper-case characters, lower-case
    characters, punctuation characters, digits and spaces `str`.

    :param text: str - a single string argument.
    :return: str - containing the specification.

    expected lines:
        '
            The text contains 'n' characters:
            'n' upper letters
            'n' lower letters
            'n' punctuation marks
            'n' spaces
            'n' digits
        '
    """

    upper = lower = digit = space = punct = chara = 0

    # punctuation marks list
    punctuation_marks = [
        '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+',
        ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@',
        '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~'
    ]

    for char in text:
        chara += 1
        if char.isupper():
            upper += 1
        elif char.islower():
            lower += 1
        elif char.isdigit():
            digit += 1
        elif char.isspace():
            space += 1
        elif char in punctuation_marks:
            punct += 1

    return (
        f"The text contains {chara} characters:\n" +
        f"{upper} upper letters\n" +
        f"{lower} lower letters\n" +
        f"{punct} punctuation marks\n" +
        f"{space} spaces\n" +
        f"{digit} digits\n"
    )


def main():
    """Handling the input argument and printing its specification.

    Checking if the number of arguments is not exactly one
    if not will raise an AssertionError.
    Print the result of get_text_specification().
    """

    if len(sys.argv) > 2:
        print(AssertionError("More than one argument is provided."))
    elif len(sys.argv) < 2:
        print(AssertionError("No provided string."))
    else:
        print(get_text_specification(str(sys.argv[1])))


if __name__ == "__main__":
    main()
