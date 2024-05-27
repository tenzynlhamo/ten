def reverse_string(r):
    if len(r) <= 1:
        return r
    else:
        return reverse_string(r[1:]) + r[0]

s = input("Enter the word: ")
print(reverse_string(s))
