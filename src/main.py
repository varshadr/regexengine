import sys
def match_pattern(input_line, pattern):
    if len(pattern) == 1:
        return pattern in input_line
    elif pattern == "\\d":
        return any(char.isdigit() for char in input_line)
    elif pattern == "\\w":
        return any(char.isdigit() or char.isalpha() for char in input_line)
    elif pattern[0] == "[" and pattern[-1] == "]":
        if pattern[1] == "^":
            char_group = pattern[2 : -1]
            for char in input_line:
                if char in char_group:
                    return False
                return True
            
        else:
            char_group = pattern[1 : -1]
            for char in input_line:
                if char in char_group:
                    return True
            return False
    else:
        raise RuntimeError(f"Unhandled pattern: {pattern}")


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