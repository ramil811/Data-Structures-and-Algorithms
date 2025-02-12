strs = ["flower","flow","flight"]

print([s for s in strs])

for i in range(max(len(s) for s in strs)):
    print(f"index: {i}")
    try:
        print([s[i] for s in strs])
        print(set(s[i] for s in strs))
    except IndexError:
        break