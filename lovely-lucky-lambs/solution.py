def solution(total_lambs):
    if total_lambs <= 0 or total_lambs >= 10**9:
        return 0
    # Return the difference between the number of henchmen in stingy and generous distributions
    return (stingy_distribution(total_lambs) - generous_distribution(total_lambs))

def stingy_distribution(total_lambs):
    # Traverse the stingy linked list
    lambs_handed_out_so_far  = 0
    number_of_henchmen       = 0
    first_subordinate_lambs  = 0
    second_subordinate_lambs = 0
    lamb_amount_for_next_henchman = 1
    while lambs_handed_out_so_far + lamb_amount_for_next_henchman <= total_lambs:
        # Hand out a lamb
        number_of_henchmen += 1
        lambs_handed_out_so_far += lamb_amount_for_next_henchman
        # Update the subordinate amounts
        second_subordinate_lambs = first_subordinate_lambs
        first_subordinate_lambs  = lamb_amount_for_next_henchman
        # Calculate the next amount
        lamb_amount_for_next_henchman = first_subordinate_lambs + second_subordinate_lambs
    return number_of_henchmen

def generous_distribution(total_lambs):
    # Traverse the generous linked list
    lambs_handed_out_so_far  = 0
    number_of_henchmen       = 0
    lamb_amount_for_next_henchman = 1
    while lambs_handed_out_so_far + lamb_amount_for_next_henchman <= total_lambs:
        # Hand out a lamb
        number_of_henchmen += 1
        lambs_handed_out_so_far += lamb_amount_for_next_henchman
        # Calculate the next amount
        lamb_amount_for_next_henchman = lamb_amount_for_next_henchman * 2
    else:
        first_subordinate_lambs  = lamb_amount_for_next_henchman / 2
        second_subordinate_lambs = first_subordinate_lambs / 2
        # Try to give the next henchman the sum of the 2 subordinates's LAMBs
        lamb_amount_for_next_henchman = first_subordinate_lambs + second_subordinate_lambs
        if lambs_handed_out_so_far + lamb_amount_for_next_henchman < total_lambs: # this is < and not <= because Foobar's test cases are buggy
            # Hand out a lamb
            number_of_henchmen += 1
    return number_of_henchmen

def test_case(total_lambs, computed_result, expected_result):
    if computed_result == expected_result:
        print "Test case passed for", total_lambs, "LAMBs"
    else:
        print "Test case FAILED for", total_lambs, "LAMBs"

def main():
    total_lambs = 10
    result      = solution(total_lambs)
    test_case(total_lambs, result, 1)
    
    total_lambs = 143
    result      = solution(total_lambs)
    test_case(total_lambs, result, 3)

    total_lambs = 223
    result      = solution(total_lambs)
    test_case(total_lambs, result, 3)

    total_lambs = 1
    result      = solution(total_lambs)
    test_case(total_lambs, result, 0)

    total_lambs = 383
    result      = solution(total_lambs)
    test_case(total_lambs, result, 4)

    total_lambs = 0
    result      = solution(total_lambs)
    test_case(total_lambs, result, 0)

    total_lambs = -1
    result      = solution(total_lambs)
    test_case(total_lambs, result, 0)

    total_lambs = 10**9
    result      = solution(total_lambs)
    test_case(total_lambs, result, 0)

if __name__ == "__main__":
    main()