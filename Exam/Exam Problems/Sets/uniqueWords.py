text1 = "the quick brown fox jumps over the lazy dog"
text2 = "the quick blue hedgehog dashes past the lazy fox"

words1 = set(text1.split())
words2 = set(text2.split())

onlyInFirst = words1 - words2
onlyInSecond = words2 - words1
inBoth = words1 & words2

print(f"Only in first: {onlyInFirst}")
print(f"Only in second: {onlyInSecond}")
print(f"In Both: {inBoth}")
