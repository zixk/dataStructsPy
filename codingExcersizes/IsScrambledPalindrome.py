# Is Scrambled Palindrome
# Write a function that, given a string of letters, returns true or false for whether the letters in the string could be arranged to form a palindrome.
# E.g. For “torro”, the answer is True, because the letters can be rearranged to spell “rotor”.

def isScrambledPalindrome(letters):
    char_dict = {}
    for char in letters:
        if (char in char_dict):
            char_dict[char] += 1
        else:
            char_dict[char] = 1

    hasOneOdd = False
    for char in char_dict.keys():
        if(char_dict[char]%2 == 1):
            if(hasOneOdd):
                return False
            hasOneOdd = True
    return True
    print(char_dict)


if __name__ == "__main__":
    print(isScrambledPalindrome("torro"))
    print(isScrambledPalindrome("potato"))
    print(isScrambledPalindrome("tom tom and and jjeerry"))
