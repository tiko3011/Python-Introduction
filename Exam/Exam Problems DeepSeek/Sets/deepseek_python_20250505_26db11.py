text1 = "the quick brown fox jumps over the lazy dog"
text2 = "the quick blue hedgehog dashes past the lazy fox"

set1 = set(text1.split())
set2 = set(text2.split())

only_in_text1 = set1 - set2
only_in_text2 = set2 - set1
common_words = set1 & set2

print("Only in text1:", only_in_text1)
print("Only in text2:", only_in_text2)
print("Common words:", common_words)