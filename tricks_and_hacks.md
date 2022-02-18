## Python trick to output something on a new line

The trick converts all output to strings then put them into a list and then join them into a string that is returned or printed on a new line
'''
print('\n'.join(map(str,list(output))))
'''

## defaultdict from the collecitons module

Automatically add a key to the dictionary for you if the key is not already inside the dictionary. Helps avoid keyErrors
