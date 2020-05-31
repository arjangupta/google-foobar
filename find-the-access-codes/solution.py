def solution(l):
    return 0

def test_case(l, expected_result):
    print "Test for", l,
    if expected_result != solution(l):
        print "FAILED."
    else:
        print "passed."

def main():
    test_case([1, 2, 3, 4, 5, 6], 3)
    test_case([1, 1, 1], 1)

if __name__ == "__main__":
    main()