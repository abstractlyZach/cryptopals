import pytest

from cryptopals import basics


def test_hex_to_base64():
    input_string = (
        "49276d206b696c6c696e6720796f757220627261696e206c696b6520"
        "6120706f69736f6e6f7573206d757368726f6f6d"
    )
    expected = (
        "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2"
        "hyb29t"
    )
    assert basics.hex_to_base64(input_string) == expected


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
    assert basics.hex_to_dec(input_string) == expected


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


def test_fixed_xor():
    buffer1 = "1c0111001f010100061a024b53535009181c"
    buffer2 = "686974207468652062756c6c277320657965"
    expected = "746865206b696420646f6e277420706c6179"
    assert basics.fixed_xor(buffer1, buffer2) == expected


def test_fixed_xor_fails_on_unmatched_buffers():
    """We should throw an exception when the buffers do not have equal length"""
    with pytest.raises(ValueError):
        basics.fixed_xor(
            "a" * 15,
            "a" * 14,
        )

# reuse the tests but in reversed order


@pytest.mark.parametrize("expected,input_int", hex_to_dec_tests)
def test_dec_to_hex(expected, input_int):
    # strip leading zeroes from the test parameters
    assert basics.dec_to_hex(input_int) == expected.lstrip('0')
