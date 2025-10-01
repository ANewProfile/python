def parse(input):
    reports = input.split('\n')[:-1]
    output = []
    for report in reports:
        cur_report = []
        for level in report.split():
            cur_report.append(int(level))

        output.append(cur_report)
    
    return output

def is_safe(report):
    increasing = True if report[0] < report[1] else False
    for i in range(1, len(report)):
        if abs(report[i] - report[i-1]) > 3 or \
           abs(report[i] - report[i-1]) < 1:
            return False
        
        if (report[i] < report[i-1] and increasing) or \
           (report[i] > report[i-1] and not increasing):
               return False

    return True

def main():
    with open('day2input.txt', 'r') as input:
        reports = parse(input.read())

    num_safe_reports = 0
    for report in reports:
        if is_safe(report):
            num_safe_reports += 1

    return num_safe_reports

if __name__ == '__main__':
    num_safe_reports = main()
    print(num_safe_reports)

