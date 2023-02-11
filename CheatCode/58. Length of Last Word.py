# using in-built methods
# def lenOfLastWord(s):
#     splits = s.split()
#     return len(splits[-1])

# This idea is more efficient since we can easily ignore the spaces from the last. The idea is to start incrementing the count when you encounter the first alphabet from the last and stop when you encounter a space after those alphabets.

def lenOfLastWord(s):
    c=0
    for i in s[::-1]:
        if i == ' ':
            if c>=1:
                return c
        else:
            c+=1
    return c

s = "   fly me   to   the moon  "
print(lenOfLastWord(s))

