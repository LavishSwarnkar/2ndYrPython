strs = ["ABC", "def", "GHI", "jkl", "MNO"]
def convertor(s):
    if s.isupper():
        return s.lower()
    else:
        return s
strs2 = list(map(convertor, strs))
print(strs, "->", strs2)
