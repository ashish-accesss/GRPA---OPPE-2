'''Check if an even-length string has A or a in the second half
Given an even-length string s, check if the second half contains the character "a" or "A". Return True if it does, otherwise return False.

Example

s = "abcDef"
The second half is "Def", which does not contain "a" or "A", so the result is False.'''


def has_a_in_second_half(s: str) -> bool:
    '''
    Given an even-length string, check if the second half contains 
    the character "a" or "A".

    Arguments:
    s: str - an even-length string.

    Return: bool - True if "a" or "A" is found in the second half, else False.
    '''
    mid=len(s)//2
    second_half=s[mid:]
    return 'a' in second_half or 'A' in second_half
    

