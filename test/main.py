def romanToInt(s):
    romanNums = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    value = 0
    for i in range(len(s)):
        if i < len(s) - 1 and romanNums[s[i]] < romanNums[s[i+1]]:
            value -= romanNums[s[i]]
        else:
            value += romanNums[s[i]]
    return value

def longPrefix(strs):
    for i in range(100):
