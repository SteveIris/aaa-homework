issue-1:

python -m doctest -v -o NORMALIZE_WHITESPACE morse.py > result

Trying:
    [encode(letter) for letter in list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')]
Expecting:
    ['.-',  '-...',  '-.-.', '-..', '.',  '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--', '-.', '---', '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..']
ok
Trying:
    encode('SOS')
Expecting:
    '... --- ...'
ok
Trying:
    encode('SMESHARIKI')
Expecting:
    '... -- . ... .... .- .-. .. -.- ..'
ok
Trying:
    encode('QWERTY')
Expecting:
    '--.- .-- . .-. - -.--'
ok
Trying:
    encode('smeshariki')
Expecting:
    Traceback (most recent call last):
    KeyError: 's'
ok
2 items had no tests:
    morse
    morse.decode
1 items passed all tests:
   5 tests in morse.encode
5 tests in 3 items.
5 passed and 0 failed.
Test passed.

issue-2:

python -m pytest test_morse.py > result

================================================= test session starts =================================================
platform win32 -- Python 3.11.0, pytest-7.2.0, pluggy-1.0.0
rootdir: C:\Users\Public\Documents\AAA\aaa-homework\homework
collected 29 items

test_morse.py .............................                                                                      [100%]

================================================= 29 passed in 0.06s ============================================

issue-3:

python -m unittest > result

Ran 4 tests in 0.001s

OK

issue-4:

python -m pytest test_one_hot_encoder_pytest.py > result

================================================== 4 passed in 0.03s ==================================================