import re

pattern = r'mul\((\d{1,3}),(\d{1,3})\)'
do_pattern = r'do\(\)'  # Matches do()
dont_pattern = r"don't\(\)" 
res = 0
mul_enabled = True



with open('input.txt') as file:
    while True:
        line = file.readline()
        
        if not line:
            break
        if re.search(do_pattern, line):
            mul_enabled = True
        elif re.search(dont_pattern, line):
            mul_enabled = False
        if mul_enabled:
            matches = re.findall(pattern, line)
            for num1, num2 in matches:
                res += int(num1) * int(num2)
    print(res)

     