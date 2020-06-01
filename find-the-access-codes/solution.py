def solution(l):
    lucky_triplets = []
    for i in range(len(l)):
        pairs = []
        first_sublist = l[:i]
        for j in range(len(first_sublist)):
            if l[i] % first_sublist[j] == 0:
                pair = [first_sublist[j], l[i]]
                pairs.append(pair)
        second_sublist = l[i+1:]
        for k in range(len(second_sublist)):
            if second_sublist[k] % l[i] == 0:
                for pair in pairs:
                    triplet = [pair[0], pair[1], second_sublist[k]] 
                    if triplet not in lucky_triplets:
                        lucky_triplets.append(triplet)
    return len(lucky_triplets)

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

if __name__ == "__main__":
    main()