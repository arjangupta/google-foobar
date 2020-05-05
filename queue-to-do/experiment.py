def solution(start, length):
    current_total  = 0
    current_length = length
    for i in range(length):
        row_total = summation_of_xors(start + i * length - 1) ^ summation_of_xors(start + (i + 1) * (length - 1))
        current_total ^= row_total
        print "row #, row total: ", i, row_total
        current_length -= 1
    return current_total

def summation_of_xors(n):
    remainder = n % 4
    if remainder == 0:
        return n
    elif remainder == 1:
        return 1
    elif remainder == 2:
        return n + 1
    elif remainder == 3:
        return 0

def main():
    # answer = solution(16, 75)
    answer = solution(53, 75)
    # answer = solution(53, 100)
    # answer = solution(10, 100)
    # answer = solution(0, 100)
    # answer = solution(0, 10)
    print "Answer is", answer 

if __name__ == "__main__":
    main()