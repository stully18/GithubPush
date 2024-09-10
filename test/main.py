def isValid(string):
    stack = []
    closeToOpen = {
        ")":"(",
        "]": "[",
        "}": "{"
    }

    for c in s:
        if c in closeToOpen:
            if stack and stack[-1] == closeToOpen[c]: