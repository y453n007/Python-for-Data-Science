import sys
from ft_filter import ft_filter


def main():
    """The program that accepts two arguments:
        - string (S)
        - integer (N).
        This program outputs a list of words according to this condition;
        S that have a length greater than N.


        If the number of arguments is different from 2,
        or if the type of any argument is wrong,
        the program prints an AssertionError.


        After the reading of the argument and processing them,
        the progarm called the ft_filter to check the truthy elemwnts.
    """
    if len(sys.argv) != 3:
        print(AssertionError("AssertionError: the arguments are bad"))
        sys.exit()
    is_alpha = lambda s: s.isalpha()
    is_num = lambda x: x.isdigit()
    string = sys.argv[1].split()
    digit = sys.argv[2]
    num = ""
    for i in digit:
        if is_num(i):
            num += i
        else:
            print(AssertionError("AssertionError: the arguments are bad"))
            sys.exit()
    size = int(num)
    text = [hand for hand in string if is_alpha(hand)]
    if not text:
        print(AssertionError("AssertionError: the arguments are bad"))
        sys.exit()
    else:
        truthy = ft_filter(lambda item: len(item) > size, text)
        print(list(truthy))


if __name__ == "__main__":
    main()