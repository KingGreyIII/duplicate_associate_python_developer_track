"""Dataset: A string of text (pick any small paragraph).
Task:

Use Counter to count word frequencies.

Print the 5 most common words with .most_common(5)."""
# solution
from collections import Counter
text_content = """Now seven world think timed while her. Spoil large oh he rooms on since an. Am up unwilling eagerness perceived incommode. Are not windows set luckily musical hundred can. Collecting if sympathize middletons be of of reasonably. Horrible so kindness at thoughts exercise no weddings subjects. The mrs gay removed towards journey chapter females offered not. Led distrusts otherwise who may newspaper but. Last he dull am none he mile hold as."""
words = text_content.split()
word_count = Counter(words)
print(word_count.most_common(3))

# with open("dataset.txt", "r") as f:  # # # method 2
#     text = f.read()
