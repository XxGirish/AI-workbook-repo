from approvedimports import *

def exhaustive_search_4tumblers(puzzle: CombinationProblem) -> list:
    """simple brute-force search method that tries every combination until
    it finds the answer to a 4-digit combination lock puzzle.
    """

    # check that the lock has the expected number of digits
    assert puzzle.numdecisions == 4, "this code only works for 4 digits"

    # create an empty candidate solution
    my_attempt = CandidateSolution()

    # ====> insert your code below here
    for num1 in puzzle.value_set:
        for num2 in puzzle.value_set:
            for num3 in puzzle.value_set:
                for num4 in puzzle.value_set:
                    my_attempt.variable_values=[num1,num2,num3,num4]

                    try:
                        result=puzzle.evaluate(my_attempt.variable_values)
                    except Exception:
                        continue

                    if result==1:
                        return [num1,num2,num3,num4]


    # <==== insert your code above here

    # should never get here
    return [-1, -1, -1, -1]

def get_names(namearray: np.ndarray) -> list:

    family_names = []
    # ====> insert your code below here
    last_name=namearray[:,-6:]
    for i in last_name:

        family_names.append(''.join(i))



    # <==== insert your code above here
    return family_names

def check_sudoku_array(attempt: np.ndarray) -> int:
    tests_passed = 0
    slices = []  # this will be a list of numpy arrays

    # ====> insert your code below here
    assert attempt.shape == (9,9)

    for i in range(9):
        slices.append(attempt[i,:])

    for i in range(9):
        slices.append(attempt[:,i])

    for i in range(3):
        for j in range(3):
            subgrid = attempt[3*i:3*i+3, 3*j:3*j+3].flatten()  
            slices.append(subgrid)


    # use assertions to check that the array has 2 dimensions each of size 9


    ## Remember all the examples of indexing above
    ## and use the append() method to add something to a list

    for slice in slices:  # easiest way to iterate over list
        pass
        if len(np.unique(slice))==9:
                tests_passed=tests_passed +1
        # print(slice) - useful for debugging?

        # get number of unique values in slice

        # increment value of tests_passed as appropriate

    # <==== insert your code above here
    # return count of tests passed
    return tests_passed
