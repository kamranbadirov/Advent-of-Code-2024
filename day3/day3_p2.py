res = 0
mul_enabled = True

# Function to get the number from the string
def get_num(i):
    x = 0
    while i < len(line) and line[i].isdigit():
        x = x * 10 + int(line[i])
        i += 1
    if 1 <= x <= 999:
        return x, i
    return -1, i  # Return -1 if the number is invalid

with open('input.txt') as file:
    enable = True  # Initially, multiplications are enabled
    while True:
        line = file.readline()
        if not line:
            break
        line += '########################'  # Ensure no issues at the end of the line
        
        i = 0
        n = len(line)

        while i < n:
            # Check for do() instruction
            if line[i:i+4] == 'do()':
                enable = True
                i += 4  # Move past 'do()'

            # Check for don't() instruction
            elif line[i:i + 7] == "don't()":
                enable = False
                i += 7  # Move past "don't()"

            # Process mul() if enabled
            elif enable and line[i:i+4] == 'mul(':
                i += 4  # Move past 'mul('
                x, i = get_num(i)
                if x == -1:  # Invalid number, skip to next character
                    i += 1
                    continue
                if line[i] == ',':
                    i += 1  # Move past the comma
                y, i = get_num(i)
                if y == -1:  # Invalid number, skip to next character
                    i += 1
                    continue
                if line[i] == ')':
                    res += x * y  # Valid multiplication
                    i += 1  # Move past ')'
                else:
                    i += 1  # Skip invalid character if ')' is not found

            else:
                i += 1  # Continue to next character

print(res)
