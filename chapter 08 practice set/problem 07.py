l = ["harry", "rohan", "akash", "an"]
n = []

def rem(l, word):
    for item in l:
        if not(item == word):
            n.append(item.strip(word))
    return n        

print(rem(l, "an"))        