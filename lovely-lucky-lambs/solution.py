def solution(total_lambs):
    # Get number of henchman you can give a stingy distribution to
    num_henchmen_stingy_distribution   = calculate_stingy_distribution(total_lambs)
    # Get number of henchmen you can give a generous distribution to
    num_henchmen_generous_distribution = calculate_generous_distribution(total_lambs)   
    # Return the difference
    return (num_henchmen_stingy_distribution - num_henchmen_generous_distribution)

def calculate_stingy_distribution(total_lambs, lambs_so_far=0, first_sub_lambs=0, second_sub_lambs=0):
    # Traverse the stingy linked list
    lambs_handed_out_so_far  = lambs_so_far
    number_of_henchmen       = 0
    first_subordinate_lambs  = first_sub_lambs
    second_subordinate_lambs = second_sub_lambs
    lamb_amount_for_next_henchman = 1 if (first_subordinate_lambs + second_subordinate_lambs) == 0 \
                                    else first_subordinate_lambs + second_subordinate_lambs
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

def calculate_generous_distribution(total_lambs):
    # Traverse the generous linked list
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
        lamb_amount_for_next_henchman = lamb_amount_for_next_henchman * 2
    else:
        # Try to give the next henchman the sum of the 2 subordinates
        lamb_amount_for_next_henchman = first_subordinate_lambs + second_subordinate_lambs
        if lambs_handed_out_so_far + lamb_amount_for_next_henchman <= total_lambs:
            # Hand out a lamb
            number_of_henchmen += 1
            lambs_handed_out_so_far += lamb_amount_for_next_henchman
        else:
            temp_lambs_so_far = lambs_handed_out_so_far - first_subordinate_lambs
            temp_num_henchmen = number_of_henchmen - 1
            second_subordinate_lambs /= 2
            first_subordinate_lambs  /= 2
            temp_num_henchmen += calculate_stingy_distribution(total_lambs, temp_lambs_so_far, 
                                                   first_subordinate_lambs, second_subordinate_lambs)
            if number_of_henchmen < temp_num_henchmen:
                number_of_henchmen = temp_num_henchmen
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
    test_case(total_lambs, result, 2)

    total_lambs = 1
    result      = solution(total_lambs)
    test_case(total_lambs, result, 0)

    total_lambs = 383
    result      = solution(total_lambs)
    test_case(total_lambs, result, 3)

if __name__ == "__main__":
    main()