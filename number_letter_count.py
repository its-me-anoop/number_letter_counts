units = [
    "",
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
    "ten",
]
teens = [
    "",
    "eleven",
    "twelve",
    "thirteen",
    "fourteen",
    "fifteen",
    "sixteen",
    "seventeen",
    "eighteen",
    "nineteen",
]
tens = [
    "",
    "ten",
    "twenty",
    "thirty",
    "forty",
    "fifty",
    "sixty",
    "seventy",
    "eighty",
    "ninety",
]


def count_letters_in_units(n):
    """
    Return the total number of letters used in writing numbers from 1 to 9 in English.

    Parameters:
    n (int): a number from 1 to 9

    Returns:
    int: the number of letters used to write 'n' in English
    """
    return len(units[n])


def count_letters_in_teens(n):
    """
    Return the total number of letters used in writing numbers from 11 to 19 in English.

    Parameters:
    n (int): a number from 11 to 19

    Returns:
    int: the number of letters used to write 'n' in English
    """
    return len(teens[n])


def count_letters_in_tens(n):
    """
    Return the total number of letters used in writing numbers from 20 to 99 in English.

    Parameters:
    n (int): a number from 20 to 99

    Returns:
    int: the number of letters used to write 'n' in English
    """
    return len(tens[n // 10]) + len(units[n % 10])


def count_letters_in_hundreds(n):
    """
    Return the total number of letters used in writing numbers from 100 to 999 in English.

    Parameters:
    n (int): a number from 100 to 999

    Returns:
    int: the number of letters used to write 'n' in English
    """
    count = len(units[n // 100]) + len("hundred")
    remainder = n % 100
    if remainder != 0:
        count += len("and")
        if 10 < remainder < 20:
            count += count_letters_in_teens(remainder - 10)
        else:
            count += count_letters_in_tens(remainder)
    return count


def count_letters_in_thousands(n):
    """
    Return the total number of letters used in writing numbers from 1000 to 9999 in English.

    Parameters:
    n (int): a number from 1000 to 9999

    Returns:
    int: the number of letters used to write 'n' in English
    """
    return len(units[n // 1000]) + len("thousand")


total_letters = 0
for i in range(1, 1001):
    if i < 10:
        total_letters += count_letters_in_units(i)
    elif i < 20:
        total_letters += count_letters_in_teens(i - 10)
    elif i < 100:
        total_letters += count_letters_in_tens(i)
    elif i < 1000:
        total_letters += count_letters_in_hundreds(i)
    else:
        total_letters += count_letters_in_thousands(i)

print(total_letters)
