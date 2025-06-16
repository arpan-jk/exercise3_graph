
import random

# Conditions
is_even = lambda x: x is not None and x % 2 == 0
is_odd = lambda x: x is not None and x % 2 == 1
move_direct = lambda x: True

# Process names
ADD, MULT, DIV, START, END = "ADD", "MULT", "DIV", "START", "END"

MAX_ATTEMPT = 3

def get_random_number(start: int = 1, end: int = 1000) -> int:
    return random.randint(start, end)

