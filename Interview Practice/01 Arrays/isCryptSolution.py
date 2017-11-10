"""
Codefights: Interview Prep - isCryptSolution.py
Written by cmdellinger
    
This function checks a possible solution to a cryptarithm. Given a solution as a list of character pairs (ex. ['A', '1']), the solution is valid of word_1 + word_2 == word_3 once decoded.

See .md file for more information about cryptarithm and problem constraints.
"""

def isCryptSolution(crypt, solution):
    ''' checks that list of pairs is a solution for 3 word cryptarithm;
        see problem for more details '''
    # change list of pairs to dictionary
    dictionary = dict(solution)
    # helper functions for map
    def str_decode(string = ''): #-> string
        ''' changes values in string according to key,value pair '''
        return ''.join([dictionary[letter] for letter in string])
    def lead_zeros(string = ''): #-> boolean
        ''' checks if a string of numbers has no lead zero '''
        return len(string) == len(str(int(string)))
    # decode crypt values
    decoded = map(str_decode, crypt)
    # check that no leading zeros and word_1+word_2==word_3
    return all(map(lead_zeros, decoded)) and int(decoded[0]) + int(decoded[1]) == int(decoded[2])

if __name__ == '__main__':
    print(__doc__)
