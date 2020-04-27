# Returns the array of parents
# h is the height of the tree
# q is the list of elements in tree for which 
# parents are to be found
def solution(h, q):
    return [find_parent(h, i) for i in q]

# Returns a parent for a given node of the tree
def find_parent(height, element):
    # Return -1 if no parent exists or element doesn't
    # belong to the tree
    absolute_parent = (2**height - 1)
    if element >= absolute_parent:
        return -1
    
    # Rules of the binary tree:
    # 1. It is a perfect binary tree
    # 2. The post order traversal list is an ascending order
    #    integer list from 1 to (2**h - 1)
    whole_tree       = range(1, absolute_parent + 1)
    current_sublist  = whole_tree
    current_parent   = -1
    current_height   = height
    found_parent     = 0
    left_sublist     = []
    right_sublist    = []
    # Begin the sublisting algorithm
    while found_parent == 0:
        current_parent  = current_sublist[-1]
        current_height -= 1
        left_sublist    = current_sublist[ : (2**current_height - 1) ]
        right_sublist   = current_sublist[ (2**current_height - 1) : -1 ]
        if element == left_sublist[-1] or element == right_sublist[-1]:
            found_parent = current_parent
        elif element in left_sublist:
            current_sublist = left_sublist
        else:
            current_sublist = right_sublist
    return found_parent

def test_case(h, q, p):
    print "Test case for", q,
    if (p != solution(h, q)):
        print "FAILED."
    else:
        print "passed." 

def main():
    # Run test cases
    test_case(3, [7, 3, 5, 1], [-1, 7, 6, 3])
    test_case(5, [19, 14, 28], [21, 15, 29])
    test_case(4, [14, 4, 8, 20, 12], [15, 6, 10, -1, 13])

if __name__ == "__main__":
    main()