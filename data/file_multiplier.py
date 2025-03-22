DESIGNATED_FILE_NUMBER = 1000

import random
import os

with open('main.c', 'r') as bug_file:
    bug_code = bug_file.read()

with open('main.cpp','r') as good_file:
    good_code = good_file.read()

for i in range(DESIGNATED_FILE_NUMBER):
    choice = random.randint(0,1)
    code_copied = None
    if choice == 1:
        code_copied = good_code
    else:
        code_copied = bug_code

    filename = "main_" + str(i) + ".c"
    filename = os.path.join(os.getcwd(), filename)
    with open(filename, 'w') as f:
        f.write(code_copied)