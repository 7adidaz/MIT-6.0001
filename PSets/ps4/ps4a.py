# Problem Set 4A
# Name: abdallah
# Collaborators: didn't solve this on my own i got help from some guy on youtube
# Time Spent: x:xx
def get_permutations(sequence):
    """
    
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    """
    if len(sequence) ==1:
        return [sequence]
    
    
    
    
    permutations = get_permutations(sequence[1:])
    star_char = sequence[0]
    result = []
    
    for perm in permutations:
        for i in range(len(perm)+1):
            result.append(perm[:i]+ star_char+ perm[i:])
            
    return result
        
        


if __name__ == '__main__':
#    #EXAMPLE
    example_input = 'abc'
    print('Input:', example_input)
    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
    print('Actual Output:  ', get_permutations(example_input))
    
#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)

    #print(get_permutations("xyz"))

