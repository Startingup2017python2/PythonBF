"""

This is a code written in Python 3 by Mostafa Ahangarha
as the second homework for StartingUp2017 project.

"""
import re


code = ""   # container for BrainFuck code

cell = {}   # Cells as ASCII code container

pointer = 0 # Pointer to determine which cell is under operation

# Reading code from the code file
with open("./ahangarha-code.bf", "r") as codeFile:
    for l in codeFile:
        code = code + l

# removing all non-BF characters, leaving only +-><[].
code = re.sub('[^\+-\.\[\]<>]', '', code)


# incriment (+)
def inc():
    global cell, pointer
    
    if cell.get(pointer) is None:
        cell[pointer] = 0
    
    cell[pointer] = cell[pointer] + 1

# decriment (-)
def dec():
    global cell, pointer
    
    if cell.get(pointer) is None:
        cell[pointer] = 0
    cell[pointer] = cell[pointer] - 1

#shift right (>)
def shift_right():
    global pointer
    pointer = pointer + 1

#shift right (<)
def shift_left():
    global pointer
    pointer = pointer - 1

#output (.)
def output():
    global cell, pointer
    
    if cell.get(pointer) is None:
        cell[pointer] = 0
    
    print(chr(cell[pointer]))

# =================================
# Running the BF code

for c in code:
    if c=="+":
        inc()
    elif c =="-":
        dec()
    elif c ==">":
        shift_right()
    elif c =="<":
        shift_left()
    elif c ==".":
        output()
