###Program: Anagrams using recursion


def anagram(s):

    if s == "":
        return [s]
    else:
        ans = []
        for w in anagram(s[1:]):
            for pos in range(len(w)+1):
                ans.append(w[:pos] + s[0] + w[pos:])

        return ans
