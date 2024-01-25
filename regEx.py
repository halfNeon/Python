import re

# 1. '\': use to draw special meaning of character following it.
pattern_1 = re.compile(r'\d')  # Match any digit
result_1 = pattern_1.findall("I have 5 apples and 3 oranges.")
print("1. Match any digit:", result_1)

# 2. '[]' Returns a match for any lower-case character, alphabetically between a and n
pattern_2 = re.compile(r'[a-n]')
result_2 = pattern_2.findall("The quick brown fox jumps over the lazy dog.")
print("2. Match any lower-case character between a and n:", result_2)

# 3. '^' Starts with
pattern_3 = re.compile(r'^The')
result_3 = pattern_3.findall("The quick brown fox jumps over the lazy dog.")
print("3. Starts with 'The':", result_3)

# 4. '$' Ends with
pattern_4 = re.compile(r'dog.$')
result_4 = pattern_4.findall("The quick brown fox jumps over the lazy dog.")
print("4. Ends with 'dog.':", result_4)

# 5. '.' Any character (except newline character)
pattern_5 = re.compile(r'T..')
result_5 = pattern_5.findall("The quick brown fox jumps over the lazy dog.")
print("5. Any two characters after 'T':", result_5)

# 6. ‘|’ Check if the string contains either "fox" or "dog"
pattern_6 = re.compile(r'fox|dog')
result_6 = pattern_6.findall("The quick brown fox jumps over the lazy dog.")
print("6. Contains either 'fox' or 'dog':", result_6)

# 7. '?' Zero or one occurrences
pattern_7 = re.compile(r'colou?r')
result_7 = pattern_7.findall("The color of the car is red.")
print("7. Match 'color' or 'colour':", result_7)

# 8. '*' Zero or more occurrences
pattern_8 = re.compile(r'go*gle')
result_8 = pattern_8.findall("gggle gogle google")
print("8. Match 'ggle', 'gole', 'gogle', 'google':", result_8)

# 9. '+' One or more occurrences
pattern_9 = re.compile(r'go+gle')
result_9 = pattern_9.findall("gggle gogle google")
print("9. Match 'gogle', 'google':", result_9)

# 10. '{}' Exactly the specified number of occurrences
pattern_10 = re.compile(r'\d{3}')
result_10 = pattern_10.findall("The price is $123 and $456.")
print("10. Match exactly 3 digits:", result_10)

# 11. Enclose a group of regex
pattern_11 = re.compile(r'(quick|lazy) (brown|black) (fox|dog)')
result_11 = pattern_11.findall("The quick brown fox jumps over the lazy dog.")
print("11. Enclosed groups:", result_11)
