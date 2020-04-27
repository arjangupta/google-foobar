def solution(h, q):
    return []

def test_case(h, q, p):
    if (p != solution(h, q)):
        print "Test case for", q, "failed."

def main():
    # Run test cases
    test_case(3, [7, 3, 5, 1], [-1,7,6,3])
    test_case(5, [19, 14, 28], [21, 15, 29])
    test_case(4, [14, 4, 8, 20, 12], [15, 6, 10, -1, 13])

if __name__ == "__main__":
    main()