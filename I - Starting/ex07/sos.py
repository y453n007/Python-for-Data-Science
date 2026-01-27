import sys


def mosre_cipher(text) -> str:
    """Morse translatore function.


    :param text: str
    :return: str
    :rtype: str

    The function tanslates the text chars to morse code,
    using dicionary of morse alphanumeric
    """
    morse_dict = {
        'A': '.-',
        'B': '-...',
        'C': '-.-.',
        'D': '-..',
        'E': '.',
        'F': '..-.',
        'G': '--.',
        'H': '....',
        'I': '..',
        'J': '.---',
        'K': '-.-',
        'L': '.-..',
        'M': '--',
        'N': '-.',
        'O': '---',
        'P': '.--.',
        'Q': '--.-',
        'R': '.-.',
        'S': '...',
        'T': '-',
        'U': '..-',
        'V': '...-',
        'W': '.--',
        'X': '-..-',
        'Y': '-.--',
        'Z': '--..',
        ' ': '/',
        '1': '.----',
        '2': '..---',
        '3': '...--',
        '4': '....-',
        '5': '.....',
        '6': '-....',
        '7': '--...',
        '8': '---..',
        '9': '----.',
        '0': '-----'
    }

    ciphered = ""
    for letter in text.upper():
        if letter in morse_dict:
            ciphered += morse_dict[letter] + ' '
        else:
            print(AssertionError("AssertionError: the arguments are bad"))
            sys.exit()
    return ciphered.strip()


def main():
    if len(sys.argv) != 2:
        print(AssertionError("AssertionError: the arguments are bad"))
        sys.exit()
    print(mosre_cipher(sys.argv[1]))


if __name__ == "__main__":
    main()
