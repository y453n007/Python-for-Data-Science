import os


def bar_calc(curr, total) -> str:
    """Calculates the visual progress bar string based on terminal width.

    Args:
        - curr: (int): The current iteration count.
        - total: (int): The total number of iterations expected.

    Returns:
        str: A string containing the '█' blocks and trailing spaces
            sized to the current terminal window.
    """
    term_size = os.get_terminal_size().columns - 41
    time = int(curr * term_size // total)
    ret = f"{'█' * time}{' ' * (term_size - time)}"
    return ret


def ft_tqdm(lst: range) -> None:
    """A custom progress bar generator mimicking the tqdm library.


    :parms: lst (range) - The range or iterable to iterate over.
    :yields: item - The current item from the original iterable.
    """

    total = len(lst)
    for i, item in enumerate(lst, 1):
        percent = (i / total) * 100
        barf = bar_calc(i, total)
        print(f"\r{percent:3.0f}%|{barf}| {i}/{total}", end="\r")
        yield item
