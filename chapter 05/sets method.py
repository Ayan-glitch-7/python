s = {1, 5, 45, 23, 5, 12}
print(s, type(s))

s.add(555)
print(s, type(s))

print(len(s))

s.remove(5)
print(s)

print(s.pop())

print(s.clear())

print(s.union({2, 3}))

print(s.intersection({23, 555}))
