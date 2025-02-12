# Problem Set 4A
# Name: Mikias Yohannes
# Collaborators: my demons telling me I can't do this
# Time Spent: x:xx

def get_permutations(sequence):
    '''
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
    '''
    if len(sequence) == 1:
        return [sequence]
    
    first_char = sequence[0]
    remaining_permutations = get_permutations(sequence[1:])
    result = []
    for perm in remaining_permutations:
        for i in range(len(perm)+1):
            result.append(perm[:i] + first_char + perm[i:])

    return result

if __name__ == '__main__':

    # print('Input:', "deg")
    # print('Expected Output:', ['deg', 'dge', 'edg', 'egd', 'gde', 'ged'])
    # print('Actual Output:', get_permutations("deg"))
    
    # print('Input:', "abc")
    # print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
    # print('Actual Output:', get_permutations("abc"))
    

    pass #delete this line and replace with your code here

