import re
import collections
import matplotlib.pyplot as plt
import numpy as np
text_file = open(r"C:\Users\ydrub\OneDrive\Documents\raven.txt", "r")

data = text_file.read()
text_file.close()


result = re.sub(r'[\xa0!]', '', data)
result = re.sub(r'[—,.\n!;\"]', ' ', result)
result=re.sub(' +', ' ', result)
result=result.rstrip()
result=result.lower()
result = result.replace("  ", " ")
print(result)

no_words = ['the', 'a', 'that', 'is', 'and', 'at', 'of', 'this', 'there']

for i in result:
    new = result.split(" ")



new = [i for i in new if i not in no_words]

print(new)
c = collections.Counter(new)
print(c)

word_count = []
words = []



for i in range(10):
    print(c.most_common()[i])
    word_count.append(c.most_common()[i][1])
    words.append(c.most_common()[i][0])

print(word_count)
words = tuple(words)
print(words)

plt.figure(figsize=(12,6))

plt.bar(np.arange(len(words)), word_count, color = (0.2,0.3,0.5,0.8))
plt.xticks(np.arange(len(words)), words)

plt.show()

plt.show()