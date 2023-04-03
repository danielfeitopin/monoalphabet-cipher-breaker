ALPHABETS: dict = {
    'EN': ('E', 'T', 'A', 'O', 'I', 'N', 'S', 'H', 'R', 'D', 'L', 'C', 'U', 'M',
           'W', 'F', 'G', 'Y', 'P', 'B', 'V', 'K', 'J', 'X', 'Q', 'Z'),
    'ES': ('E', 'T', 'A', 'O', 'I', 'N', 'S', 'H', 'R', 'D', 'L', 'C', 'U', 'M',
           'W', 'F', 'G', 'Y', 'P', 'B', 'V', 'K', 'J', 'X', 'Q', 'Z'),
}


def get_stats(string: str) -> dict:
    """Return statistics about the input string.

    Args:
        string (str): The input string.

    Returns:
        dict: A dictionary containing the following keys:
            - num_of_chars (int): The number of characters in the input string.
            - num_of_letters (int): The number of letters in the input string.
            - letters (str): A string containing all the letters found in the '\
                'input string.
            - frequencies (dict): A dictionary with the frequency of each '\
                'letter found in the input string.

    """

    def get_frequencies(string: str) -> dict[str, int]:
        frequencies: dict[str, int] = {}
        for c in string:
            frequencies[c] = frequencies.get(c, 0) + 1
        return frequencies

    def filter_frequencies(function,
                           frequencies: dict[str, int]) -> dict[str, int]:
        return dict(filter(lambda item: function(item[0]), frequencies.items()))

    def order_frequencies(frequencies: dict) -> dict:
        return {
            k: v for k, v in sorted(frequencies.items(),
                                    key=lambda item: item[1],
                                    reverse=True)
        }

    frequencies: dict[str, int] = order_frequencies(
        filter_frequencies(str.isalpha, get_frequencies(string.upper()))
    )

    return {
        'num_of_chars': len(string),
        'num_of_letters': sum(frequencies.values()),
        'letters': "".join(frequencies.keys()),
        'frequencies': frequencies
    }


def confirm(m: str, c: str, confirmed: dict[str, str]) -> None:
    """Adds a confirmed mapping to the dictionary.

    Args:
        m (str): The message character to be mapped.
        c (str): The cipher character to map to.
        confirmed (dict[str, str]): The confirmed mapping dictionary.
    """
    
    confirmed[m.upper()] = c.upper()


def disconfirm(m: str, confirmed: dict[str, str]) -> None:
    """Removes a confirmed mapping from the dictionary.

    Args:
        m (str): The message character to be removed.
        confirmed (dict[str, str]): The confirmed mapping dictionary.
    """

    confirmed.pop(m.upper(), None)


def estimate(alphabet: tuple, letters: str, confirmed: dict[str, str],
             estimated: dict[str, str]) -> dict[str, str]:
    """Estimates the mappings based on the letters frequency.

    Args:
        alphabet (tuple): The set of possible characters to map.
        letters (str): The set of letters in the cipher text.
        confirmed (dict[str, str]): The confirmed mappings dictionary.
        estimated (dict[str, str]): The estimated mappings dictionary.

    Returns:
        The estimated mappings dictionary.
    """

    estimated.clear()
    estimated.update(zip((c for c in alphabet if c not in confirmed),
                         (c for c in letters if c not in confirmed.values())))


def reverse_dict(d: dict) -> dict:
    """Returns a new dictionary with reversed key-value pairs.

    Args:
        d (dict): The dictionary to be reversed.

    Returns:
        The reversed dictionary.
    """

    return dict((v, k) for k, v in d.items())


def show_stats(stats: dict) -> None:
    print(''.join((
        "STATS:\n",
        f"- Number of characters: {stats['num_of_chars']}\n",
        f"- Number of letters: {stats['num_of_letters']}\n",
        f"- Letters ordered by frequency: {stats['letters']}\n",
        f"- Frequencies: {stats['frequencies']}\n",
    )))


def __green(string: str) -> str:
    return "\033[0;32m" + string + "\033[0m"


def __yellow(string: str) -> str:
    return "\033[1;33m" + string + "\033[0m"


def __red(string: str) -> str:
    return "\033[0;31m" + string + "\033[0m"


