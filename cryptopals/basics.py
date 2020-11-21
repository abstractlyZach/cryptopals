import string

BASE64_CHARS = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"


def convert_hex_to_base64(hex_string):
    pass


def convert_hex_to_dec(hex_string):
    hex_string = hex_string.lower()
    decimal_value = 0
    for index, char in enumerate(reversed(hex_string)):
        char_as_dec = string.hexdigits.index(char)
        decimal_value += char_as_dec * (16 ** index)
    return decimal_value


def dec_to_base64(decimal: int) -> str:
    pass
