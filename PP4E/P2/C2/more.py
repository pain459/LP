"""
Split and interactively page a string or file of text.
"""

def more(text, numlines=15):
    lines = text.splitlines()  # just like split('\n') but no '' at end
    while lines:
        chuck = lines[:numlines]
        lines = lines[numlines:]
        for line in chuck: print(line)
        if line and input('More?') not in ['y', 'Y']: break

if __name__ == '__main__':
    import sys
    more(open(sys.argv[1]).read(), 10)
