text1 = "the quick brown fox jumps over the lazy dog"
text2 = "the quick blue hedgehog dashes past the lazy fox"

# Split texts into words and convert to sets
words1 = set(text1.split())
words2 = set(text2.split())

# Find differences
only_in_text1 = words1 - words2
only_in_text2 = words2 - words1
both_texts = words1 & words2

print("Only in text1:", only_in_text1)
print("Only in text2:", only_in_text2)
print("In both texts:", both_texts)