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
    while True:
        line = file.readline()
        if not line:
            break
        line += '########################'  # Ensure no issues at the end of the line
        
        i = 0
        n = len(line)

        while i < n:
            # Check for mul() instruction
            if line[i:i+4] == 'mul(':
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
