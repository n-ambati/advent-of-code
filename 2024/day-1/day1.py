import re


def read_input(filename="input1.txt"):
    with open(filename, "r") as f:
        data = f.readlines()

    left, right = [], []
    pattern = r"(\d+)\s+(\d+)"
    for line in data:
        matched = re.search(pattern, line)
        if matched:
            left.append(int(matched.group(1)))
            right.append(int(matched.group(2)))

    left.sort()
    right.sort()
    return left, right


def search(arr, key):
    low, high = 0, len(arr)

    while low < high:
        mid = low + (high - low) // 2

        if arr[mid] == key:
            break
        elif arr[mid] > key:
            high = mid
        else:
            low = mid + 1
    else:
        return 0
    
    count = 1
    left = mid - 1
    while left >= 0 and arr[left] == key:
        count += 1
        left -= 1
    
    right = mid + 1
    while mid < len(arr) and arr[right] == key:
        count += 1
        right += 1
    
    return count


def puzzle1(left, right):
    idx = 0
    difference = 0
    while idx < len(right):
        difference += abs(right[idx] - left[idx])
        idx += 1

    print(difference)


def puzzle2(left, right):
    similarity_score = 0
    for elem in left:
        similarity_score += elem * search(right, elem)
    
    print(similarity_score)


def main():
    left, right = read_input()
    puzzle1(left, right)
    puzzle2(left, right)


if __name__ == "__main__":
    main()