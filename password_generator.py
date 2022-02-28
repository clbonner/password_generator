from random import randrange
import sys

if len(sys.argv) != 2:
    print("Usage: password_generator {password length}")
    exit()

PASSWORD_SIZE = int(sys.argv[1])

CHARS = [ "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
          "abcdefghijklmnopqrstuvwxyz",
          "0123456789",
          "-*&^%$!@#()"
        ]

VALID = False
VALID_CHECK = [0,0,0,0]

while not VALID:
    password = ""
    
    for i in range(PASSWORD_SIZE):
        char_list = randrange(0, len(CHARS))
        list_length = len(CHARS[char_list])
        char = randrange(0, list_length)
        password += CHARS[char_list][char]
        VALID_CHECK[char_list] = 1

        # VALID becomes true when each charater set has been used at least once
        if VALID_CHECK == [1,1,1,1]: VALID = True
    
print(password)
