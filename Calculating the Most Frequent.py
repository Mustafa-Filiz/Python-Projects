# First way

import collections
numbers = [1, 3, 7, 4, 3, 0, 3, 6, 3]
most_freq = collections.Counter(numbers).most_common(1)

print(most_freq)

print("The most frequent number is {} and it was {} times \
repeated".format(most_freq[0][0], numbers.count(most_freq[0][0])))

# Second way

numbers = [1, 3, 7, 4, 3, 0, 3, 6, 3]


print("The most frequent number is {} and it was {} times \
repeated".format(max(numbers, key = numbers.count), numbers.count(max(numbers, key = numbers.count))))
