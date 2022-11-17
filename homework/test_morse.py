import pytest
from morse import decode


@pytest.mark.parametrize("test_input,expected", [('-.-. ..- -.-. ..- -- -... . .-.', 'CUCUMBER'),
                                                 ('... --- ...', 'SOS'),
                                                 ('.-. -.-- .- -. --. --- ... .-.. .. -. --.', 'RYANGOSLING')])
def test_decode(test_input, expected):
    assert decode(test_input) == expected


@pytest.mark.parametrize("test_input,expected", zip(['.-',  '-...', '-.-.', '-..', '.',  '..-.', '--.',
                                                     '....', '..', '.---', '-.-', '.-..', '--', '-.', '---',
                                                     '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--',
                                                     '-..-', '-.--', '--..'], list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')))
def test_letters(test_input, expected):
    assert decode(test_input) == expected
