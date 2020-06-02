def solution(l):
    triples = 0
    pairs = [0] * len(l)
    for i in range(len(l)):
        for j in range(i):
            if l[i] % l[j] == 0:
                pairs[i] += 1
    for i in range(len(l)):
        for j in range(i):
            if l[i] % l[j] == 0:
                triples += pairs[j]
    return triples

def test_case(l, expected_result):
    print "Test for", l,
    result = solution(l)
    if expected_result != result:
        print "FAILED, returned", result
    else:
        print "passed."

def main():
    test_case([1, 2, 3, 4, 5, 6], 3)
    test_case([1, 1, 1], 1)
    test_case([1, 1, 1, 1], 4)

if __name__ == "__main__":
    main()