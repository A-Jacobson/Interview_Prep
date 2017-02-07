a = "cde"
b = "abc"

# approach
# anagrams have the same character frequency
# an array of len(vocab) if frequency arrays are the same strings are anagrams
# to find the distance we can calculate manhattan distance between the two arrays
# sum(abs([0, 1, 3] - [0, 0, 2])) = [0, 1, 1] = 2


def number_needed(a, b):
    a_freq = [0] * 26
    b_freq = [0] * 26

    vocab = 'abcdefghijklmnopqrstuvwxyz'
    char_to_int = {c:i for i, c in enumerate(vocab)}

    for char in a:
        index = char_to_int[char]
        a_freq[index] += 1

    for char in b:
        index = char_to_int[char]
        b_freq[index] += 1

    distance = 0
    for i in range(len(vocab)):
        distance += abs(a_freq[i] - b_freq[i])

    return distance

print number_needed(a, b)




