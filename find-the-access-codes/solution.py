def solution(l):
    lucky_triples_list = []
    for i in range(len(l)):
        rest_of_the_list = l[i+1:]
        if l[i] == 1:
            grow_lucky_list(rest_of_the_list, l[i], lucky_triples_list)
        else:
            divs_shortlist = divisible_short_list(l[i], rest_of_the_list)
            grow_lucky_list(divs_shortlist, l[i], lucky_triples_list)
    return len(lucky_triples_list)

def divisible_short_list(divisor, l):
    shortlist = []
    for i in l:
        if i % divisor == 0:
            shortlist.append(i)
    return shortlist

# Find divisible pairs and append lucky list
def grow_lucky_list(l, initial_divisor, lucky_triples_list):
    for i in range(len(l)):
        for lj in l[i+1:]:
            if lj % l[i] == 0:
                lucky_triplet = [initial_divisor, l[i], lj]
                if lucky_triplet not in lucky_triples_list:
                    lucky_triples_list.append(lucky_triplet)

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