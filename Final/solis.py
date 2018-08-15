'''
## Functions
-------------------------------------------------
'''
def clean_trim_year(value):
    value = str(value)
    result = value[6:]
    return result

def print_file_from_head(fname, nlines):
        from itertools import islice
        with open(fname) as f:
                for line in islice(f, nlines):
                        print("".join(line.rstrip()))