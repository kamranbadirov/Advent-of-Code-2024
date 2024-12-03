# Part 1

def check_report(record):
    for i in range(1, len(record)):
        diff = abs(record[i] - record[i - 1])
        if diff > 3 or diff < 1:
            return False
    increasing = all(record[i] < record[i - 1] for i in range(1, len(record)))
    decresing = all(record[i] > record[i - 1] for i in range(1, len(record)))

    return increasing or decresing
# Part 2

def is_safe_with_dampener(report):
    for i in range(len(report)):
        modified = report[:i] + report[i + 1:]
        if check_report(modified):
            return True
    return False


with open('input.txt') as file:
    res = []
    while True:
        line = file.readline()
        if not line:
            break
        cur_report = [int(x) for x in line.split(' ')]
        if is_safe_with_dampener(cur_report):
            res.append(1)
    print(sum(res))
        



