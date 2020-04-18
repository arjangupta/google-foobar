def solution(total_lambs):
    return 0

def test_case(total_lambs, computed_result, expected_result):
    if computed_result == expected_result:
        print "Test case passed for", total_lambs, "LAMBs"
    else:
        print "Test case failed for", total_lambs, "LAMBs"


def main():
    total_lambs = 10
    result      = solution(total_lambs)
    test_case(total_lambs, result, 1)
    
    total_lambs = 143
    result      = solution(total_lambs)
    test_case(total_lambs, result, 3)

    total_lambs = 223
    result      = solution(total_lambs)
    test_case(total_lambs, result, 2)

if __name__ == "__main__":
    main()