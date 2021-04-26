""" Conduct Hexgrid Walk ACSL 2017-2018 All-Star Challenge.
    
    moves: 1 is up.         4 is down.     Rows go from 1 to infinity.
           2 is up-right.   6 is up-left.  Cols go from 1 to MAX_COLS.
           3 is down-right. 5 is down-left.

    Rows are incremented/decremented when moving from an odd column to an even one,
    when moving upward (2 and 6) unless we're at Row 1.

    Rows are incremented/decremented when moving from an even column to an odd one
    when moving downward (3 and 5) unless we're at Row 1.

    Rows can't be incremented/decremented when attempting to move right (2 and 3)
    at the MAX_COLS column (there's nowhere to go).  Similarly, rows can't be
    incremented/decremented when attempting to move left (5 and 6) from Column 1.

    Columns are incremented/decremented as expected unless we're at column 1 or MAX_COLS
    (there's nowhere to go so we skip the operation).  Cells on the bottom row in even 
    columns 'hang down' so down-right and down-left are also not defined.

"""
import string
import re
from collections import namedtuple
import logging

LOG_FILE = r"hex_log.txt"
logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

MAX_COLS = 26
MOVES = 10
FIRST_ROW = 1

INPUT_REGEX = r"^([A-Z])([\d]+) ([0-9]+)"

def parse_input_line(inp: str) -> namedtuple:
    "Parse an input line  B2 123 -> namedtuple(col=B, row=2, moves=123)"
    input_tuple = namedtuple("Inp_line", "col row moves")
    logger.debug(f"input tuple: {input_tuple}")
    col, row, moves = re.match(INPUT_REGEX, inp).groups()
    return input_tuple(col, row, moves)


def fetch_chr_to_ord_dicts() -> tuple:
    """Returns a tuple of dicts mapping UC characters to their code points.
       chr_to_col is of the form {'A': 65, ...}
       col_to_chr is of the form {65: 'A', ...}
    """
    
    chr_to_col = {r: ord(r) - 64 for r in string.ascii_uppercase}
    col_to_chr = {val: key for key, val in chr_to_col.items()}
    return chr_to_col, col_to_chr

# Some logical functions to make more readable code    
def is_first_row(row):
    if row == FIRST_ROW:
        return True
def is_first_col(col):
    if col == 1:
        return True
def is_last_col(col):
    if col == MAX_COLS:
        return True
def is_even_col(col):
    if not col % 2:
        return True
def ask_incr_col(move):
    if move in (2, 3):
        return True
def ask_decr_col(move):
    if move in (5, 6):
        return True
def ask_incr_row(move):
    if move in (1, 2, 6):
        return True
def ask_decr_row(move):
    if move in (3, 4, 5):
        return True

def process_data(input_tuple: namedtuple, chr_to_col: dict, col_to_chr: dict) -> str:
    """Process input tuple, return final location.


    """
    row = int(input_tuple.row)
    icol = chr_to_col[input_tuple.col]
    for move in input_tuple.moves:
        move = int(move)
        if is_first_col(icol) and ask_decr_col(move):   # Can't go left from the first col 
            continue

        if is_last_col(icol) and ask_incr_col(move):  # We can't go right from the last column.
            continue
        
        if is_first_row(row):   # In the bottom row ...
            if is_even_col(icol) and ask_decr_row(move): #... we can's go down from even cols ...
                continue
            if move == 4:  # ... and can never go straight down.
                continue

        # Impossible moves now screened out so we don't need to check further.

        # A move upward or down is always honored ...
        if move == 1:
            row += 1
            continue

        if move == 4:
            row -= 1
            continue

        # Row decrement requests are honored only for even columns. 
        if ask_decr_row(move) and is_even_col(icol):
            row -= 1
        
        # Row increment requests are honored only for odd columns.
        if ask_incr_row(move) and not is_even_col(icol):
            row += 1

        # All requests to increment or decrement the column are honored.
        if ask_decr_col(move):
            icol -= 1
        if ask_incr_col(move):
            icol += 1
    position = f"{col_to_chr[icol]}{row}"
    logger.debug(f"position: {position}")
    return position


def main(input_path: str, results_path: str) -> None:
    " Parse input file, create output file"
    
    chr_to_col, col_to_chr = fetch_chr_to_ord_dicts()
    results = [0 for x in range(MOVES)]
    results_ix = 0

    with open(input_path, "r") as fh:
        contents = fh.readlines()
        for line in contents:
            logger.debug(f"original: {line.strip()}")
            data_tuple = parse_input_line(line.strip())
            logger.debug(f"input {data_tuple}")
            result = process_data(data_tuple, chr_to_col, col_to_chr)
            logger.debug(f"final result: {result}")
            results[results_ix] = result
            results_ix += 1

    with open(results_path, "w") as fh:
        for index, res in enumerate(results, 1):
            show_index_as = f"{index}."
            outpt = f"{show_index_as:<4}{res}\n"
            fh.write(outpt)


if __name__ == '__main__':
    main("test_input.txt", "actual_test_output.txt")