def show_substitution_table(alphabets: dict[str, str],
                            confirmed: dict[str, str],
                            estimated: dict[str, str]) -> None:

    def substitute(string: str, substitution: dict[str, str]) -> str:
        return ''.join(substitution.get(c, '·') for c in string)

    language: str = __green(alphabets['language'])
    letters: str = __red(alphabets['letters'])

    c_language: str = substitute(alphabets['language'], confirmed)
    c_language = __green(c_language)
    c_letters: str = substitute(alphabets['letters'], reverse_dict(confirmed))
    c_letters = __green(c_letters)

    e_language: str = substitute(alphabets['language'], estimated)
    e_language = __yellow(e_language)
    e_letters: str = substitute(alphabets['letters'], reverse_dict(estimated))
    e_letters = __yellow(e_letters)

    substitution: dict[str, str] = {}
    substitution.update(estimated)
    substitution.update(confirmed)
    s_language: str = substitute(alphabets['language'], substitution)
    s_letters: str = substitute(alphabets['letters'],
                                reverse_dict(substitution))

    print(''.join((
        "ALPHABETS (PLAIN->CIPHER | CIPHER->PLAIN):\n",
        f"Alphabet:     {language} | {letters}\n",
        f"Confirmed:    {c_language} | {c_letters}\n",
        f"Estimated:    {e_language} | {e_letters}\n",
        f"Substitution: {s_language} | {s_letters}\n",
    )))


def show_substitution_texts(text: str, confirmed: dict[str, str],
                            estimated: dict[str, str]) -> None:

    def substitute(text: str, confirmed: dict[str, str],
                   estimated: dict[str, str]) -> str:

        r_confirmed: dict[str, str] = reverse_dict(confirmed)
        r_estimated: dict[str, str] = reverse_dict(estimated)

        string: str = ''
        for c in text:
            string += __green(r_confirmed[c]) if c in r_confirmed \
                else __yellow(r_estimated[c]) if c in r_estimated \
                else __red(c)
        return string

    print(''.join((
        f"★ {__red('ORIGINAL')} ",
        f"★ {__green('CONFIRMED')} ",
        f"★ {__yellow('ESTIMATED')} ",
        '\n'*2,

        substitute(text, {}, {}) + '\n'*2,
        substitute(text, confirmed, {}) + '\n'*2,
        substitute(text, confirmed, estimated) + '\n'*2,
    )))


def main(cipher_text: str) -> None:

    # Stats
    stats: dict = get_stats(cipher_text)

    # Alphabets
    alphabet: tuple = ALPHABETS['EN']
    alphabets: dict[str, str] = {
        'language': ''.join(sorted(alphabet)),
        'letters': stats['letters'],
    }

    # Substitution dictionaries
    confirmed: dict[str, str] = {}
    estimated: dict[str, str] = {}
    estimate(alphabet, alphabets['letters'], confirmed, estimated)

    # Information
    def show_help() -> None:
        print(''.join((
            '--- Help Menu ---' + '\n',
            'Commands:' + '\n',
            'help: Show this help menu.' + '\n',
            'set a b: Includes \'a\' as the plain text key with value \'b\' '
            + 'in the confirmed dict.' + '\n',
            'unset a: Removes key \'a\' from confirmed dict.' + '\n',
            'exit: Quit the program.' + '\n',
        )))

    def show_info() -> None:
        show_stats(stats)
        show_substitution_table(alphabets, confirmed, estimated)
        show_substitution_texts(cipher_text, confirmed, estimated)

    # Menu
    show_info()
    while True:
        command: str = input("Enter command: ")
        command_list: list[str] = command.split()

        if command == "help":
            show_help()
        elif command == "exit":
            exit(0)
        elif len(command_list) == 3 \
                and command_list[0] == "set" \
                and len(command_list[1]) == 1 \
                and len(command_list[2]) == 1:
            confirm(command_list[1], command_list[2], confirmed)
            estimate(alphabet, alphabets['letters'], confirmed, estimated)
            show_info()
        elif len(command_list) == 2 and command_list[0] == "unset":
            disconfirm(command_list[1], confirmed)
            estimate(alphabet, alphabets['letters'], confirmed, estimated)
            show_info()
        else:
            print("Invalid command. Enter 'help' to show the help menu.")


if __name__ == '__main__':

    # File reading
    from sys import argv
    try:
        with open(argv[1], 'r') as f:
            cipher_text: str = f.read().upper()
    except:
        print('Error opening file to read.')
        exit(-1)

    try:
        main(cipher_text)
    except KeyboardInterrupt:
        exit(0)
