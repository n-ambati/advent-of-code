def read_input(filename="input2.txt"):

    with open(filename, "r") as f:
        data = f.read()
    
    data = data.split("\n")
    data = [list(map(int, report.split(" "))) for report in data]
    return data


def is_safe(report):
    if report[0] < report[1]:
        report = [-1 * level for level in report]
    
    for i in range(1, len(report)):
        diff = report[i - 1] - report[i]
        if diff < 1 or diff > 3:
            return False
    
    return True


def puzzle1(data):
    no_of_safe_reports = 0

    for report in data:
        # if report[1] >= report[0]:
        #     report = [-1 * level for level in report]
        
        # for i in range(1, len(report)):
        #     diff = report[i - 1] - report[i]
        #     if diff < 1 or diff > 3:
        #         break
        # else:
        #     no_of_safe_reports += 1
        if is_safe(report):
            no_of_safe_reports += 1
    
    print(no_of_safe_reports)


def puzzle2(data):
    no_of_safe_reports = 0

    for report in data:
        if is_safe(report):
            no_of_safe_reports += 1
        else:
            for i in range(len(report)):
                if is_safe(report[:i] + report[i + 1:]):
                    no_of_safe_reports += 1
                    break
    
    print(no_of_safe_reports)



def main():
    data = read_input()
    puzzle1(data)
    puzzle2(data)


if __name__ == "__main__":
    main()