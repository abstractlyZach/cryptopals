import string
import operator

BASE64_CHARS = (
    "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    "abcdefghijklmnopqrstuvwxyz"
    "0123456789+/"
)


def hex_to_base64(hex_string: str) -> int:
    decimal_value = hex_to_dec(hex_string)
    return dec_to_base64(decimal_value)


def dec_to_hex(decimal: int) -> str:
    # remove the "0x" prefix of the string
    return hex(decimal)[2:]


def hex_to_dec(hex_string: str) -> int:
    hex_string = hex_string.lower()
    decimal_value = 0
    for index, char in enumerate(reversed(hex_string)):
        char_as_dec = string.hexdigits.index(char)
        decimal_value += char_as_dec * (16 ** index)
    return decimal_value


def dec_to_base64(decimal: int) -> str:
    base64_str = ""
    exponent = 0
    # get the largest exponent
    while 64 ** exponent <= decimal:
        exponent += 1

    remainder = decimal
    while exponent > 0:
        exponent -= 1
        current_term = remainder // (64 ** exponent)
        base64_str += BASE64_CHARS[current_term]
        remainder = remainder % (64 ** exponent)
    return base64_str


def fixed_xor(buffer1: str, buffer2: str):
    if len(buffer1) != len(buffer2):
        raise ValueError(
            "Buffers must be the same length. {len(buffer1)} != {len(buffer2)}"
        )
    decimal_xor = operator.xor(hex_to_dec(buffer1), hex_to_dec(buffer2))
    return dec_to_hex(decimal_xor)
