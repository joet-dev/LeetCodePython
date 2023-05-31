import collections

def groupAnagrams(strs): 
    letters_to_words = collections.defaultdict(list)
    for word in strs:
        letters_to_words[tuple(sorted(word))].append(word)

    return letters_to_words.values()

print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))