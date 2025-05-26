from collections import Counter

def closeStrings(word1: str, word2: str) -> bool:

    counter1 = Counter(word1)
    counter2 = Counter(word2)

    sortCounter1 = sorted(counter1.values())
    sortCounter2 = sorted(counter2.values())

    chars1 = set(counter1.keys())
    chars2 = set(counter2.keys())

    return sortCounter1 == sortCounter2 and chars1 == chars2


closeStrings("abc", "bca")
    