## Python trick to output something on a new line

The trick converts all output to strings then put them into a list and then join them into a string that is returned or printed on a new line
'''
print('\n'.join(map(str,list(output))))
'''

## defaultdict from the collections module

Automatically add a key to the dictionary for you if the key is not already inside the dictionary. Helps avoid keyErrors

## Strings to array

```
s = 'This is an example sentence'
s.split()
```

## Array or list to string

```
l = ['my', 'example', 'sentence']
' '.join(l)
```

## startswith()

This method check if a string start with a particular string

```
sentence = 'Hi I am Fodela'
sentence.startswith('Hi')
#returns True
```

### inline print / print on the same line

```python
s = ["I", "love", "python"]

for w in s:
# Python2
    print w, # I love python

# Python3
    print(w, end=" ")
    # I love python

# NB: end takes a string which serves as a separator
    print(w, end="-")
    # I-love-python
```
