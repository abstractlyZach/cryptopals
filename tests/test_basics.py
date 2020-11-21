import pytest

from cryptopals import basics


@pytest.mark.skip
def test_hex_to_base64():
    input_string = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
    expected = "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"
    assert basics.convert_hex_to_base64(input_string) == expected


hex_to_dec_tests = [
    ("a", 10),
    ("b", 11),
    ("c", 12),
    ("d", 13),
    ("e", 14),
    ("f", 15),
    ("10", 16),
    ("100", 256),
    ("0ff", 255),
]


@pytest.mark.parametrize("input_string,expected", hex_to_dec_tests)
def test_hex_to_decimal(input_string, expected):
    assert basics.convert_hex_to_dec(input_string) == expected


def test_hex_chars_have_64_mappings():
    assert len(basics.BASE64_CHARS) == 64


dec_to_base64_tests = [
    (10, "K"),
    (62, "+"),
    (100, "Bk"),
    (64, "BA"),
]


@pytest.mark.parametrize("input_int,expected", dec_to_base64_tests)
def test_dec_to_base64(input_int, expected):
    assert basics.dec_to_base64(input_int) == expected
