DESIGNATED_FILE_NUMBER = 500

import random
import os
import json

ERROR_TYPE = ['MEMORY_NOT_FREE', 'UNALLOCATED_POINTER', 'UNUSED_VARIABLE', 'NONE']

with open('main.c', 'r') as not_free_file:
    not_free_code = not_free_file.read()

with open('main.cpp','r') as good_file:
    good_code = good_file.read()

with open('main_only_p.c', 'r') as unalloc_file:
    unalloc_code = unalloc_file.read()

with open('main_init.cpp','r') as unused_file:
    unused_code = unused_file.read()


file_dictionary = []

for i in range(DESIGNATED_FILE_NUMBER):
    choice = random.randint(0,3)
    code_copied = None
    error = None
    if choice == 0:
        code_copied = good_code
        error = 'NONE'
    elif choice == 1:
        code_copied = not_free_code
        error = 'MEMORY_NOT_FREE' 
    elif choice == 2:
        code_copied = unalloc_code
        error = 'UNALLOCATED_POINTER'
    elif choice == 3:
        code_copied = unused_code
        error = 'UNUSED_VARIABLE'

    filename = "main_" + str(i) + ".c"
    filename = os.path.join(os.getcwd(), filename)
    with open(filename, 'w') as f:
        f.write(code_copied)
    
    file_dictionary.append({"file":filename, "error":error})

json_file_path = 'data.json'
with open(json_file_path, "w", encoding="utf-8") as json_file:
    json.dump(file_dictionary, json_file, indent=4)