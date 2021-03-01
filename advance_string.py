s = 'hello world'
print(s.capitalize())
print(s.upper())
print(s.lower())
# strings are immutable. None of the above methods change the string in place, they only return modified copies of the original string.
print(s)

# To change a string requires reassignment:
s = s.upper()
print(s)
s = s.lower()
print(s)
# returns the number of occurrences, without overlap
print(s.count('o'))
#  returns the starting index position of the first occurence
print(s.find('o'))
print(s.center(20,'z'))
# expandtabs() method will expand tab notations \t into spaces
print('hello\thi'.expandtabs())

s = 'hello'
print(s.isalnum())
print(s.isalpha())
print(s.islower())
print(s.isspace())
print(s.istitle())
print(s.isupper())
print(s.endswith('o'))
print(s.split('e'))
print(s.partition('l'))