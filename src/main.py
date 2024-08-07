import sys

def match_pattern(input_line, pattern):
    if len(pattern) == 1:
        return pattern in input_line
    elif pattern == "\\d":
        return any(char.isdigit() for char in input_line)
    elif pattern == "\\w":
        return any(char.isdigit() or char.isalpha() for char in input_line)



def main():
    pattern = sys.argv[2]
    input_line = sys.stdin.read()
    if sys.argv[1] != "-E":
        print("Expected first argument to be '-E'")
        exit(1)
        
    if match_pattern(input_line, pattern):
        exit(0)
    else:
        exit(1)
        
if __name__ == "__main__":
    main()