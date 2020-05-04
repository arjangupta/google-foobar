def solution(start, length):
    partition_position  = length
    current_xor_result  = 0
    current_employee_id = start
    break_loops = False
    while (partition_position > 0) and (not break_loops):
        for employee_position in range(length):
            if employee_position < partition_position:
                current_xor_result ^= current_employee_id
            current_employee_id += 1
            if current_employee_id > 2*10**9:
                break_loops = True
                break
        if break_loops:
            break
        partition_position -= 1
    return current_xor_result

def test_case(start, length, expected_result):
    print "Test for ( " + str(start) + ", " + str(length) + " ) ",
    if expected_result != solution(start, length):
        print "FAILED."
    else:
        print "passed."

def main():
    # Run the test cases
    test_case(0, 3, 2)
    test_case(17, 4, 14)
    test_case(1, 1, 1)
    test_case((2*10**9), 2, (2*10**9))
    test_case((2*10**9), 10, (2*10**9))
    test_case((2*10**9)-1, 2, 2047)

if __name__ == "__main__":
    main()