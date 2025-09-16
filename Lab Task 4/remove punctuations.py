a = "kuch bhi ! , kuch bhi?"
remove = "!,?"
b = ""
for i in a:
    if i not in remove:
        b += i
print(b)