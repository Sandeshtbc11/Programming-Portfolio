"""
Write and test three functions that each take two words (strings) as parameters and
return sorted lists (as defined above) representing respectively:
Letters that appear in at least one of the two words.
Letters that appear in both words.
Letters that appear in either word, but not in both.
Hint: These could all be done programmatically, but consider carefully what topic we
have been discussing this week! Each function can be exactly one line
"""
def letters_one(word1, word2):
    return sorted(set(word1) | set(word2))

def letters_both(word1, word2):
    return sorted(set(word1) & set(word2))

def letters_not(word1, word2):
    return sorted(set(word1) ^ set(word2))

# Testing the func
word1 = "cheese"
word2 = "sandesh"

result1 = letters_one(word1, word2)
result2 = letters_both(word1, word2)
result3 = letters_not(word1, word2)

result1, result2, result3
