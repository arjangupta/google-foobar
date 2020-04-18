def solution(total_lambs):
    print ""
    print "Distributing", total_lambs, "LAMBs"
    # Get number of henchman you can give a stingy distribution to
    num_henchman_stingy = calculate_stingy_distribution(total_lambs)
    
    return 0


def calculate_stingy_distribution(total_lambs):
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

    print "STINGY: A total of", lambs_handed_out_so_far, "LAMBs were handed out among", number_of_henchmen, "henchmen"

    return number_of_henchmen

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