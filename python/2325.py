from collections import OrderedDict

# * https://leetcode.com/problems/decode-the-message/

def decodeMessage(key: str, message: str) -> str:
    ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
    secret_mapper = {' ': ' '}
    i = 0
    res = ''

    for char in key:
        if char not in secret_mapper:
            secret_mapper[char] = ALPHABET[i]
            i += 1

    for char in message:
        res += secret_mapper[char]

    return res


print(decodeMessage(key = "the quick brown fox jumps over the lazy dog", message = "vkbs bs t suepuv")) # this is a secret
print(decodeMessage(key = "eljuxhpwnyrdgtqkviszcfmabo", message = "zwx hnfx lqantp mnoeius ycgk vcnjrdb")) # the five boxing wizards jump quickly

